import requests
import pco_config as pco
import credentials as cred
from datetime import datetime

base_url = 'https://api.planningcenteronline.com/services/v2/'
tech_team = {}
next_plans = {}
weekend_team = []


def get_user_next_plans(person_id):
    next_plans_dates = []
    response = requests.get(
        base_url + f'people/{person_id}/schedules', auth=(cred.pco_app_id, cred.pco_key)).json()
    if len(response['data']) > 0:
        for plan in response['data']:
            plan_date = datetime.strptime(
                plan['attributes']['sort_date'][0:10], '%Y-%m-%d')
            next_plans_dates.append(plan_date)
    return next_plans_dates


def get_team_members(team_id):
    response = requests.get(
        base_url + f'teams/{team_id}?include=people', auth=(cred.pco_app_id, cred.pco_key)).json()
    for person in response['included']:
        person_id = person['id']
        person_name = person['attributes']['full_name']
        # if someone hasn't set their birthday it will be saved as "None"
        person_bday = person['attributes']['birthdate']
        if person_bday != None:
            try:
                current_bday = datetime.strptime(
                    person_bday, '%Y-%m-%d').replace(year=datetime.today().year)
            except ValueError:
                leap_bday = datetime.strptime(person_bday, '%Y-%m-%d')
                current_bday = (leap_bday - timedelta(days=1)
                                ).replace(year=datetime.today().year)
            tech_team.update(
                {person_name: {'id': person_id, 'birthday': current_bday, 'next plan': get_user_next_plans(person_id)}})


def get_next_plan(service_id):
    response = requests.get(
        base_url + f'service_types/{service_id}/plans?filter=future&per_page=1', auth=(cred.pco_app_id, cred.pco_key)).json()
    if len(response['data']) > 0:
        next_plan_date = datetime.strptime(
            response['data'][0]['attributes']['sort_date'][0:10], '%Y-%m-%d')
        next_plan_id = response['data'][0]['id']
        return next_plan_date
