from datetime import datetime as dt, timedelta
from config import API_URL
import requests

def fetch_data():
    date = str(dt.today().date() - timedelta(days=1))
    url = API_URL+date
    response = requests.post(url)
    if response.status_code == 200:
        data = response.json()['data']
    else:
        print(f'Something went wrong : {response.status_code}')

    return data