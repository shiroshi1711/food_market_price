from fetch import  fetch_data
from transform import clean_data
from database import save_to_database

def main():
    data = fetch_data()
    df = clean_data(data)
    save_to_database(df, 'food_prices')

    
if __name__ == "__main__":
    main()