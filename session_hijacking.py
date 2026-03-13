# now we are going to learn sending an email with python
import os 
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
     # IN Here we are going to loign to our mail server with smtp.login
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # now we are going to send a message to our target using the email format as you all know how it 
    subject = 'Grab dinner together'
    body = ''
    msg = f'SUbject: {subject}'



