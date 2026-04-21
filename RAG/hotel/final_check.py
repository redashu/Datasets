import csv

files = ["jan.csv", "jan_low.csv", "jan_avg.csv", "jan_case_mix.csv"]

for filename in files:
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        
        row_count = len(data)
        seasons = sorted(list(set(row['season'] for row in data)))
        scores = [float(row['review_score']) for row in data]
        
        print(f"File: {filename}")
        print(f"Rows: {row_count}")
        print(f"Seasons: {seasons}")
        print(f"Review Score: min={min(scores)}, max={max(scores)}")
        print("-" * 20)
    except Exception as e:
        print(f"Error processing {filename}: {e}")
