# Clothing Brand SQL Database

Fictional SQL database for a clothing brand – products, sales and stock management.

## What it does
- Creates 3 linked tables : products, sales, stocks
- Inserts fictional data
- Runs business queries : total revenue, best-selling product, stock alerts

## Queries
- `SUM` – total revenue
- `JOIN` + `ORDER BY` – best-selling product
- `JOIN` + `WHERE` – stock alert detection

## Tech
- Python + SQLite3
# Clothing Brand SQL Database

Fictional SQL database for a clothing brand – products, sales and stock management.

## What it does
- Creates 3 linked tables : products, sales, stocks
- Inserts fictional data
- Runs business queries : total revenue, best-selling product, stock alerts

## Database Structure

**Products**
| id | nom | categorie | prix |
|----|-----|-----------|------|
| 1 | Veste | Haut | 90€ |
| 2 | Jean | Bas | 85€ |
| 3 | T-shirt | Haut | 35€ |

**Sales**
| id | produit_id | quantite | date_vente | chiffre_affaires |
|----|------------|----------|------------|------------------|
| 1 | 1 | 17 | 2025-04-16 | 1530€ |
| 2 | 2 | 22 | 2025-04-16 | 1870€ |
| 3 | 3 | 40 | 2025-04-1§ | 1400€ |
