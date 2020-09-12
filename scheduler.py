from datetime import datetime


def schedule_check(day_of_week):
    if datetime.weekday(datetime.now()) == day_of_week:
        return True
    else:
        return False
