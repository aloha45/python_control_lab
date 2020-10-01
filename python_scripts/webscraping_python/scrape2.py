import requests
from pprint import pprint
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from pathlib import Path # this is similar to os.path -- allows us to access files
from string import Template # string Template allows you to substitute variables inside of texts

import requests
from pprint import pprint
from bs4 import BeautifulSoup
res = requests.get('https://forecast.weather.gov/MapClick.php?lat=25.75622500000003&lon=-80.20751499999994#.X3X572dKhTY')
print(res)
soup = BeautifulSoup(res.text, 'html.parser') # parse into html or xml
html_body = []
conditions = soup.find(id='current_conditions_detail').find_all('td')
def print_weather(conditions):
    for condition in conditions:
        if conditions.index(condition) % 2 == 0:
            condition = condition.find('b')
            print(f'<h3>{condition.decode_contents()}</h3>')
            html_body.append(str(f'<h3>{condition.decode_contents()}</h3>'))
        else:
            print(f'<p>    {condition.decode_contents()}<p>')
            html_body.append(str(f'<p>    {condition.decode_contents()}<p>'))
print_weather(conditions)
print(html_body)
separator= ', '
new_html_body = separator.join(html_body)
print(new_html_body)
# html_str = """
# <body>
#     <h1> Hello world! </h1>
# </body>
# """
Html_file= open('index.html', 'w')
Html_file.write('<html><body>' + new_html_body + '</body></html>') 
Html_file.close()



# html = Path('index.html').read_text()

html = Template(Path('index.html').read_text())

email = EmailMessage() # this is our email object

email['from'] = 'Cordawg'
email['to'] = 'cory.send.it@gmail.com, mariospizzaworld@gmail.com'
email['subject'] = 'Better update this subject line'

email.set_content(html.substitute({'name': 'Cordawg'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('cory.send.it@gmail.com', 'bonfrerebehavior')
    smtp.send_message(email)
    print('this email is sent')