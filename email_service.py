# Email Service File

import email_credentials
import smtplib, ssl
from datetime import date

def email_response(message):
    port = email_credentials.port
    sender_email = email_credentials.sender_email
    sender_password = email_credentials.sender_password
    receiver_email = email_credentials.receiver_email
    
    if message == None:
        print("No insider reports for today, " + date.today().strftime("%b %d, %Y") + ".")
        return None
    else:
        # Add Header to Email
        message = "\nDAILY INSIDER SEC FILINGS REPORT" + message
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", port) as server:
            try: 
                server.starttls(context=context)
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message)
            except: 
                "Email service failed for some reason."
