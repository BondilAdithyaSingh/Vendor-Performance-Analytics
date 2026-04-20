# 📊 Vendor Performance Analytics — End-to-End Data Project

An end-to-end data analytics project that analyzes vendor sales performance using Python, MySQL, and Power BI. The project covers the full data pipeline — from raw Excel ingestion to business insights and an interactive dashboard.

---

## 🗂️ Project Structure

```
Vendor-Performance-Analytics/
│
├── data/
│   └── vendor_sales_summary.csv
│
├── notebooks/
│   ├── Exploratory_Data_Analysis.ipynb
│   └── Vendor_Performance_Analysis.ipynb
│
├── scripts/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── dashboard/
│   └── vendor_performance.pbix
│
├── reports/
│   └── Vendor_Performance_Report.pdf
│
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python (Pandas, Matplotlib, Seaborn) | Data cleaning, EDA, visualizations |
| MySQL + MySQL Workbench | Database storage and querying |
| SQLAlchemy | Connecting Jupyter Notebook to MySQL |
| Jupyter Notebook | Analysis environment |
| Power BI | Interactive dashboard |
| Excel | Raw data source |

---

## 🔄 Project Pipeline

### 1. 🔌 Data Ingestion & Database Connection
- Loaded multiple Excel datasets into Jupyter Notebook
- Connected to MySQL Workbench using **SQLAlchemy's** `create_engine()`
- Used `read_sql_query()` to pull data directly from the database into Pandas DataFrames
- Pushed processed tables back to MySQL using `to_sql()`

```python
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
df = pd.read_sql_query("SELECT * FROM vendor_data", con=engine)
```

### 2. 🔗 Data Engineering
- Joined multiple datasets across tables to build a unified data model
- Redesigned and redeveloped the schema for better analytical structure

### 3. 🧹 Data Cleaning
- Handled missing values and standardized inconsistent formats
- Detected and removed outliers to ensure data reliability

### 4. ⚡ SQL Query Optimization
- Identified a slow-running SQL query causing major performance bottlenecks
- Rewrote and optimized the query — reducing execution time significantly

### 5. 📊 Exploratory Data Analysis (EDA)
- Built multiple visualizations to uncover patterns in vendor behavior
- Explored relationships between key metrics:
  - Sales volume vs. profit margins
  - Delivery performance trends
  - Inventory turnover rates
  - Top vs. low-performing vendors

### 6. 💡 Business Problem Solving
- Identified top-performing and underperforming vendors
- Uncovered slow-moving inventory causing capital inefficiency
- Delivered actionable insights for procurement, pricing, and vendor strategy

---

## 📈 Key Business Insights

- **Vendor Segmentation** — Classified vendors into top and low performers based on sales and margin data
- **Inventory Optimization** — Identified slow-moving stock tying up significant capital
- **Profit Margin Analysis** — Compared margin distributions across vendor groups
- **Delivery Performance** — Evaluated on-time vs. delayed delivery patterns

---

## 📋 Deliverables

- ✅ Cleaned and structured vendor dataset
- ✅ EDA notebook with visualizations
- ✅ Automated vendor summary Python script
- ✅ Interactive Power BI dashboard
- ✅ Final PDF report with business recommendations

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Vendor-Performance-Analytics.git
   cd Vendor-Performance-Analytics
   ```

2. **Install dependencies**
   ```bash
   pip install pandas matplotlib seaborn sqlalchemy pymysql jupyter
   ```

3. **Set up MySQL connection**
   - Open `ingestion_db.py` and update your MySQL credentials
   - Run the script to load data into your database:
   ```bash
   python scripts/ingestion_db.py
   ```

4. **Run the notebooks**
   ```bash
   jupyter notebook
   ```
   - Start with `Exploratory_Data_Analysis.ipynb`
   - Then run `Vendor_Performance_Analysis.ipynb`

5. **View the dashboard**
   - Open `vendor_performance.pbix` in Power BI Desktop

---

## 📦 Dependencies

```
pandas
matplotlib
seaborn
sqlalchemy
pymysql
jupyter
```

Install all at once:
```bash
pip install pandas matplotlib seaborn sqlalchemy pymysql jupyter
```

---


## 📬 Connect

Feel free to connect with me on [LinkedIn]([https://www.linkedin.com/in/adithya-singh-b9697a335/]) or check out my other projects on [GitHub](https://github.com/BondilAdithyaSingh).

---

