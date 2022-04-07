from apscheduler.schedulers.blocking import BlockingScheduler
import webbrowser
import time

scheduler=BlockingScheduler()

def auto_open_url():
    webbrowser.open('https://willingwoods.com')
    print(time.asctime(time.localtime(time.time())))

scheduler.add_job(auto_open_url,'interval',hours=5, jitter=11160)
scheduler.start()
   