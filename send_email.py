import smtplib, ssl
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = "unsubstantiated.script@gmail.com"
    # Note to self. Password sits in .zshrc and awaits deployment for environment there.
    password = os.getenv("GMAIL_PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
        server.quit()
