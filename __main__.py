import requests
import yagmail
import os
from bs4 import BeautifulSoup

BASE_URL = [
'https://www.titan.fitness/racks/power-racks/x-3-series/x-3-half-rack/400406.html',
'https://www.titan.fitness/racks/squat-stands/x-3-series/x-3-series-short-squat-stand-with-spotter-arms/400422.html',
'https://www.titan.fitness/racks/squat-stands/x-3-series/x-3-series-tall-squat-stand-with-pull-up-bar-and-spotter-arms/400404.html',
'https://www.titan.fitness/racks/squat-stands/t-3-series/t-3-series-short-squat-stand-with-j-hooks/400925.2.html',
'https://www.titan.fitness/racks/squat-stands/t-3-series/titan-t-3-series-squat-stand-v2/400994.html',
'https://www.titan.fitness/strength/barbells/olympic/regular-bar-20kg---chrome/430086.html',
'https://www.titan.fitness/strength/weight-plates/cast-iron-plates/cast-iron-olympic-weight-plates-%7C-245-lb-set/430230.html'
]

# loop through the URLs above
for pg in BASE_URL:
	# query the website and return the html to the variable 'page'
	page = requests.get(pg)

	# parse the html using Beautiful Soup and store in variable 'soup'
	soup = BeautifulSoup(page.content, 'html.parser')

	# take out the <div> of name and get its value
	product_name_box = soup.find('span', attrs={'class': 'h1 product-name'})
	product_name = (product_name_box.text.strip())

	availability_box = soup.find('span', attrs={'class': 'availability-msg'})
	availability = (availability_box.text.strip())

	status = product_name + " - " + availability
	#print (status)
	#print ()

	# create text file
	with open ('titan.txt', "a") as txt_file:
		txt_file.write(status + '\n'+ '\n')

txt_file.close()

# email the text file as an attachment
FROM = 'george.davitiani@gmail.com'
TO = 'george.davitiani@gmail.com'
subject = 'Titan Fitness'
contents = 'titan.txt'
yag = yagmail.SMTP(FROM, 'hkxzacjexgundssc')
yag.send(TO, subject, contents)

# delete the file
os.remove('titan.txt')
