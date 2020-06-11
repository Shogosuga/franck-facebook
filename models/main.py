from json import loads
import requests
import sys
import time
import datetime
from bs4 import BeautifulSoup


def parse_data(flask_req_data):
    return loads(flask_req_data.decode(encoding = 'utf-8'))


def get_bussiness_account(access_token):
    url = f"https://graph.facebook.com/v7.0/me/accounts?access_token={access_token}"
    response = requests.get(url)
    json_data = response.json()
    return json_data


def get_ig_account(access_token, page_id):
    url = f"https://graph.facebook.com/v7.0/{page_id}?fields=instagram_business_account&access_token={access_token}"
    response = requests.get(url)
    json_data = response.json()
    return json_data


def get_ig_account_media(access_token, ig_user_id):
    url = f"https://graph.facebook.com/v7.0/{ig_user_id}/media?access_token={access_token}"
    response = requests.get(url)
    json_data = response.json()
    return json_data


def get_ig_account_profile(access_token, ig_user_id):
    url = f'https://graph.facebook.com/v7.0/{ig_user_id}?fields=biography%2Cid%2Cusername%2Cprofile_picture_url%2Cname%2Cig_id&access_token={access_token}'
    response = requests.get(url)
    json_data = response.json()
    json_data['ig_user_id'] = ig_user_id
    return json_data


def process_login_data(access_token):
    bussiness_accounts_data = get_bussiness_account(access_token)
    ig_account_data = [
        get_ig_account(access_token, account.get('id')) for account in bussiness_accounts_data.get('data')
    ]

    ig_account_detail_data = [
        get_ig_account_profile(access_token, account.get('instagram_business_account').get('id')) for account in ig_account_data
    ]

    return ig_account_detail_data