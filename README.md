# Mutual Fund Performance Analytics & Risk Scorecard

An advanced financial analytics pipeline built to evaluate, risk-adjust, and rank mutual fund schemes against market benchmark baselines. This project processes historical Net Asset Value (NAV) data to extract trailing returns, market volatility regressions, and downside risk profiles.

## 📊 Project Scope & Deliverables

This repository contains the end-to-end quantitative data sprint files:
* **`Performance_Analytics.ipynb`**: Core execution environment handling returns, CAGR matrix configurations, and analytics modeling.
* **`fund_scorecard.csv`**: Automated evaluation matrix scoring all funds across a standardized 0-100 system.
* **`alpha_beta.csv`**: Target regression export showcasing underlying portfolio beta dynamics and alpha generation.
* **`benchmark_comparison_chart.png`**: Interactive 3-year performance trend tracking line visualization.

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
