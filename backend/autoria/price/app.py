from apscheduler.schedulers.background import BackgroundScheduler


def update_exchange_rates():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_exchange_rates, 'interval', days=1)
    scheduler.start()
