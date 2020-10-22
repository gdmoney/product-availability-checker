import os
import requests
import yagmail
from bs4 import BeautifulSoup

BASE_URL = [
'https://www.titan.fitness/strength/weight-plates/bumper-plates/230-lb-set-economy-black-bumper-plates/430117.html',
'https://www.titan.fitness/strength/weight-plates/bumper-plates/45-lb-single-economy-black-bumper-plate/430105.2.html',
'https://www.titan.fitness/strength/weight-plates/bumper-plates/25-lb-pair-economy-black-bumper-plates/430103.2.html',
'https://www.titan.fitness/racks/rack-accessories/t-3-series/t-3-series-spotter-arms/400413.html',
'https://www.titan.fitness/racks/rack-accessories/t-3-series/t-3-series-dual-pull-up-stabilizer-bar/400307.html',
'https://www.titan.fitness/racks/rack-accessories/t-3-series/olympic-weight-plate-holder-for-t-3-power-rack-3-inchx2-inch-tube/400116.html'
]

# loop through the URLs above
for page in BASE_URL:
    # query each website and return html, parse the html using Beautiful Soup and store in variable 'soup'
    soup = BeautifulSoup(requests.get(page).content, 'html.parser')

    # take out the <div> of name and get its value
    product_name_box = soup.find('span', attrs={'class': 'h1 product-name'})
    product_name = (product_name_box.text.strip())

    price_box = soup.find('span', attrs={'class': 'sales'})
    price = (price_box.text.strip())

    availability_box = soup.find('span', attrs={'class': 'availability-msg'})
    availability = (availability_box.text.strip())

    status = 'Product Name: ' + product_name + '\n' + 'Price:        ' + price + '\n' + 'Availability: ' + availability

    # create a text file
    with open ('/tmp/titan.txt', 'a') as f:
        f.write(status + '\n' + '\n')

def send_email():
    FROM = 'george.davitiani@gmail.com'
    TO = 'george.davitiani@gmail.com'
    subject = 'Titan Fitness Inventory Report'
    #contents = '/tmp/titan.txt'
    contents = [yagmail.inline('/tmp/titan.txt')]
    yag = yagmail.SMTP(FROM, 'zmytgndtkxdukwwk')
    yag.send(TO, subject, contents)

# email if keywords are found in the text file
def hello_pubsub(event, context):
    with open('/tmp/titan.txt') as f:
        if 'In Stock' in f.read():
            send_email()
        elif 'Backorder' in f.read():
            send_email()
        elif 'Select Styles for Availability' in f.read():
            send_email()
