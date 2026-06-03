# Bluestock Mutual Fund Schema Data Dictionary

### 1. Table: `dim_fund` (Dimension Table)
* `amfi_code` (INTEGER, Primary Key): Unique operational code assigned to the mutual fund asset.
* `scheme_name` (TEXT): The full registration name of the fund scheme.
* `amc_name` (TEXT): Asset Management Company managing the scheme portfolio.

### 2. Table: `fact_nav` (Fact Table)
* `nav_id` (INTEGER, Primary Key Auto-increment): Unique record index.
* `amfi_code` (INTEGER, Foreign Key): Maps back to `dim_fund`.
* `date` (TEXT): Normalized datetime string for tracking.
* `nav` (REAL): Net Asset Value valuation price for the record entry.

### 3. Table: `fact_transactions` (Fact Table)
* `transaction_id` (INTEGER, Primary Key Auto-increment): Unique structural trade code.
* `customer_id` (TEXT): Masked user alphanumeric identifier.
* `transaction_type` (TEXT): Transaction method category (Sip, Lumpsum, Redemption).
* `amount` (REAL): Local absolute fiat transactional value.