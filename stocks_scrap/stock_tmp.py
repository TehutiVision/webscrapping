import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# specify the url
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

# Get the data by getting its text
name = name_box

# strip() is used to remove starting and trailing
print(name)

# get the index price
price_box = soup.find('div', attrs={'class': 'price'})
price = price_box
print(price)

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name,price, datetime.now()])
