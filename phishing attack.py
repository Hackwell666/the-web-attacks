import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import subprocess
import json

def phone_attack():
    phone_attack = int(input("press 4 to launch attack"))
    if phone_attack == 4:
        os.system == 'Android 14'
        subprocess.run("")
phone_attack()
# Your details (update these!)
sender_email = "siphelelenabo969@gmail.com"
app_password = "rjuo tais qwju ntzr"  # From Google App Passwords (no spaces!)
recipient_email = "siphelelen@redalert.co.za"  # Test with your own email first
subject = "facebook.com"
body = "please click at the link below to update you facebook details http://facebook.com  🎉" # this is the body of the email for it to go through another person 

def phishing():
    for body in sender_email:
        if open(body):
            print("user.json") 

phishing()

# Build the message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, ('http://login\\facebook.com')))


# Connect and send (this replaces your line 10+)
try:
    # Use SMTP (not SMTP_SSL) on port 587
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Encrypt after connecting
        server.login(sender_email, app_password)  # Authenticate
        
        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
    
    print("✅ Email sent! Check the recipient's inbox/spam.")
    
except TimeoutError as timeout_err:
    print(f"❌ Connection timed out: {timeout_err}")
    print("Tip: Check internet/firewall; try port 587 explicitly.")
except smtplib.SMTPAuthenticationError as auth_err:
    print(f"❌ Auth failed: {auth_err}")
    print("Tip: Verify App Password—no regular password allowed!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")