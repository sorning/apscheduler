from sched import scheduler
from apscheduler.schedulers.background import BackgroundScheduler
import webbrowser
import time

scheduler=BackgroundScheduler()

def auto_open_url():
    webbrowser.open('https://soft.sorning.com')
    print(time.asctime(time.localtime(time.time())))
def auto():
    webbrowser.open('https://willingwoods.com')
    print(time.asctime(time.localtime(time.time())))

scheduler.add_job(auto_open_url, trigger='interval', id='3', hours=5, jitter=60*60)
scheduler.add_job(auto, 'interval', hours=3, jitter=60*60)
scheduler.start()

try:
    while True:
        time.sleep(2)
except(KeyboardInterrupt,SystemExit):
    scheduler.shutdown()
