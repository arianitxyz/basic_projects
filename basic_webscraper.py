import requests
from bs4 import BeautifulSoup as bs


def get_user_profile(username: str) -> str:
    # username = input('Please input GitHub user: ')

    url = 'https://github.com/' + username
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    return profile_image
