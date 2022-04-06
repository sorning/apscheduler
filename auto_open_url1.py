from apscheduler.schedulers.blocking import BlockingScheduler


scheduler=BlockingScheduler()
def app1job():
    print('hi')
scheduler.add_job(app1job, 'interval',seconds=5)
scheduler.start()