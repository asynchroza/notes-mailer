from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
from mail_controller import send_mail
import os
from dotenv import load_dotenv
from bson.json_util import loads, dumps
import datetime

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
current_db = client["notes-mailer"]
current_col = current_db["to-dos"]

# implement filtering for current day
# implement html template for 
def delete_old_todos(day_today):
    day_today = datetime.datetime.combine(day_today, datetime.time())

    data = list(current_col.find())

    for todo in data:
        if datetime.datetime.strptime(todo['date'], '%Y-%m-%d') < day_today:
            current_col.delete_one(todo)

def send_current_todos():
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

    date = datetime.date.today()
    print("Date today is: " + str(date))
    data = list(current_col.find({"date":str(date)}))
    print(data)

    if data is not None:
        data = loads(dumps(data))
        for i in range(len(data)):
            html_start = html_start + ("<li>" + data[i]["todo"] + "</li>" + "\n")
        part = MIMEText(html_start+html_end, 'html')
        msg.attach(part)
        send_mail(msg)
    
    delete_old_todos(datetime.date.today()) # delete old notes (-1 day) after sending current ones
