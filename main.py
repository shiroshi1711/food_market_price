from fetch import  fetch_data
from transform import clean_data
from database import save_to_database
from datetime import date, timedelta
import time

def main():
    start_date = date(2026, 1, 1)
    end_date = date.today()
    current_date = start_date
    days =[]
    while current_date <= end_date:
        days.append(str(current_date))
        current_date += timedelta(days=1)
    for day in days:
        data = fetch_data(day)
        df = clean_data(data)
        save_to_database(df, 'food_prices')
        
        print(f"Saved {len(df)} rows")
        time.sleep(3)

if __name__ == "__main__":
    main()