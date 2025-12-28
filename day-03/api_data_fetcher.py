import requests
import os
import json

API_key = "K2XW0CNQJNB1Q37P"
api_url = "https://www.alphavantage.co/"
symbol = "IBM" # default argument
query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_key}"

print(f"{api_url}{query}\n")

def get_stock_market_data(symbol): 
       query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_key}"
       response = requests.get(url=api_url+query)
       data = response.json()
       keys_list = list(data.keys())
       
       if "Error Message"!=keys_list[0]:
           BASE_DIR = os.path.dirname(os.path.abspath(__file__))
           file_path = os.path.join(BASE_DIR, f"Output_{symbol}.json")
           with open(file_path, "w") as file:
               json.dump(data, file, indent=4)
           print(f"\n✅ Data successfully saved to Output_{symbol}.json\n")
       else :
            print (" ")
            print(data)
            print(" ❌ Retry to fetch data again .\n")

symbol = input("Enter the Symbol you want for the Stock Market API eg. (AMZN, Goog, etc) : ").upper()
get_stock_market_data(symbol)

