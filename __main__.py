# pip install beautifulsoup4
# pip install boto3
# pip install requests

import boto3
import email.utils
import importlib
import os
import requests
import smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import urls
importlib.reload(urls)
from urls import URL_LIST

# loop through the URLs
for each_url in URL_LIST:
    try:
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
    except Exception:
        continue
    else:
        # create a text file
        with open('inventory.txt', 'a') as f:
            f.write(status + '\n' + '\n')

def send_email():
    CHARSET = 'utf-8'
    AWS_REGION = 'us-west-2'
    SENDER = 'george.davitiani@gmail.com'
    RECIPIENT = 'george.davitiani@hey.com'
    SUBJECT = 'Inventory Report'
    ATTACHMENT = 'inventory.txt'
    BODY_TEXT = ('email body text goes here.')
    BODY_HTML = """<html>
        <head></head>
        <body>
            <h1> email headline goes here</h1>
            <p> email body text goes here. </p>
        </body>
        </html>"""

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Create a multipart/mixed parent container.
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    # Define the attachment part and encode it using MIMEApplication.
    att = MIMEApplication(open(ATTACHMENT, 'rb').read())

    # Add a header to tell the email client to treat this part as an attachment, and to give the attachment a name.
    att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

    # Attach the multipart/alternative child container to the multipart/mixed parent container.
    msg.attach(msg_body)

    # Add the attachment to the parent container.
    msg.attach(att)

    response = client.send_raw_email(
        Source=SENDER,
        Destinations=[RECIPIENT],
        RawMessage={'Data':msg.as_string(),},
    )

# email if keywords are found in the text file
with open('inventory.txt') as f:
    if 'In Stock' in f.read():
        send_email()
    elif 'Backorder' in f.read():
        send_email()
    elif 'Select Styles for Availability' in f.read():
        send_email()

# delete the text file
os.remove('inventory.txt')
