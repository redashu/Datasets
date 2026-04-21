import csv

files = ["jan_low.csv", "jan_avg.csv", "jan_case_mix.csv"]

for filename in files:
    print(f"--- Verification for {filename} ---")
    data = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    
    print(f"Row count: {len(data)}")
    
    seasons = set(row['season'] for row in data)
    print(f"Unique season values: {seasons}")
    
    scores = [float(row['review_score']) for row in data]
    print(f"Review Score range: min={min(scores)}, max={max(scores)}")
    
    print("First 2 rows:")
    for row in data[:2]:
        print(row)
    print()
