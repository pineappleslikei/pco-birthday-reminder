from datetime import datetime, timedelta
import pco as p
import pco_config as pco

today = datetime.today()
bday_before_weekend = {}
bday_scheduled = {}

# variable storing next "Elevate" service time
next_elevate_plan = p.get_next_plan(pco.service_ids['Elevate'])

# sorts team members into 2 categories of upcoming birthdays:
# 1) team members that have a birthday this week before the weekend/are not scheduled this weekend
# 2) team members that are scheduled for the upcoming weekend and have a birthday before they are scheduled again


def bday_priority(name, birthday, next_user_plans):
    if today <= birthday and birthday <= next_elevate_plan:
        if len(next_user_plans) > 0:
            if next_user_plans[0] != next_elevate_plan:
                bday_before_weekend.update({name: birthday})
        else:
            bday_before_weekend.update({name: birthday})
    if len(next_user_plans) > 0:
        # checks if the team member is serving the upcoming weekend
        if next_user_plans[0] == next_elevate_plan:
            try:
                if today < birthday and birthday < next_user_plans[1]:
                    bday_scheduled.update({name: birthday})
            except IndexError:
                if today < birthday and next_user_plans[0] <= birthday:
                    bday_scheduled.update({name: birthday})

# builds a text string of reminders for team members who's birthdays will happen before their next scheduled plan


def body_builder_catch(dict_of_bdays):
    bday_catch = []
    for name, bday in dict_of_bdays.items():
        birthday = datetime.strftime(bday, '%B %d')
        bday_catch.append(f"Reminder: {name}'s birthday is {birthday}\n")
    bday_str = "".join(bday_catch)
    return bday_str

# builds a text string of reminders for team members who are scheduled the next plan and will have their birthday before their next plan


def body_builder_sched(dict_of_bdays):
    bday_catch = []
    for name, bday in dict_of_bdays.items():
        birthday = datetime.strftime(bday, '%B %d')
        bday_catch.append(
            f"{name} is scheduled this week and it's the last time before their birthday on {birthday}\n")
    bday_str = "".join(bday_catch)
    return bday_str
