from email.message import EmailMessage

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
