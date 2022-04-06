import imp
from apscheduler.schedulers.blocking import BlockingScheduler
import webbrowser

scheduler=BlockingScheduler()

def auto_open_url():
    webbrowser.open('https://willingwoods.com')

scheduler.add_job(auto_open_url,'interval',seconds=5)
scheduler.start()
   