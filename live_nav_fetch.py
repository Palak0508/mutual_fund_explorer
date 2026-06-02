import os
import requests
import pandas as pd
from pathlib import Path

# 1. Define where to save the files safely
# Since this file is in the root folder, we only go 1 level up (.parent)
BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# 2. List of Mutual Fund Scheme Codes requested by Bluestock
schemes = {
    "125497": "hdfc_top_100_direct",
    "119551": "sbi_bluechip",
    "120503": "icici_bluechip",
    "118632": "nippon_large_cap",
    "119092": "axis_bluechip",
    "120841": "kotak_bluechip"
}

def fetch_mutual_fund_data():
    print("Starting live NAV data fetch from mfapi.in...")
    
    for code, name in schemes.items():
        url = f"https://api.mfapi.in/mf/{code}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()
                
                # Extract the historical NAV rows
                nav_rows = json_data.get('data', [])
                
                if not nav_rows:
                    print(f"⚠️ No data found for code {code}")
                    continue
                
                # Convert into a clean table format
                df = pd.DataFrame(nav_rows)
                
                # Add columns for identifying the scheme
                df['scheme_code'] = code
                df['scheme_name'] = json_data.get('meta', {}).get('scheme_name', name)
                
                # Save it as a CSV file in data/raw/
                output_file = RAW_DATA_DIR / f"live_nav_{code}.csv"
                df.to_csv(output_file, index=False)
                print(f"  Successfully saved: live_nav_{code}.csv ({name})")
            else:
                print(f"❌ Failed to fetch code {code}. Status code: {response.status_code}")
                
        except Exception as e:
            print(f"❌ An error occurred while fetching code {code}: {e}")

if __name__ == "__main__":
    fetch_mutual_fund_data()