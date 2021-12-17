import importlib
import os
import requests
import yagmail
from bs4 import BeautifulSoup
from importlib import util

import urls
importlib.reload(urls)
from urls import URL_LIST

# loop through the URLs
for each_url in URL_LIST:
    # query each website and return html, parse the html using Beautiful Soup and store in variable 'soup'
    page = requests.get(each_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # take out the <div> of name and get its value
    product_name_box = soup.find('h1', attrs={'class': 'h1 product-name text-uppercase d-none d-sm-block large-devices'})
    product_name = product_name_box.text.strip()

    price_box = soup.find('span', attrs={'class': 'sup-hide'})
    price = price_box.text.strip()

    availability_box = soup.find('span', attrs={'class': 'availability-msg'})
    availability = availability_box.text.strip()

    status = 'Product Name: ' + product_name + '\n' + 'Price:        ' + price + '\n' + 'Availability: ' + availability

    # create a text file
    with open ('/tmp/inventory.txt', 'a') as f:
        f.write(status + '\n' + '\n')

def send_email():
    FROM = 'george.davitiani@gmail.com'
    TO = 'george.davitiani@hey.com'
    subject = 'Inventory Report'
    #contents = '/tmp/inventory.txt'
    contents = [yagmail.inline('/tmp/inventory.txt')]
    yag = yagmail.SMTP(FROM, 'zmytgndtkxdukwwk')
    yag.send(TO, subject, contents)

# email if keywords are found in the text file
def hello_pubsub(event, context):
    with open('/tmp/inventory.txt') as f:
        if 'In Stock' in f.read():
            send_email()
        elif 'Backorder' in f.read():
            send_email()
        elif 'Select Styles for Availability' in f.read():
            send_email()
