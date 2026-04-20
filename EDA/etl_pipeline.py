# etl_pipeline.py

import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# -------------------------------
# 1. DATABASE CONNECTION
# -------------------------------
def create_db_engine():
    username = "root"
    password = "your_password"
    host = "localhost"
    database = "your_db"

    engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")
    return engine


# -------------------------------
# 2. LOAD DATA
# -------------------------------
def load_data():
    purchases = pd.read_csv("data/purchases.csv")
    sales = pd.read_csv("data/sales.csv")
    vendors = pd.read_csv("data/vendors.csv")

    return purchases, sales, vendors


# -------------------------------
# 3. JOIN DATASETS
# -------------------------------
def join_datasets(purchases, sales, vendors):
    # Merge purchases + sales
    df = pd.merge(purchases, sales, on="ProductID", how="inner")

    # Merge vendors
    df = pd.merge(df, vendors, on="VendorNumber", how="left")

    return df


# -------------------------------
# 4. CLEAN DATA
# -------------------------------
def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df.fillna(0, inplace=True)

    # Remove inf values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)

    # Remove duplicate columns (important)
    df = df.loc[:, ~df.columns.duplicated()]

    return df


# -------------------------------
# 5. FEATURE ENGINEERING
# -------------------------------
def feature_engineering(df):
    # Total Purchase Dollars
    df["TotalPurchaseDollars"] = df["PurchasePrice"] * df["PurchaseQuantity"]

    # Total Sales Dollars
    df["TotalSalesDollars"] = df["SalesPrice"] * df["SalesQuantity"]

    # Gross Profit
    df["GrossProfit"] = df["TotalSalesDollars"] - df["TotalPurchaseDollars"]

    # Profit Margin
    df["ProfitMargin"] = (df["GrossProfit"] / df["TotalSalesDollars"]) * 100

    # Stock Turnover
    df["StockTurnover"] = df["SalesQuantity"] / df["PurchaseQuantity"]

    # Sales to Purchase Ratio
    df["SalestoPurchaseRatio"] = df["TotalSalesDollars"] / df["TotalPurchaseDollars"]

    return df


# -------------------------------
# 6. AGGREGATION (OPTIONAL)
# -------------------------------
def aggregate_data(df):
    summary = df.groupby(
        ["VendorNumber", "VendorName", "Brand", "Description"]
    ).agg({
        "PurchasePrice": "mean",
        "SalesPrice": "mean",
        "Volume": "mean",
        "PurchaseQuantity": "sum",
        "TotalPurchaseDollars": "sum",
        "SalesQuantity": "sum",
        "TotalSalesDollars": "sum",
        "GrossProfit": "sum"
    }).reset_index()

    return summary


# -------------------------------
# 7. LOAD TO MYSQL
# -------------------------------
def load_to_mysql(df, table_name, engine):
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"✅ Data loaded successfully into {table_name}")


# -------------------------------
# 8. MAIN PIPELINE FUNCTION
# -------------------------------
def run_pipeline():
    print("🚀 Starting ETL Pipeline...")

    # Load
    purchases, sales, vendors = load_data()
    print("✅ Data Loaded")

    # Join
    df = join_datasets(purchases, sales, vendors)
    print("✅ Data Joined")

    # Clean
    df = clean_data(df)
    print("✅ Data Cleaned")

    # Feature Engineering
    df = feature_engineering(df)
    print("✅ Features Added")

    # Aggregate
    summary_df = aggregate_data(df)
    print("✅ Data Aggregated")

    # DB Connection
    engine = create_db_engine()

    # Load
    load_to_mysql(summary_df, "vendor_sales_summary", engine)

    print("🎯 Pipeline Completed Successfully!")


# -------------------------------
# RUN SCRIPT
# -------------------------------
if __name__ == "__main__":
    run_pipeline()