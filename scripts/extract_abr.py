#!/usr/bin/env python3
"""
Download and process Australian Business Register (ABR) data.
"""

import requests
import pandas as pd
import zipfile
import io
from bs4 import BeautifulSoup

def download_abr_data():
    """Download ABR data from data.gov.au."""
    # Latest ABR data URL (ZIP)
    url = "https://data.gov.au/data/dataset/australian-business-register-abr-data/download/abrv202401.zip"
    response = requests.get(url)
    response.raise_for_status()
    
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        csv_files = [f for f in z.namelist() if f.endswith('.csv')]
        if csv_files:
            with z.open(csv_files[0]) as f:
                # Read with robust parsing
                try:
                    df = pd.read_csv(f, low_memory=False, on_bad_lines='skip', encoding='utf-8', sep=',', quotechar='"', escapechar='\\')
                except pd.errors.ParserError:
                    f.seek(0)
                    df = pd.read_csv(f, low_memory=False, on_bad_lines='skip', encoding='latin1', sep=';', quotechar='"')
                return df
    return None

def process_abr_data():
    """Process ABR CSV files."""
    df = download_abr_data()
    if df is not None:
        print("Columns in ABR data:", df.columns.tolist())
        # Select relevant columns (adjust based on actual CSV)
        # Assuming columns like 'ABN', 'Entity name', 'Main business location', etc.
        columns = ['ABN', 'Entity name', 'Main business location', 'Postcode', 'State']
        df = df[columns]
        df.columns = ['abn', 'business_name', 'address', 'postcode', 'state']
        # Clean data
        df = df.dropna(subset=['abn'])
        # Limit for demo
        df = df.head(10000)
        df.to_csv('data/abr_processed.csv', index=False)
        print(f"Processed {len(df)} ABR records.")
    else:
        print("Failed to download ABR data.")

if __name__ == '__main__':
    process_abr_data()