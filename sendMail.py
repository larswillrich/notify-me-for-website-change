import smtplib, ssl
import os

def sendmail(smtp, content, url):
    port = 465  # For SSL
    smtp_server = smtp['endpoint']
    sender_email = smtp['senderEmail']
    receiver_email = smtp['receiverEmail']
    password = smtp['password']
    message = "Subject: {}\n{}\nURL: {}".format(smtp['message'], content, url)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print("sent mail")