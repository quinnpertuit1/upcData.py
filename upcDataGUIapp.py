#!/usr/bin/env python3

####################################
# upcDataGUI macOS App v1.1        #
# Copyright (c) 2020 Quint Wingate #
# Licensed under Apache 2.0        #
####################################

import json, os, requests, sys, pyautogui

user = os.getlogin()

upc = pyautogui.prompt(text='Scan UPC:', title='UPCDataGUI')
upcSave = pyautogui.prompt(text='Save Name:', title='UPCDataGUI')

url ='https://api.upcitemdb.com/prod/trial/lookup?upc=%s' % (upc)
response = requests.get(url)
response.raise_for_status()

upcData = json.loads(response.text)
upcOutput = open('/Users/'+user+'/Downloads/'+upcSave+'.txt','w')

w = upcData['items']
print(w)
upcString = w[0]
upcOutput.write('Basic Info: \n\n')
upcOutput.write('Item: \n')
upcOutput.write(upcString['title'] + ' \n\n')
upcOutput.write('Description: \n')
upcOutput.write(upcString['description'] + ' \n\n')
upcOutput.write('Brand: \n')
upcOutput.write(upcString['brand'] + ' \n\n')
upcOutput.write('Model: \n')
upcOutput.write(upcString['model'] + ' \n\n')
upcOutput.write('Color: \n')
upcOutput.write(upcString['color'] + ' \n\n')
upcOutput.write('Size: \n')
upcOutput.write(upcString['size'] + ' \n\n')
upcOutput.write('Weight: \n')
upcOutput.write(upcString['weight'] + ' \n\n')
upcOutput.write('Lowest recorded price: \n')
upcOutput.write(str(upcString['lowest_recorded_price'])+(' \n\n'))
upcOutput.write('Highest recorded price: \n')
upcOutput.write(str(upcString['highest_recorded_price'])+(' \n\n\n'))
upcOutput.write('Barcodes: \n\n')
upcOutput.write('EAN: \n')
upcOutput.write(upcString['ean'] + ' \n\n')
upcOutput.write('UPC: \n')
upcOutput.write(upcString['upc'] + ' \n\n\n')

w = upcData['items'][0]['offers']
upcString = w[0]
upcOutput.write('Offers: \n\n')
upcOutput.write('Merchant: \n')
upcOutput.write(upcString['merchant'] + ' \n\n')
upcOutput.write('Link: \n')
upcOutput.write(upcString['link'] + ' \n\n')
upcOutput.write('Item:  \n')
upcOutput.write(upcString['title'] + ' \n\n')
upcOutput.write('Currency: \n')
upcOutput.write(upcString['currency'] + ' \n\n')
upcOutput.write('Price: \n')
upcOutput.write(str(upcString['price'])+(' \n\n'))
upcOutput.write('List Price: \n')
upcOutput.write(str(upcString['list_price'])+(' \n\n'))
upcOutput.write('Shipping: \n')
upcOutput.write(upcString['shipping'] + ' \n\n')
upcOutput.write('Condition: \n')
upcOutput.write(upcString['condition'] + ' \n\n')
upcOutput.write('Availability: \n')
upcOutput.write(upcString['availability'] + ' \n\n')

upcOutput.close()
