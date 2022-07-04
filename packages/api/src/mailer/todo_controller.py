from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
from mail_controller import send_mail
import os
from dotenv import load_dotenv
from bson.json_util import loads, dumps

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
current_db = client["notes-mailer"]
current_col = current_db["to-dos"]

# implement filtering for current day
# implement html template for 
def get_all_todos():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Today's To-Do's"
    html_start = """\
    <html>
    <head></head>
    <body>
    <h3>Tasks:</h3>
    <ul>
    """

    html_end = """\
    </ul>
    </body>
    </html>
    """
    mail_body = []
    data = current_col.find()
    if data is not None:
        data = loads(dumps(data))
        for i in range(len(data)):
            html_start = html_start + ("<li>" + data[i]["todo"] + "</li>" + "\n")
        part = MIMEText(html_start+html_end, 'html')
        msg.attach(part)
        send_mail(msg)

get_all_todos()