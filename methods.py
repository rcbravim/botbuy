import os
import smtplib
import email.message
import deploy
import time

def send_email(dest, subject, message):
    
    # Server Config / Connect
    server = smtplib.SMTP(deploy.EMAIL_SENDER_HOST)
    server.starttls()
    server.login(deploy.EMAIL_SENDER_LOGIN, deploy.EMAIL_SENDER_PASS)

    # Message Constructor
    message_content = message
    
    # Message Config
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = 'BOT BUYER'
    tolist = dest
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(message_content)

    # Sending Message
    server.sendmail(msg['From'], tolist, msg.as_string().encode('utf-8'))
    
    # Close Connection
    server.quit()

def shutdown(wait=1):
    try:
        time.sleep(wait)
        return False
    except KeyboardInterrupt:
        return True

# Testing...
#team = ['raphael.bravim@gmail.com', 'ricalves1131@gmail.com']
#send_email(team, 'assunto: teste', 'apenas um teste e tal...')