#!/usr/bin/env python3
"""
Run example queries on the integrated data
"""

import psycopg2

def run_queries():
    conn = psycopg2.connect('host=localhost port=5432 user=postgres password=password dbname=australian_companies')
    cursor = conn.cursor()

    # Query 1: Total companies by state
    cursor.execute('SELECT state, COUNT(*) AS company_count FROM integrated_companies GROUP BY state ORDER BY company_count DESC;')
    print('Companies by state:', cursor.fetchall())

    # Query 2: Top industries
    cursor.execute("SELECT industry, COUNT(*) AS count FROM integrated_companies WHERE industry IS NOT NULL GROUP BY industry ORDER BY count DESC LIMIT 10;")
    print('Top industries:', cursor.fetchall())

    # Query 3: Companies with websites
    cursor.execute('SELECT COUNT(*) AS companies_with_website FROM integrated_companies WHERE website_url IS NOT NULL;')
    print('Companies with websites:', cursor.fetchone()[0])

    cursor.close()
    conn.close()

if __name__ == '__main__':
    run_queries()
