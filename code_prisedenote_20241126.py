import requests
import pandas as pd
import os

response = requests.get("https://www.google.fr/")
response.status_code
response.content


response = requests.get("https://api.taceconomics.com/data/datasets")
response.status_code
response.content
type(response.content)
myData = response.json()
type(myData)
myData.keys()
myData = pd.DataFrame(myData["data"])
myData.iloc[0]



headers = {'Content-Type': 'application/json'
          ,'Accept':'application/json'}

apikey = ""
headers.update({"Authorization": "Bearer {}".format(apikey)})

res = requests.get(f"https://api.taceconomics.com/data/FRED/DCOILBRENTEU/GBR?start_date=2024-01-01&collapse=M&transform=growth_yoy"
                   , headers=headers)
res = res.json()
res = pd.DataFrame(res["data"])
res





