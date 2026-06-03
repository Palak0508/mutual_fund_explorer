import os
import sqlite3
import pandas as pd
from pathlib import Path

def build_and_load_db():
    base_dir = Path(__file__).resolve().parent
    processed_dir = base_dir / "data" / "processed"
    raw_dir = base_dir / "data" / "raw"
    db_path = base_dir / "bluestock_mf.db"
    schema_path = base_dir / "schema.sql"
    
    print("="*60)
    print("🗄️ Initializing SQLite Database Setup...")
    
    # Connect to SQLite (Fresh start)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Read and execute schema.sql to build our tables properly
    print("🛠️ Reading database architecture from schema.sql...")
    with open(schema_path, 'r') as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    conn.commit()
    print("✨ Database tables initialized successfully!")
    
    # Load Clean Fund Master (Dimension)
    print("\n📥 Loading dim_fund table...")
    fund_df = pd.read_csv(raw_dir / "01_fund_master.csv")
    fund_df.columns = fund_df.columns.str.strip().str.lower()
    fund_df.to_sql('dim_fund', conn, if_exists='replace', index=False)
    print(f"✅ Loaded {len(fund_df)} funds into dim_fund.")
    
    # Load Clean NAV History (Fact)
    print("\n📥 Loading fact_nav table...")
    nav_df = pd.read_csv(processed_dir / "02_nav_history_clean.csv")
    nav_df.columns = nav_df.columns.str.strip().str.lower()
    nav_df.to_sql('fact_nav', conn, if_exists='replace', index=False)
    print(f"✅ Loaded {len(nav_df)} entries into fact_nav.")
    
    # Load Clean Investor Transactions (Fact)
    print("\n📥 Loading fact_transactions table...")
    trans_df = pd.read_csv(processed_dir / "08_investor_transactions_clean.csv")
    trans_df.columns = trans_df.columns.str.strip().str.lower()
    
    # FIX: If the column is named 'investor_id', rename it to match the SQL schema
    if 'investor_id' in trans_df.columns:
        trans_df = trans_df.rename(columns={'investor_id': 'customer_id'})
        
    trans_df.to_sql('fact_transactions', conn, if_exists='replace', index=False)
    print(f"✅ Loaded {len(trans_df)} records into fact_transactions.")
    
    # Load Clean Performance Metrics (Fact)
    print("\n📥 Loading fact_performance table...")
    perf_df = pd.read_csv(processed_dir / "07_scheme_performance_clean.csv")
    perf_df.columns = perf_df.columns.str.strip().str.lower()
    perf_df.to_sql('fact_performance', conn, if_exists='replace', index=False)
    print(f"✅ Loaded {len(perf_df)} rows into fact_performance.")
    
    conn.close()
    print("="*60)
    print("🎉 Success! All datasets matched, mapped, and loaded into bluestock_mf.db!")
    print("="*60)

if __name__ == "__main__":
    build_and_load_db()