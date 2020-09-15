from datetime import datetime, timedelta
import pco as p
import pco_config as pco

today = datetime.today()
bday_before_weekend = {}
bday_scheduled = {}

# variable storing next "Elevate" service time
next_elevate_plan = p.get_next_plan(pco.service_ids['Elevate'])

# need to add a check for if the users 2nd next plan is before birthday too. probably better solution than timedelta
def bday_priority(name, birthday, next_user_plan):
    if today < birthday and birthday < next_elevate_plan:
        bday_before_weekend.update({name: birthday})
    if next_user_plan == next_elevate_plan:
        if today < birthday and next_user_plan < birthday:
            sevendays = timedelta(days=7)
            week_plus_1 = next_user_plan + sevendays
            if birthday < week_plus_1:
                bday_scheduled.update({name: birthday})


def body_builder_catch(dict_of_bdays):
    bday_catch = []
    for name, bday in dict_of_bdays.items():
        birthday = datetime.strftime(bday, '%B %d')
        bday_catch.append(f"Reminder: {name}'s birthday is {birthday}\n")
    bday_str = "".join(bday_catch)
    return bday_str


def body_builder_sched(dict_of_bdays):
    bday_catch = []
    for name, bday in dict_of_bdays.items():
        birthday = datetime.strftime(bday, '%B %d')
        bday_catch.append(
            f"{name} is scheduled this week and it's the last time before their birthday on {birthday}\n")
    bday_str = "".join(bday_catch)
    return bday_str
