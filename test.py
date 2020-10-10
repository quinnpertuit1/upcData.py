#!/usr/bin/env python3

import json, requests, sys, pprint
import pandas as pd 

d = []
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
   d = d.append(c)
   
e = pd.concat(d)
   
e.to_csv("upc.csv")