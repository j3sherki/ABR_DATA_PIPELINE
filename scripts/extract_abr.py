#!/usr/bin/env python3
"""
Download and process Australian Business Register (ABR) data.
"""

import requests
import pandas as pd
import io

def download_abr_data():
    """Download ABR data from data.gov.au."""
    # Latest ABR data URL (CSV)
    url = "https://data.gov.au/data/dataset/australian-business-register-abr-data/download/abrv202401.csv"
    response = requests.get(url)
    response.raise_for_status()
    
    # Read CSV directly
    df = pd.read_csv(io.StringIO(response.text), low_memory=False)
    return df

def process_abr_data():
    """Process ABR CSV files."""
    df = download_abr_data()
    if df is not None:
        # Select relevant columns (adjust based on actual CSV)
        # Assuming columns like 'ABN', 'Entity name', 'Main business location', etc.
        columns = ['ABN', 'Entity name', 'Main business location', 'Postcode', 'State']
        df = df[columns]
        df.columns = ['abn', 'business_name', 'address', 'postcode', 'state']
        # Clean data
        df = df.dropna(subset=['abn'])
        df.to_csv('data/abr_processed.csv', index=False)
        print(f"Processed {len(df)} ABR records.")
    else:
        print("Failed to download ABR data.")

if __name__ == '__main__':
    process_abr_data()