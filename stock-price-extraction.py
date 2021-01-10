### Extract stock market price from Yahoo Finance website
### Build a live stock market price prediction tool

import requests
from bs4 import BeautifulSoup

## Define a function stockprice() to extract stock prices from Yahoo Finance or any stock market website
def stockprice():
    ## requests packages,sends a request to the website and catches the response using get method
    req = requests.get('https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN')

    ## extract text from html response and parse using BeautifulSoup()
    soup = BeautifulSoup(req.text,'lxml')

    ## we select the current price from website,then right click 'inspect' to view page source
    ## and we note down the class name 'D(ib) Mend(20px)' of the particular div tag we want.
    ## we need to look into this class in span tags so use findAll() method.
    price = soup.find('div', {'class':'D(ib) Mend(20px)'}).findAll('span')

    ## we want stockprice() function to return the current price of that stock, enclose price[0] for first element
    return price[0].text

## print current price continuosly, hence use continuous while loop
while True:
    print('The current price: '+str(stockprice()))
