import pco as p
import pco_config as pco
import date_comp as dc
import credentials as cred

for team_id in pco.team_ids:
    p.get_team_members(team_id)

p.get_next_plan(pco.service_ids['Elevate'])

for x, y in p.tech_team.items():
    name = x
    birthday = y['birthday']
    next_plans = y['next plan']
    dc.bday_priority(name, birthday, next_plans)


this_plan_bdays = dc.body_builder_sched(dc.bday_scheduled)
this_week_bdays = dc.body_builder_catch(dc.bday_before_weekend)


def body_assemble():
    if len(this_week_bdays) or len(this_plan_bdays) > 0:
        body = f'Hi {cred.receiver_name}. This is your weekly birthday notification:\n\n{this_plan_bdays}\n{this_week_bdays}\n\nHope you have an amazing day!'
    else:
        body = f'Hi {cred.receiver_name}. No birthday reminders this week :)'
    return body


body = body_assemble()
print(body)
