from email.message import EmailMessage
import ssl
import smtplib

email_sender = '{my email}'
email_password = '{my password}'
email_receiver = '{my receiver}'
subject = 'My Youtube Channel'
body = """
This is just a test message
"""
email_msg = EmailMessage()
email_msg['From'] = email_sender
email_msg['To'] = email_receiver 
email_msg['subject'] = subject
email_msg.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, email_msg.as_string())
