from datetime import datetime, timedelta
import pco as p
import pco_config as pco

today = datetime.today()
bday_before_weekend = {}
bday_scheduled = {}

next_elevate_plan = p.get_next_plan(pco.service_ids['Elevate'])


def bday_priority(name, birthday, next_user_plan):
    if today < birthday and birthday < next_elevate_plan:
        bday_before_weekend.update({name: {'birthday': birthday}})
    if next_user_plan == next_elevate_plan:
        if today < birthday and next_user_plan < birthday:
            sevendays = timedelta(days=7)
            week_plus_1 = next_user_plan + sevendays
            if birthday < week_plus_1:
                bday_scheduled.update({name: birthday})
