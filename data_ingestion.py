import os
import glob
import pandas as pd
from pathlib import Path

def run_data_ingestion():
    # Find the data/raw folder dynamically
    base_dir = Path(__file__).resolve().parent
    raw_data_dir = base_dir / "data" / "raw"
    
    print("="*60)
    print("🚀 STARTING TASK 3: INGESTING ALL 10 RAW CSV FILES")
    print("="*60)
    
    csv_pattern = os.path.join(raw_data_dir, "[0-1][0-9]_*.csv")
    csv_files = sorted(glob.glob(csv_pattern))
    
    if not csv_files:
        print(f"❌ Error: No numbered CSV files found in: {raw_data_dir}")
        return
        
    datasets = {}
    for file_path in csv_files:
        filename = os.path.basename(file_path)
        try:
            df = pd.read_csv(file_path)
            datasets[filename] = df
            print(f"✅ Successfully loaded: {filename} | Shape: {df.shape}")
        except Exception as e:
            print(f"❌ Could not read {filename}: {e}")

    print("\n" + "="*60)
    print("🔍 STARTING TASK 6: EXPLORING FUND MASTER PROFILE")
    print("="*60)
    
    fund_master_file = "01_fund_master.csv"
    if fund_master_file in datasets:
        fm_df = datasets[fund_master_file]
        print("Available columns in your Fund Master file:", list(fm_df.columns))
        
        # Flexibly find columns even if spelling is slightly off
        fh_col = [c for c in fm_df.columns if 'fund_house' in c or 'amc' in c.lower()]
        cat_col = [c for c in fm_df.columns if 'category' in c.lower() and 'sub' not in c.lower()]
        sub_col = [c for c in fm_df.columns if 'sub_category' in c.lower() or 'sub-category' in c.lower()]
        risk_col = [c for c in fm_df.columns if 'risk' in c.lower()]
        
        if fh_col: print(f"🏢 Unique Fund Houses: {fm_df[fh_col[0]].nunique()}")
        if cat_col: print(f"🗂️  Unique Categories: {fm_df[cat_col[0]].nunique()}")
        if sub_col: print(f"📋 Unique Sub-Categories: {fm_df[sub_col[0]].nunique()}")
        if risk_col: print(f"⚠️  Unique Risk Grades: {fm_df[risk_col[0]].unique()}")
    else:
        print(f"❌ Could not find {fund_master_file}")

    print("\n" + "="*60)
    print("🛡️  STARTING TASK 7: REFERENTIAL INTEGRITY VALIDATION")
    print("="*60)
    
    nav_history_file = "02_nav_history.csv"
    if fund_master_file in datasets and nav_history_file in datasets:
        fm_df = datasets[fund_master_file]
        nav_df = datasets[nav_history_file]
        
        # Find scheme code columns dynamically
        code_col_fm = [c for c in fm_df.columns if 'code' in c.lower() or 'scheme' in c.lower()]
        code_col_nav = [c for c in nav_df.columns if 'code' in c.lower() or 'scheme' in c.lower()]
        
        if code_col_fm and code_col_nav:
            fm_codes = set(fm_df[code_col_fm[0]])
            nav_codes = set(nav_df[code_col_nav[0]])
            missing_codes = fm_codes - nav_codes
            
            print(f"🔢 Total schemes in Master Registry: {len(fm_codes)}")
            print(f"🔢 Total schemes in NAV Logs: {len(nav_codes)}")
            print(f"⚠️  Count of missing codes in NAV History: {len(missing_codes)}")
            if missing_codes:
                print(f"📋 Sample of missing Scheme Codes: {list(missing_codes)[:5]}")
        else:
            print("❌ Scheme code columns could not be identified automatically.")

if __name__ == "__main__":
    run_data_ingestion()