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
     for key1, value1 in response.json().items ():
      for key2, value2 in value1.items() :
           print("")
           if isinstance(value2, dict):
               print(f"# Date : {key2} \n" )
               for key3, value3 in value2.items() :
                  print (f"{key3} : {value3}")
           else : 
               print (f"{key2} : {value2}")  
    
     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
     file_path = os.path.join(BASE_DIR, f"Output_{symbol}.json")
     # "__file__" is a built-in Python variable that stores the path of the current Python file.
     # "os.path.abspath"  It converts the file path into a full absolute path.
     # "os.path.dirname" extracts path till folder excludes file.
     # "os.path.join" jions folder path and file name
     
     # Open text file in append mode
     with open( file_path, "a", encoding="utf-8") as file: # "a"  append mode : append existing file , or create new one if not exists , encoding="utf-8" supports all text characters safely.
        file.write(f"===== Stock Data for {symbol} =====\n\n")
        
        for key1, value1 in response.json().items():
            for key2, value2 in value1.items():
                if isinstance(value2, dict):
                    file.write(f"\n# Date : {key2}\n")
                       
                    for key3, value3 in value2.items():
                        file.write(f"{key3} : {value3}\n")
                else:
                    file.write(f"{key2} : {value2}\n")

     print(f"\n✅ Data successfully saved to Output_{symbol}.txt\n")
         

symbol = input("Enter the Symbol you want for the Stock Market API eg. (AMZN, Goog, etc) : ").upper()
is_timeseries = True
get_stock_market_data(symbol)