import schedule, time
from todo_controller import send_current_todos

def schedule_pending_todo_job():
    print("Mailing TODOs job started")

    schedule.every().day.at("11:00").do(send_current_todos)

    while True:
       schedule.run_pending()
       time.sleep(1)
