import csv
from decimal import *
from datetime import datetime
from datetime import date
from nsepython import *
import os.path

import sys

# total arguments
n = len(sys.argv)
symbol = 'SBIN'
# print("No of arguments:",n, sys.argv)
if n > 1 :
    symbol = sys.argv[1]
    print(symbol, end = " ")
format_string = "%Y-%m-%d"
mydict = {}
# f = 'BAJFINANCE-EQ-08-09-2023-to-08-09-2024.csv'
# f = 'Quote-Equity-WIPRO-EQ-09-09-2023-to-09-09-2024.csv'
# f = 'Quote-Equity-JIOFIN-EQ-09-09-2023-to-09-09-2024.csv'
# f = 'Quote-Equity-COALINDIA-EQ-09-09-2023-to-09-09-2024.csv'
# f = 'Quote-Equity-SBIN-EQ-09-09-2023-to-09-09-2024.csv'
f = symbol + '.csv'
start_date = "09-09-2023"
end_date = "09-09-2024"
if os.path.isfile(f) == False:
    print('File does not exist.')
    equity_history(symbol,'EQ',start_date, end_date).to_csv(f)
with open(f, mode='r',encoding='utf-8-sig') as infile:
    next(infile) # skip header
    reader = csv.reader(infile)
    mydict = dict((datetime.datetime.strptime(rows[20][0:10], format_string),rows[5]) for rows in reader)
    keys = sorted(mydict.keys())
    sorted_dict= {}
    for k in keys:
        sorted_dict[k] = mydict.get(k)
val = 0.0
for k,v in sorted_dict.items():
    v = float(v.replace(',',''))
    if v > val: 
        val = v
        print(k,v)
