import requests
import pco_config as pco
import credentials as cred

base_url = 'https://api.planningcenteronline.com/services/v2/'
tech_team = {}
next_plans = {}


def get_team_members(team_id):
    response = requests.get(
        base_url + f'teams/{team_id}?include=people', auth=(cred.pco_app_id, cred.pco_key)).json()
    for person in response['included']:
        person_id = person['id']
        person_name = person['attributes']['full_name']
        # if someone hasn't set their birthday it will be saved as "None"
        person_bday = person['attributes']['birthdate']
        tech_team.update(
            {person_name: {'id': person_id, 'birthday': person_bday}})


def get_next_plan(service_id):
    response = requests.get(
        base_url + f'service_types/{service_id}/plans?filter=future&per_page=1', auth=(cred.pco_app_id, cred.pco_key)).json()
    if len(response['data']) > 0:
        next_plan_date = response['data'][0]['attributes']['sort_date']
        next_plan_id = response['data'][0]['id']
        next_plans.update(
            {service_id: {'plan_id': next_plan_id, 'date': next_plan_date}})
