import requests # allows us to download the html
from bs4 import BeautifulSoup # import web scraper
import pprint
import smtplib
from email.message import EmailMessage
from pathlib import Path # this is similar to os.path -- allows us to access files
from string import Template # string Template allows you to substitute variables inside of texts

# html = Path('index.html').read_text()

html = Template(Path('index.html').read_text())

email = EmailMessage() # this is our email object

email['from'] = 'Cordawg'
email['to'] = 'cory.send.it@gmail.com'
email['subject'] = "Today's weather in bonita Miami"

email.set_content(html.substitute({'name': 'Cordawg'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('cory.send.it@gmail.com', 'bonfrerebehavior')
    smtp.send_message(email)
    print('this email is sent')

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=25.75622500000003&lon=-80.20751499999994#.X3X6WpNKgc9')

# print(res)

# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser') #parse this into html

# print(soup.body)

# print(soup.find_all('div'))

ab = soup.find_all('a')

# print(a)

count = 0

for a in ab:
    count += 1
    print(f'There are {count} a-tags')

print(id)

conditions = soup.find(id='current_conditions_detail').find_all('td')

print(conditions)

# print(divs)

# print(soup.find_all('a'))

# use css selectors to find data


# def create_custom_survivor(links, divs):
#     custom_survivor = []
#     return custom_survivor

# create_custom_survivor(links, divs)