# Clothing Brand SQL Database

Fictional SQL database for a clothing brand – products, sales and stock management.  
**Stack :** Python, SQLite3

## What it does
- Creates 3 linked tables : products, sales, stocks
- Inserts fictional data
- Runs business queries : total revenue, best-selling product, stock alerts

## Queries
- `SUM` – total revenue
- `JOIN` + `ORDER BY` – best-selling product
- `JOIN` + `WHERE` – stock alert detection

## Database Structure

| Table | Key columns |
|---|---|
| Products | id, name, category, price |
| Sales | id, product_id, quantity, date, revenue |
| Stocks | id, product_id, quantity_available |

## How to Run
1. Clone the repository
2. Run `python3 clothing_brand_db.py`
