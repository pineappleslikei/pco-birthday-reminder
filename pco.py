import requests
import pco_config as pco
import credentials as cred

base_url = 'https://api.planningcenteronline.com/services/v2/'
tech_team = []


def get_team_members(team_id):
    response = requests.get(
        base_url + f'teams/{team_id}?include=people', auth=(cred.pco_app_id, cred.pco_key)).json()
    for person in response['included']:
        person_id = person['id']
        person_name = person['attributes']['full_name']
        # if someone hasn't set their birthday it will be saved as "None"
        person_bday = person['attributes']['birthdate']
        tech_team.append(
            {person_name: {'id': person_id, 'birthday': person_bday}})
