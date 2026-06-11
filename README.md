# Mutual Fund Performance Analytics & Risk Scorecard

An advanced financial analytics pipeline built to evaluate, risk-adjust, and rank mutual fund schemes against market benchmark baselines. This project processes historical Net Asset Value (NAV) data to extract trailing returns, market volatility regressions, and downside risk profiles.

## 📊 Project Scope & Deliverables

This repository contains the end-to-end quantitative data sprint files:
* **`Performance_Analytics.ipynb`**: Core execution environment handling returns, CAGR matrix configurations, and analytics modeling.
* **`fund_scorecard.csv`**: Automated evaluation matrix scoring all funds across a standardized 0-100 system.
* **`alpha_beta.csv`**: Target regression export showcasing underlying portfolio beta dynamics and alpha generation.
* **`benchmark_comparison_chart.png`**: Interactive 3-year performance trend tracking line visualization.
* **Mutual_Fund_Performance_Dashboard.pbix:** Interactive 3-page business intelligence layer mapping the final analytics engine into production-ready visual modules (featuring Industry Overview, Alpha vs. Beta risk scatter matrices, and trailing performance curves).
---

## 🛠️ Performance & Risk Metrics Calculated

### 1. Trailing Performance (CAGR)
Calculates the Compound Annual Growth Rate over 1-year, 3-year, and 5-year horizons to establish normalized long-term tracking metrics.

### 2. Risk-Adjusted Ratios
* **Sharpe Ratio**: Measures the excess return generated per unit of total portfolio volatility.
* **Sortino Ratio**: Narrowly isolates downside deviation to evaluate performance against negative return sequences.
* *Note: Calculations assume a standard Risk-Free Rate (Rf) proxy baseline of 6.5%.*

### 3. OLS Linear Regression (Alpha & Beta)
Regresses fund historical daily returns against the market baseline index to extract:
* **Beta**: Systemic market sensitivity index.
* **Alpha**: Annualized excess returns generated purely via manager strategy selection.

### 4. Maximum Drawdown (Max DD)
Tracks peak-to-trough drops row-by-row to outline structural capital risk thresholds along with specific historical calendar event start and end dates.

---

## 🏆 Weighted Scoring Framework

The composite ranking score (0-100) dynamically normalizes tracking positions across five strict parameters:

| Metric | Weight Allocation | Direction Preference |
| :--- | :--- | :--- |
| **3-Year Trailing CAGR** | 30% | Higher is Better |
| **Annualized Sharpe Ratio** | 25% | Higher is Better |
| **Annualized Alpha** | 20% | Higher is Better |
| **Expense Ratio** | 15% | Lower is Better (Inverse) |
| **Maximum Drawdown** | 10% | Smaller Drop is Better (Inverse) |

## 📊 Power BI Dashboard Pages
* **Page 1: Industry Overview** — High-level overview of different fund houses.
* **Page 2: Risk Analysis** — Alpha vs. Beta scatter plot and a clean risk ratio table.
* **Page 3: Return Profile** — Bar charts comparing 1-year, 3-year, and 5-year returns side-by-side.

## 🧪 Day 6: Advanced Financial Analytics & Quant Risk Metrics

Expanded the repository engine to process advanced risk tracking, investor behaviors, and automated portfolio evaluation pipelines:

* **Quantitative Risk Engine (`var_cvar_report.csv`)**: Computes 95% Historical Value at Risk (VaR) and 95% Conditional Value at Risk (CVaR) to mathematically evaluate potential downside boundaries across 40 mutual fund schemes.
* **Volatility Over Time Visualization (`rolling_sharpe_chart.png`)**: A dynamic line graph mapping the annualized rolling 90-day Sharpe Ratio timeline to identify performance consistency across key equity funds.
* **Investor Behavior Metrics**:
    * *Cohort Analysis*: Aggregates average SIP subscription levels and aggregate capital distributions segmented by client activation year.
    * *Continuity Pipeline*: Tracks sequential payment dates to isolate transaction anomalies exceeding 35-day windows, identifying a portfolio churn risk rate of 90.54%.
* **Sector Concentration Analysis**: Implemented the Herfindahl-Hirschman Index (HHI) mathematical model ($\sum (\text{weight}_i)^2$) across asset sectors to flag funds carrying high concentration vs. safe structural diversification.
* **Interactive Fund Recommender (`recommender.py`)**: A standalone terminal utility that parses fund scorecards and returns localized top-3 fund recommendations optimized by Sharpe ratios for **Low**, **Moderate**, or **High** user risk-appetites.

 ## 🚀 Day 7: Final Deliverables & Pipeline Integration

The final stage of the capstone project focuses on operational automation, comprehensive documentation, and executive-level reporting to transition the analytics engine into a production-ready asset.

* **Master Pipeline Automation (`run_pipeline.py`):** Developed a unified orchestration script that sequences data ingestion, triggers cleaning routines, executes the advanced financial analytics engines, and refreshes the downstream database layers in a single, automated workflow.
* **Executive Presentation Deck:** Formulated a 10-slide high-impact presentation detailing the end-to-end data architecture, system integrity safeguards, quantitative risk boundaries, and user churn trends for leadership review.
* **Comprehensive Capstone Report (`Final_Report.pdf`):** Compiled a exhaustive technical and strategic document detailing the system methodology, mathematical frameworks ($\Sigma(\text{weight}_i)^2$), empirical findings, and deployment architecture.
