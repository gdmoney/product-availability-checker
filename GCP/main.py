import os
import requests
import yagmail
from bs4 import BeautifulSoup

BASE_URL = [
'https://www.titan.fitness/strength/weight-plates/bumper-plates/230-lb-set-economy-black-bumper-plates/430117.html',
'https://www.titan.fitness/strength/weight-plates/bumper-plates/45-lb-single-economy-black-bumper-plate/430105.2.html',
'https://www.titan.fitness/strength/weight-plates/cast-iron-plates/45-lb-single-cast-iron-olympic-plates/430232.html',
'https://www.titan.fitness/strength/weight-plates/cast-iron-plates/10-lb-pair-cast-iron-olympic-plates/430210.html',
'https://www.titan.fitness/strength/weight-plates/cast-iron-plates/5-lb-pair-cast-iron-olympic-plates/430209.html',
'https://www.titan.fitness/strength/dumbbells/rubber-coated-hex/pair-of-75-lb-black-rubber-coated-hex-dumbbells/421076.html',
'https://www.titan.fitness/strength/dumbbells/rubber-coated-hex/pair-of-85-lb-black-rubber-coated-hex-dumbbells/421086.html',
'https://www.titan.fitness/strength/dumbbells/rubber-coated-hex/pair-of-90-lb-black-rubber-coated-hex-dumbbells/421091.html',
'https://www.titan.fitness/strength/dumbbells/neoprene/neoprene-light-weight-dumbbell-set---1%2C-2%2C-3-%2C-4-lb/420003.html',
'https://www.titan.fitness/strength/specialty-machines/lower-body/economy-h-pnd/401027.html'
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
