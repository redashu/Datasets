import csv
import random
import datetime

def generate_monthly_data():
    seasons_map = {
        1: "Peak", 2: "Moderate", 3: "Moderate", 4: "Low",
        5: "Peak", 6: "Peak", 7: "Low", 8: "Moderate",
        9: "Low", 10: "Peak", 11: "Peak", 12: "Peak"
    }
    
    occupancy_map = {
        "Peak": "High",
        "Moderate": "Medium",
        "Low": "Low"
    }

    room_types = ["Standard", "Deluxe", "Suite"]
    base_prices = {"Standard": 100, "Deluxe": 200, "Suite": 400}
    season_multipliers = {"Peak": 1.5, "Moderate": 1.2, "Low": 1.0}
    
    statuses = ["Booked", "Cancelled", "No-Show", "Available"]
    channels = ["Direct", "OTA", "Travel Agent"]
    purposes = ["Leisure", "Business"]
    payment_methods = ["Credit Card", "Debit Card", "Cash"]
    countries = ["USA", "UK", "Germany", "France", "Japan", "Canada"]
    names = ["John Smith", "Emma Jones", "Hans Muller", "Yuki Tanaka", "Marie Dubois"]

    fieldnames = [
        "booking_id", "date", "room_id", "room_type", "status", "price",
        "guest_count", "check_in", "check_out", "wifi", "parking", "breakfast",
        "season", "occupancy_level", "guest_name", "country", "payment_method",
        "booking_channel", "stay_purpose", "discount_pct", "review_score", "special_request"
    ]

    for month in range(1, 13):
        filename = f"hotel_2025_{month:02d}.csv"
        season = seasons_map[month]
        occupancy = occupancy_map[season]
        
        # Probabilities for status based on season
        if season == "Peak":
            probs = [0.75, 0.1, 0.05, 0.1]
        elif season == "Moderate":
            probs = [0.5, 0.15, 0.05, 0.3]
        else: # Low
            probs = [0.3, 0.1, 0.05, 0.5]

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for i in range(1, 501):
                status = random.choices(statuses, weights=probs)[0]
                room_type = random.choice(room_types)
                base = base_prices[room_type]
                mult = season_multipliers[season]
                price = round(base * mult * random.uniform(0.9, 1.1), 2)
                
                day = random.randint(1, 28)
                current_date = datetime.date(2025, month, day)
                
                if status == "Available":
                    guest_count = 0
                    check_in = ""
                    check_out = ""
                else:
                    guest_count = random.randint(1, 4)
                    check_in = current_date.isoformat()
                    check_out = (current_date + datetime.timedelta(days=random.randint(1, 5))).isoformat()

                row = {
                    "booking_id": f"B{month:02d}{i:04d}",
                    "date": current_date.isoformat(),
                    "room_id": f"R{random.randint(100, 500)}",
                    "room_type": room_type,
                    "status": status,
                    "price": price,
                    "guest_count": guest_count,
                    "check_in": check_in,
                    "check_out": check_out,
                    "wifi": random.choice(["Yes", "No"]),
                    "parking": random.choice(["Yes", "No"]),
                    "breakfast": random.choice(["Yes", "No"]),
                    "season": season,
                    "occupancy_level": occupancy,
                    "guest_name": random.choice(names) if status != "Available" else "",
                    "country": random.choice(countries) if status != "Available" else "",
                    "payment_method": random.choice(payment_methods) if status != "Available" else "",
                    "booking_channel": random.choice(channels) if status != "Available" else "",
                    "stay_purpose": random.choice(purposes) if status != "Available" else "",
                    "discount_pct": random.randint(0, 20),
                    "review_score": round(random.uniform(3.0, 5.0), 1),
                    "special_request": random.choice(["None", "Late check-in", "Extra towels"]) if status != "Available" else ""
                }
                writer.writerow(row)

if __name__ == "__main__":
    generate_monthly_data()
