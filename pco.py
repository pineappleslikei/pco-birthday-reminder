import requests
import pco_config as pco
import credentials as cred
from datetime import datetime

base_url = 'https://api.planningcenteronline.com/services/v2/'
tech_team = {}
next_plans = {}
weekend_team = []


def get_user_next_plan(person_id):
    response = requests.get(
        base_url + f'people/{person_id}/schedules', auth=(cred.pco_app_id, cred.pco_key)).json()
    if len(response['data']) > 0:
        next_plan_date = datetime.strptime(
            response['data'][0]['attributes']['sort_date'], '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=None)
        return next_plan_date
    else:
        return None


def get_team_members(team_id):
    response = requests.get(
        base_url + f'teams/{team_id}?include=people', auth=(cred.pco_app_id, cred.pco_key)).json()
    for person in response['included']:
        person_id = person['id']
        person_name = person['attributes']['full_name']
        # if someone hasn't set their birthday it will be saved as "None"
        person_bday = person['attributes']['birthdate']
        if person_bday != None:
            current_bday = datetime.strptime(
                person_bday, '%Y-%m-%d').replace(year=datetime.today().year)
            tech_team.update(
                {person_name: {'id': person_id, 'birthday': current_bday, 'next plan': get_user_next_plan(person_id)}})


def get_next_plan(service_id):
    response = requests.get(
        base_url + f'service_types/{service_id}/plans?filter=future&per_page=1', auth=(cred.pco_app_id, cred.pco_key)).json()
    if len(response['data']) > 0:
        next_plan_date = datetime.strptime(
            response['data'][0]['attributes']['sort_date'], '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=None)
        next_plan_id = response['data'][0]['id']
        return next_plan_date
