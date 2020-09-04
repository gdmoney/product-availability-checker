# install requests
# install yagmail
# install beautifulsoup4

import os
import requests
import yagmail
from bs4 import BeautifulSoup

BASE_URL = [
'https://www.titan.fitness/racks/power-racks/x-3-series/x-3-half-rack/400406.html',
'https://www.titan.fitness/racks/squat-stands/x-3-series/x-3-series-short-squat-stand-with-spotter-arms/400422.html',
'https://www.titan.fitness/racks/squat-stands/x-3-series/x-3-series-tall-squat-stand-with-pull-up-bar-and-spotter-arms/400404.html',
'https://www.titan.fitness/racks/squat-stands/t-3-series/t-3-series-short-squat-stand-with-j-hooks/400925.2.html',
'https://www.titan.fitness/racks/squat-stands/t-3-series/titan-t-3-series-squat-stand-v2/400994.html',
'https://www.titan.fitness/strength/weight-plates/bumper-plates/230-lb-set-economy-black-bumper-plates/430117.html',
'https://www.titan.fitness/strength/weight-plates/cast-iron-plates/cast-iron-olympic-weight-plates-%7C-245-lb-set/430230.html',
'https://www.titan.fitness/strength/dumbbells/rubber-coated-hex/pair-of-75-lb-black-rubber-coated-hex-dumbbells/421076.html',
'https://www.titan.fitness/strength/dumbbells/rubber-coated-hex/pair-of-100-lb-black-rubber-coated-hex-dumbbells/421101.html'
]

# loop through the URLs above
for page in BASE_URL:
	# query each website and return html, parse the html using Beautiful Soup and store in variable 'soup'
	soup = BeautifulSoup(requests.get(page).content, 'html.parser')

	# take out the <div> of name and get its value
	product_name_box = soup.find('span', attrs={'class': 'h1 product-name'})
	product_name = (product_name_box.text.strip())

	availability_box = soup.find('span', attrs={'class': 'availability-msg'})
	availability = (availability_box.text.strip())

	status = "Product Name: " + product_name + '\n' + "Availability: " + availability

	# create a text file
	with open ('titan.txt', "a") as f:
		f.write(status + '\n' + '\n')

def send_email():
	FROM = 'george.davitiani@gmail.com'
	TO = 'george.davitiani@gmail.com'
	subject = 'Titan Fitness'
	contents = 'titan.txt'
	yag = yagmail.SMTP(FROM, 'hkxzacjexgundssc')
	yag.send(TO, subject, contents)

# email if one of the  products is available
if 'In Stock' or 'Backorder' in f.read():
    send_email()
	f.close()
else
	f.close()

# delete the file
os.remove('titan.txt')