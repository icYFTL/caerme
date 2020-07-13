from flask import Flask, make_response, render_template
import requests
import json
from time import sleep
from datetime import datetime

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

ru_rating = 0
world_rating = 0
pts = 0


def update():
    global ru_rating, world_rating, pts
    while True:
        data = json.loads(requests.get('https://icyftl.ru/ctftime/teams/get/team/121175/id').text)
        ru_rating = data['country_place']
        world_rating = data['rating'][0][str(datetime.now().year)]['rating_place']
        pts = 0
        for x in data['rating']:
            for key in x:
                pts += int(x[key]['rating_points'])
        sleep(86400)


@app.route('/', methods=['GET'])
def show():
    global ru_rating, world_rating, pts
    resp = make_response(render_template('index.html'))

    resp.set_cookie('ru_rating', ru_rating)
    resp.set_cookie('world_rating', world_rating)
    resp.set_cookie('pts', pts)

    return resp


app.run('localhost', 8013, False)
