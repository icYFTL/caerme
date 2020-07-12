from flask import Flask, make_response, render_template
import requests
from bs4 import BeautifulSoup
import re
from threading import Thread
import time
import json

api = Flask(__name__)

headers = {'Access-Control-Allow-Origin': '*'}

data = dict()
data['Cáerme'] = {}

config = json.load(open('config.json', 'r'))
api.config["APPLICATION_ROOT"] = config['url_prefix']


def update(forever=False):
    while True:
        r = requests.session()
        r.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
                     'referer': 'https://ctftime.org/'}
        r.get('https://ctftime.org/')

        soup = BeautifulSoup(r.get('https://ctftime.org/stats/2020/RU?page=1').text, 'lxml')
        csrf = soup.find(attrs={"name": "csrfmiddlewaretoken"}).get('value')
        soup = BeautifulSoup(
            r.post('https://ctftime.org/team/list/', {'csrfmiddlewaretoken': csrf, 'team_name': 'Cáerme'}).text, 'lxml')
        soup.find('a', href="/stats/RU").find(text=re.compile('[0-9]+'))
        data['Cáerme'].update({'ru_rating': soup.find('a', href="/stats/RU").find(text=re.compile('[0-9]+'))})

        soup = BeautifulSoup(r.get('https://ctftime.org/stats/2020?page=1').text, 'lxml')
        csrf = soup.find(attrs={"name": "csrfmiddlewaretoken"}).get('value')
        soup = BeautifulSoup(
            r.post('https://ctftime.org/team/list/', {'csrfmiddlewaretoken': csrf, 'team_name': 'Cáerme'}).text, 'lxml')

        temp = str(soup.find('p', attrs={'align': 'left'})).replace('<p align="left">Overall rating place: <b>',
                                                                    '').strip()
        data['Cáerme'].update({'world_rating': re.sub('</b>.*</p>', '', temp)})

        soup = BeautifulSoup(r.get('https://ctftime.org/stats/2020?page=1').text, 'lxml')
        csrf = soup.find(attrs={"name": "csrfmiddlewaretoken"}).get('value')
        soup = BeautifulSoup(
            r.post('https://ctftime.org/team/list/', {'csrfmiddlewaretoken': csrf, 'team_name': 'Cáerme'}).text, 'lxml')

        temp = str(soup.find('p', attrs={'align': 'left'})).strip()
        temp = re.findall('[0-9]+\.[0-9]+', temp)
        data['Cáerme'].update({'pts': str(temp[0]).replace('.', '')})
        if not forever:
            break
        time.sleep(86400)


update()

Thread(target=update, args=(True,)).start()


@api.route('/get/rating/2020/ru/<team>', methods=['GET'])
def get_ru_rating(team):
    if team == 'Cáerme':
        resp = make_response(data['Cáerme']['ru_rating'])
        resp.headers = headers
    else:
        return 'n0n 1lipemented'

    return resp


@api.route('/get/rating/2020/<team>', methods=['GET'])
def get_rating(team):
    if team == 'Cáerme':
        resp = make_response(data['Cáerme']['world_rating'])
        resp.headers = headers
    else:
        return 'n0n 1lipemented'

    return resp


@api.route('/get/pts/2020/<team>', methods=['GET'])
def get_pts(team):
    if team == 'Cáerme':
        resp = make_response(data['Cáerme']['pts'])
        resp.headers = headers
    else:
        return 'n0n 1lipemented'

    return resp


app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')


@app.route('/', methods=['GET'])
def show():
    return render_template('index.html')


Thread(target=api.run, args=('localhost', 8012, config['debug'])).start()
app.run('localhost', 8013, config['debug'])
