Solution: removed this broken URL

'https://www.titan.fitness/strength/weight-plates/cast-iron-plates/cast-iron-olympic-weight-plates-%7C-245-lb-set/430230.html'

=====

	product_name_box = soup.find('span', attrs={'class': 'h1 product-name'})
    product_name = product_name_box.text.strip()

    price_box = soup.find('span', attrs={'class': 'sales'})
    price = price_box.text.strip()

    availability_box = soup.find('span', attrs={'class': 'availability-msg'})
    availability = availability_box.text.strip()

Traceback (most recent call last):
  File "1.py", line 32, in <module>
    product_name = product_name_box.text.strip()
AttributeError: 'NoneType' object has no attribute 'text'

=====

    product_name_box = soup.find('span', attrs={'class': 'h1 product-name'})
    product_name = str(product_name_box.text.strip())

    price_box = soup.find('span', attrs={'class': 'sales'})
    price = str(price_box.text.strip())

    availability_box = soup.find('span', attrs={'class': 'availability-msg'})
    availability = str(availability_box.text.strip())

Traceback (most recent call last):
  File "1.py", line 32, in <module>
    product_name = str(product_name_box.text.strip())
AttributeError: 'NoneType' object has no attribute 'text'

=====

    product_name_box = soup.find('span', attrs={'class': 'h1 product-name'})
    product_name = product_name_box.strip()

    price_box = soup.find('span', attrs={'class': 'sales'})
    price = price_box.strip()

    availability_box = soup.find('span', attrs={'class': 'availability-msg'})
    availability = availability_box.strip()

Traceback (most recent call last):
  File "1.py", line 32, in <module>
    product_name = product_name_box.strip()
TypeError: 'NoneType' object is not callable

=====



