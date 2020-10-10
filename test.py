#!/usr/bin/env python3

import json, requests, sys, pprint
import pandas as pd 

d = pd.DataFrame()
indf = pd.read_csv("in.csv")

a1 = indf["upc"]

for i in a1:
   upc = i
   url ='https://api.upcitemdb.com/prod/trial/lookup?upc=%s' % (upc)
   response = requests.get(url)
   response.raise_for_status() 
   a = json.loads(response.text)
   b = a["items"]
   c = pd.DataFrame(b)
   d = pd.concat([d,c],axis=0, ignore_index=True)
   
   
d.to_csv("upc.csv")