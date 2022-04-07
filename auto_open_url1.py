from cgi import test
from apscheduler.schedulers.blocking import BlockingScheduler
import time


scheduler=BlockingScheduler()
def app1job():
    print('hi')
    print(time.asctime(time.localtime(time.time())))
scheduler.add_job(app1job, 'interval',seconds=5, jitter=5)
scheduler.start()
