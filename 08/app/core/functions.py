import requests


def get_my_ip():
    response = requests.get('https://jsonip.com/')
    return response.json()["ip"]
