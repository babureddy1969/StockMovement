import csv
from decimal import *
from datetime import datetime
from datetime import date
from nsepython import *
import os.path
import sys
stock_list = []
def getStockList():
  with open('EQUITY_L.csv', mode='r',encoding='utf-8-sig') as infile: 
    next(infile) # skip header
    reader = csv.reader(infile)
    for row in reader:
        stock_list.append(row[0])
    return stock_list
# print(stock_list)
# exit(0)
def getData():
    start_date = "10-09-2023"
    end_date = "10-09-2024"
    for symbol in stock_list:
        f = symbol + '.csv'
        if os.path.isfile(f) == False:
            print(symbol, ' File does not exist.')
            equity_history(symbol,'EQ',start_date, end_date).to_csv(f)
def process():
    format_string = "%Y-%m-%d"
    mydict = {}
    for f in stock_list:
        if os.path.isfile(f+'-result.csv') == True: continue
        print("Processing " + f)
        with open(f+".csv", mode='r',encoding='utf-8-sig') as infile:
            next(infile) # skip header
            reader = csv.reader(infile)
            for rows in reader:
                price = rows[5]
                if '-' in rows[5]:price = rows[7]
                mydict[datetime.datetime.strptime(rows[20][0:10], format_string)] = price
            keys = sorted(mydict.keys())
            sorted_dict= {}
            for k in keys:
                sorted_dict[k] = mydict.get(k)
        val = 0.0
        s = ""
        for k,v in sorted_dict.items():
            v = float(v.replace(',',''))
            if v > val: 
                # print(k,v, int(v-val))
                val = v
                s += k.strftime("%d-%m-%Y") + " " + str(v) + " " + str(int(v - val)) + '\n'
        with open(f+'-result.csv',"w") as fil:
            fil.write(s)
n = len(sys.argv)
symbol = ''
if n > 1 :
    symbol = sys.argv[1]
    print(symbol, end = " ")
    if symbol == "ALL": 
        getStockList()
    else :
        stock_list = [symbol]
        
    if n == 3 and sys.argv[2] == 'PROCESS': process()
    if n == 3 and sys.argv[2] == 'GETDATA': getData()
else:
    getStockList()
    getData()
    process()