# This function get real time crypto currency price every day at 8AM
# this also save the data as csv
# It identify top 10 crypto and send mails

import requests
import pandas as pd
from datetime import datetime

# API information
url = 'https://api.coingecko.com/api/v3/coins/markets'
param = {
    'vs_currency' : 'usd',
    'order' : 'market_cap_desc',
    'per_page': 250,
    'page': 1
}

# sending requests
response = requests.get(url, params=param)

if response.status_code == 200:
    print('Connection Successfull! \nGetting the data...')
    
    # storing the response into data
    data = response.json()
    
    # creating df dataframe
    df = pd.DataFrame(data)
    
    # print(df.columns)
    # print(df.head())
    df = df[[
        'id','current_price', 'market_cap', 'price_change_percentage_24h',
        'ath', 'atl'
    ]]
    
    #creating new columns
    today =  datetime.now().strftime('%d-%m-%Y %S:%M:%H')
    df['time_stamp'] = today
    
    # getting top 10
    top_negative = df.sort_values(by='price_change_percentage_24h', ascending=True)
    top_negative_10 = top_negative.head(10)
    top_negative_10.to_csv(f'top_negative_10 of {today} .csv', index=False)
    
    # positive top
    top_positive = df.sort_values(by='price_change_percentage_24h', ascending=False)
    top_positive_10 = top_positive.head(10)
    top_positive_10.to_csv(f'top_positive_10 of {today} .csv', index=False)
    
    
    # saving the data
    df.to_csv(f'crypto_data {today}.csv', index=False)
    print(f'Top 10 crypto with highest price decrease % {today} \n{top_negative_10}')
    print(f'Top 10 crypto with highest price increase % {today} \n{top_positive_10}')
    
    print("Data saved successfull!")
    
else:
    print(f"Connection Failed Error Code {response.status_code}")
    




