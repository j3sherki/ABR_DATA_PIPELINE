#!/usr/bin/env python3
"""
Set up PostgreSQL database schema and roles
"""

import psycopg2
from psycopg2 import sql

def setup_database():
    # Connection parameters - update as needed
    conn_params = {
        'host': 'localhost',
        'port': 5432,
        'user': 'postgres',
        'password': 'password',
        'database': 'australian_companies'
    }

    try:
        # Connect to database
        conn = psycopg2.connect(**conn_params)
        conn.autocommit = True
        cursor = conn.cursor()

        # Read and execute schema.sql
        with open('sql/schema.sql', 'r') as f:
            schema_sql = f.read()
        cursor.execute(schema_sql)
        print("Schema executed successfully.")

        # Create reader role
        cursor.execute("CREATE ROLE reader LOGIN PASSWORD 'readerpass';")
        print("Reader role created.")

        # Grant permissions
        cursor.execute("GRANT SELECT ON integrated_companies TO reader;")
        cursor.execute("GRANT USAGE ON SCHEMA public TO reader;")
        print("Permissions granted to reader role.")

        cursor.close()
        conn.close()
        print("Database setup complete.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    setup_database()
