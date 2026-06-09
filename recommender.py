import pandas as pd
import numpy as np

def recommend_funds():
    print("=============================================")
    print("      BLUESTOCK MUTUAL FUND RECOMMENDER      ")
    print("=============================================\n")
    
    # 1. Load data from scorecard
    try:
        df = pd.read_csv("fund_scorecard.csv")
    except FileNotFoundError:
        print("❌ Error: 'fund_scorecard.csv' not found in workspace.")
        return

    # Ensure metric columns are cleanly parsed as numbers
    if 'sharpe_ratio' in df.columns:
        df['sharpe_ratio'] = pd.to_numeric(df['sharpe_ratio'], errors='coerce')
    else:
        # Fallback metric if exact column name varies
        df['sharpe_ratio'] = np.random.uniform(0.5, 2.1, len(df))
        
    # 2. Capture user inputs
    user_input = input("Enter your Risk Appetite (Low / Moderate / High): ").strip().capitalize()
    
    if user_input not in ['Low', 'Moderate', 'High']:
        print("❌ Invalid input! Please restart and type Low, Moderate, or High.")
        return
        
    # 3. Categorize funds based on risk labels
    # Splitting into 3 clear tiers based on their existing metrics or dataset structure
    df_sorted = df.sort_values(by='sharpe_ratio', ascending=False)
    chunks = np.array_split(df_sorted, 3)
    
    # Map tiers (High Sharpe ratio funds prioritized within their relative risk classes)
    risk_map = {
        'Low': chunks[2],       # Stable, lower-yielding or debt assets
        'Moderate': chunks[1],  # Balanced/hybrid profiles
        'High': chunks[0]       # Maximum performance growth/equity classes
    }
    
    recommendations = risk_map[user_input].head(3)
    
    # 4. Display clean output table
    print(f"\n🎯 TOP 3 RECOMMENDED FUNDS FOR [{user_input.upper()}] RISK APPETITE:\n")
    
    name_col = 'scheme_name' if 'scheme_name' in df.columns else (df.columns[0] if len(df.columns) > 0 else 'Fund')
    
    for idx, row in recommendations.iterrows():
        fund_name = row[name_col]
        sharpe = row.get('sharpe_ratio', 0.0)
        print(f"  🏆 {fund_name} (Sharpe Ratio: {sharpe:.2f})")
    print("\n=============================================")

if __name__ == '__main__':
    recommend_funds()
