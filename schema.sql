-- DAY 2: SQL Database Schema Architecture 

-- 1. Dimension Table: Funds
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT NOT NULL,
    scheme_type TEXT,
    scheme_category TEXT,
    scheme_sub_category TEXT,
    risk_level TEXT,
    amc_name TEXT
);

-- 2. Fact Table: NAV Time-Series History
CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date TEXT,
    nav REAL NOT NULL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- 3. Fact Table: Investor Transactions
CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    customer_id TEXT,
    transaction_date TEXT,
    transaction_type TEXT,
    amount REAL,
    units REAL,
    kyc_status TEXT,
    state TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- 4. Fact Table: Scheme Performance Metrics
CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code INTEGER PRIMARY KEY,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,
    sharpe_ratio REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);