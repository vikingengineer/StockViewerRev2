import pandas as pd
import csv
import stockHistoryYFRev2 as shyf


# open CSV file with stock tickers in one column
with open('File.csv', 'r') as f:
    reader = csv.reader(f)
    stock = list(reader)
for i in range(len(stock)):

# Select start and end dates to pull data for stocks in format YYYY-MM-DD
    shyf.stockHistoryYF(stock[i],'YYYY-MM-DD', 'YYYY-MM-DD')


print('FINISHED')

