import requests
import json
import pandas as pd
import datetime

# get request
resp = requests.get("https://api.llama.fi/protocols/") # https://docs.llama.fi/api
data = resp.json()


top_ten = data[:10] #by tvl
df_top_ten = pd.DataFrame.from_dict(top_ten)
df_top_ten.insert(2,"mcap/tvl",df_top_ten['mcap']/df_top_ten['tvl']) # important metric <1 is good (value buy)
def today():
        return datetime.date.today().strftime("%Y%m%d")

filename = f'defi_llama_stats_{today()}.csv'
df_top_ten.to_csv(f'./data/{filename}',index=False)


