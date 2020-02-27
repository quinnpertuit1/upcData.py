#!/usr/bin/env python3

import json, requests, sys, pprint

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: upcData.py upc')
    sys.exit()
upc = ' '.join(sys.argv[1:])

# Download the JSON data from UPCItemDB.com's API
url ='https://api.upcitemdb.com/prod/trial/lookup?upc=%s' % (upc)
response = requests.get(url)
response.raise_for_status() # check for errors

# Load JSON data into a Python variable.
upcData = json.loads(response.text)
#pprint.pprint(upcData)                      # show pprint.pprint


# Print requested item
w = upcData['items']
print()
print('Basic Info: ##########')
print()
print('Item:')
print(w[0]['title'])
print()
print('Description:')
print(w[0]['description'])
print()
print('Brand:')
print(w[0]['brand'])
print()
print('Model:')
print(w[0]['model'])
print()
print('Color:')
print(w[0]['color'])
print()
print('Size:')
print(w[0]['size'])
print()
print('Weight:')
print(w[0]['weight'])
print()
print('Lowest recorded price:')
print(w[0]['lowest_recorded_price'])
print()
print('Highest recorded price:')
print(w[0]['highest_recorded_price'])
print()
print('Barcodes: ##########')
print()
print('EAN:')
print(w[0]['ean'])
print()
print('UPC:')
print(w[0]['upc'])
print()
print('ASIN:')
print(w[0]['asin'])
print()

w = upcData['items'][0]['offers']
print('Offers: ##########')
print()
print('Merchant:')
print(w[0]['merchant'])
print()
print('Link:')
print(w[0]['link'])
print()
print('Item:')
print(w[0]['title'])
print()
print('Currency:')
print(w[0]['currency'])
print()
print('Price:')
print(w[0]['price'])
print()
print('List Price:')
print(w[0]['list_price'])
print()
print('Shipping:')
print(w[0]['shipping'])
print()
print('Condition:')
print(w[0]['condition'])
print()
print('Availability:')
print(w[0]['availability'])
print()
