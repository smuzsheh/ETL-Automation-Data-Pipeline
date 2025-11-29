import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import os

class ETLPipeline:
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://user:pass@localhost/securetech_db')
    
    def extract(self):
        # Simulate multiple data sources
        sales_data = pd.read_csv('data/raw_sales.csv')
        customer_data = pd.read_excel('data/customer_records.xlsx')
        web_data = pd.read_json('data/web_analytics.json')
        return sales_data, customer_data, web_data
    
    def transform(self, sales_df, customer_df, web_df):
        # Data cleaning and transformation
        sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])
        sales_df = sales_df.dropna(subset=['customer_id', 'amount'])
        
        customer_df = customer_df.fillna({'region': 'Unknown'})
        customer_df = customer_df[customer_df['status'] == 'Active']
        
        # Merge datasets
        merged_df = pd.merge(sales_df, customer_df, on='customer_id', how='left')
        
        return merged_df
    
    def load(self, clean_df):
        # Load to data warehouse
        clean_df.to_sql('sales_warehouse', self.engine, if_exists='replace', index=False)
        print("ETL process completed successfully!")

# Execute pipeline
if __name__ == "__main__":
    etl = ETLPipeline()
    sales, customers, web = etl.extract()
    clean_data = etl.transform(sales, customers, web)
    etl.load(clean_data)
