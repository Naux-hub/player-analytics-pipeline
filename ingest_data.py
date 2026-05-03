import duckdb
import os

con = duckdb.connect('ecommerce.db')

# Kontrollera att alla nio rader finns med här:
mapping = {
    'olist_customers_dataset': 'raw_customers',
    'olist_orders_dataset': 'raw_orders',
    'olist_order_items_dataset': 'raw_items',
    'olist_products_dataset': 'raw_products',
    'olist_order_payments_dataset': 'raw_payments',
    'olist_order_reviews_dataset': 'raw_reviews',
    'olist_sellers_dataset': 'raw_sellers',
    'olist_geolocation_dataset': 'raw_geo',
    'product_category_name_translation': 'raw_category_translation'
}

print("--- Startar inläsning ---")
for file_name, table_name in mapping.items():
    path = f'data/{file_name}.csv'
    if os.path.exists(path):
        print(f"Laddar: {file_name} --> {table_name}")
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{path}')")
    else:
        print(f"VARNING: Hittade inte {path}")

con.close()
print("---")
print("Nu är databasen 'ecommerce.db' helt redo med 9 tabeller!")