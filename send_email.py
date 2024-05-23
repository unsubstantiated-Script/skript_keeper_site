import os
import smtplib
import ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = os.environ.get("GMAIL_ACCOUNT")

    password = os.environ.get("GMAIL_PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
        server.quit()
