import os
import pandas as pd
from pathlib import Path

def clean_mutual_fund_data():
    base_dir = Path(__file__).resolve().parent
    raw_dir = base_dir / "data" / "raw"
    processed_dir = base_dir / "data" / "processed"
    
    os.makedirs(processed_dir, exist_ok=True)
    
    print("="*60)
    
    # --- TASK 1: CLEAN NAV HISTORY ---
    print("🧼 Cleaning nav_history.csv...")
    nav_df = pd.read_csv(raw_dir / "02_nav_history.csv")
    nav_df['date'] = pd.to_datetime(nav_df['date'], errors='coerce')
    nav_df = nav_df.sort_values(by=['amfi_code', 'date'])
    nav_df['nav'] = nav_df.groupby('amfi_code')['nav'].ffill()
    nav_df = nav_df.drop_duplicates()
    nav_df = nav_df[nav_df['nav'] > 0]
    nav_df.to_csv(processed_dir / "02_nav_history_clean.csv", index=False)
    print(f"✅ Saved clean NAV History. Shape: {nav_df.shape}")

    # --- TASK 2: CLEAN INVESTOR TRANSACTIONS ---
    print("\n🧼 Cleaning investor_transactions.csv...")
    trans_df = pd.read_csv(raw_dir / "08_investor_transactions.csv")
    
    # Fix: Clean up column names by removing spaces and making lowercase
    trans_df.columns = trans_df.columns.str.strip().str.lower()
    
    # Standardize transaction_type values
    if 'transaction_type' in trans_df.columns:
        trans_df['transaction_type'] = trans_df['transaction_type'].str.strip().str.capitalize()
    
    # Dynamic fix for the 'amount' key error
    amt_col = [col for col in trans_df.columns if 'amount' in col]
    if amt_col:
        trans_df = trans_df[trans_df[amt_col[0]] > 0]
        
    if 'transaction_date' in trans_df.columns:
        trans_df['transaction_date'] = pd.to_datetime(trans_df['transaction_date'], errors='coerce')
        
    if 'kyc_status' in trans_df.columns:
        trans_df['kyc_status'] = trans_df['kyc_status'].str.strip().str.upper()
    
    trans_df.to_csv(processed_dir / "08_investor_transactions_clean.csv", index=False)
    print(f"✅ Saved clean Transactions. Shape: {trans_df.shape}")

    # --- TASK 3: CLEAN SCHEME PERFORMANCE ---
    print("\n🧼 Cleaning scheme_performance.csv...")
    perf_df = pd.read_csv(raw_dir / "07_scheme_performance.csv")
    perf_df.columns = perf_df.columns.str.strip().str.lower()
    
    return_cols = [c for c in perf_df.columns if 'return' in c or 'pct' in c]
    for col in return_cols:
        perf_df[col] = pd.to_numeric(perf_df[col], errors='coerce')
        
    exp_col = [col for col in perf_df.columns if 'expense' in col]
    if exp_col:
        perf_df = perf_df[(perf_df[exp_col[0]] >= 0.1) & (perf_df[exp_col[0]] <= 2.5)]
        
    perf_df.to_csv(processed_dir / "07_scheme_performance_clean.csv", index=False)
    print(f"✅ Saved clean Performance details. Shape: {perf_df.shape}")
    print("="*60)

if __name__ == "__main__":
    clean_mutual_fund_data()