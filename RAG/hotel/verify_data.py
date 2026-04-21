import csv
import glob
import os

files = sorted(glob.glob("hotel_2025_*.csv"))

for filename in files:
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        
        row_count = len(data)
        seasons = sorted(list(set(row['season'] for row in data)))
        scores = [float(row['review_score']) for row in data]
        sample_row = data[0] if data else "N/A"
        
        print(f"File: {filename}")
        print(f"  Rows: {row_count}")
        print(f"  Season Values: {seasons}")
        print(f"  Review Score: min={min(scores)}, max={max(scores)}")
        print(f"  Sample Row: {sample_row}")
        print("-" * 50)
    except Exception as e:
        print(f"Error processing {filename}: {e}")
