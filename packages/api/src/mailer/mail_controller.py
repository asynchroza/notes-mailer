import smtplib as smtp, ssl, os
from dotenv import load_dotenv


def send_mail(msg):
    load_dotenv()

    port = 465 # SSL
    email = os.getenv("MAIL_USERNAME")
    password = os.getenv("MAIL_PASSWORD")

    server = smtp.SMTP_SSL('smtp.gmail.com', port)
    server.login(email, password)
    server.sendmail(email, os.getenv("MAIL_RECEIVER"), msg.as_string())
    server.close()
