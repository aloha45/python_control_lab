import smtplib
from email.message import EmailMessage
from pathlib import Path # this is similar to os.path -- allows us to access files
from string import Template # string Template allows you to substitute variables inside of texts

# html = Path('index.html').read_text()

html = Template(Path('index.html').read_text())

email = EmailMessage() # this is our email object

email['from'] = 'Cordawg'
email['to'] = 'cory.send.it@gmail.com'
email['subject'] = 'Better update this subject line'

email.set_content(html.substitute({'name': 'Cordawg'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('cory.send.it@gmail.com', 'bonfrerebehavior')
    smtp.send_message(email)
    print('this email is sent')