def stockHistoryYF(ticker, start_date, end_date):
    import pandas as pd
    #from pandas_datareader import data as pdr
    import fix_yahoo_finance as yf
    import datetime
    import csv
    import matplotlib.pyplot as plt

# Data is name for function pulling stock info from Yahoo stock
# For start and end input was converted to int and parsed to get Day, Month and Year
# Year[0:4], Month[5:7], Day[8:10]
    data = yf.download(ticker, start=datetime.datetime(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])),
                          end=datetime.datetime(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])))
    dailyGrowth = data['Close'] - data['Open'] # Close - Open to give growth over trading day
    tickerString = str(ticker)[2:-2] # Converts ticker to str and removes ['']
    #print(ticker)
    #print(data)
    print(dailyGrowth)
# create unique csv file name to include stock symbol and date range.
    filename = tickerString + '_from_'+ start_date + '_to_' + end_date + '_Data_YF.csv'

    data.to_csv(filename,mode = 'a',header ='column_names')

# Create plots and save them to file
# First subplot plots the daily open and close value against each other
# to see how the stock moved during the day
    #fig, axs = plt.subplots(1, 1, constrained_layout=True)
    plt.plot(data['Open'], 'b',data['Close'], 'r')
    plt.xlabel('Date')
    plt.ylabel('Value (USD)')
    plt.legend(['Open', 'Close'],loc='upper left')
    plt.title('Daily open and close values')
    plt.suptitle(tickerString)
    imageName = tickerString + '_from_'+ start_date + '_to_' + end_date + '_Data_YF.pdf'
    plt.savefig(imageName)
    #plt.show()
    plt.close()

# Second subplot plots the daily growth (i.e. close value - open value)
# to see how the stock moved over the day and percentage growth

    plt.plot(dailyGrowth)
    plt.xlabel('Date')
    plt.ylabel('Percentage')
    #plt.legend(['Open', 'Close'],loc='upper left')
    plt.title('Daily growth')
    plt.suptitle(tickerString)
    imageName = tickerString + '_from_'+ start_date + '_to_' + end_date + '_Daily_Growth_YF.pdf'
    plt.savefig(imageName)
    #plt.show()
    plt.close()
