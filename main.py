import pco as p
import pco_config as pco
import date_comp as dc

for team_id in pco.team_ids:
    p.get_team_members(team_id)

p.get_next_plan(pco.service_ids['Elevate'])

for x, y in p.tech_team.items():
    name = x
    birthday = y['birthday']
    next_plan = y['next plan']
    dc.bday_priority(name, birthday, next_plan)
