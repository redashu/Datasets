import csv
import random
from datetime import datetime, timedelta

header = [
    "booking_id", "date", "room_id", "room_type", "status", "price", "guest_count", 
    "check_in", "check_out", "wifi", "parking", "breakfast", "season", "occupancy_level", 
    "guest_name", "country", "payment_method", "booking_channel", "stay_purpose", 
    "discount_pct", "review_score", "special_request"
]

room_types = ["Single", "Double", "Suite", "Deluxe"]
statuses = ["Available", "Booked", "Cancelled", "No-Show"]
countries = ["USA", "UK", "Canada", "Germany", "France", "Japan", "Australia"]
payments = ["Credit Card", "PayPal", "Cash", "Debit Card"]
channels = ["Direct", "Agency", "Online", "Corporate"]
purposes = ["Leisure", "Business", "Event"]
special_requests = ["None", "High Floor", "Extra Bed", "Late Check-in", "Early Check-out"]

def generate_file(filename, start_id, season_val, scenario):
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        
        for i in range(500):
            bkg_id = f"BKG{start_id + i}"
            date = f"2025-01-{random.randint(1, 31):02d}"
            room_id = f"R{random.randint(100, 500)}"
            room_type = random.choice(room_types)
            
            # Scenario tuning
            if scenario == "low":
                status = random.choices(statuses, weights=[60, 20, 15, 5])[0]
                price = random.randint(50, 120)
                occupancy = "Low"
                discount = random.randint(0, 10)
            elif scenario == "avg":
                status = random.choices(statuses, weights=[30, 50, 15, 5])[0]
                price = random.randint(100, 200)
                occupancy = random.choice(["Low", "Medium", "High"])
                discount = random.randint(5, 20)
            elif scenario == "case_mix":
                status = random.choices(statuses, weights=[20, 50, 20, 10])[0]
                # Price spread
                price = random.randint(40, 300)
                # Weekend spikes
                d_obj = datetime.strptime(date, "%Y-%m-%d")
                if d_obj.weekday() >= 4: # Friday, Sat, Sun
                    occupancy = "High"
                else:
                    occupancy = random.choice(["Low", "Medium"])
                discount = random.randint(0, 40) # higher promo spikes
            
            if status == "Available":
                guest_count = 0
                check_in = ""
                check_out = ""
            else:
                guest_count = random.randint(1, 4)
                ci_day = random.randint(1, 25)
                co_day = ci_day + random.randint(1, 5)
                check_in = f"2025-01-{ci_day:02d}"
                check_out = f"2025-01-{co_day:02d}"
                
            row = {
                "booking_id": bkg_id,
                "date": date,
                "room_id": room_id,
                "room_type": room_type,
                "status": status,
                "price": price,
                "guest_count": guest_count,
                "check_in": check_in,
                "check_out": check_out,
                "wifi": random.choice(["Yes", "No"]),
                "parking": random.choice(["Yes", "No"]),
                "breakfast": random.choice(["Yes", "No"]),
                "season": season_val,
                "occupancy_level": occupancy,
                "guest_name": f"Guest_{start_id + i}",
                "country": random.choice(countries),
                "payment_method": random.choice(payments),
                "booking_channel": random.choice(channels),
                "stay_purpose": random.choice(purposes),
                "discount_pct": discount,
                "review_score": round(random.uniform(3.0, 5.0), 1),
                "special_request": random.choice(special_requests)
            }
            writer.writerow(row)

generate_file("jan_low.csv", 2001, "Low", "low")
generate_file("jan_avg.csv", 3001, "Average", "avg")
generate_file("jan_case_mix.csv", 4001, "Mixed", "case_mix")
