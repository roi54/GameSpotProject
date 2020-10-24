from flask import Flask, render_template, request
import requests

app = Flask(__name__)
GAME_OF_THE_WEEK = {"name": "Fifa-19", "rating" : 5, "opinion" :"One of my favorites! i love this game!"}

@app.route('/trending')
def trending():
    rawg_req = requests.get(f"https://rawg.io/api/games")
    if rawg_req.ok:
        rawg_req = rawg_req.json()
        return render_template('trending.html', trend_games=rawg_req["results"])
    else:
        return index()
    

@app.route('/search', methods=['POST'])
def search():
    seacrh_radio = request.form['search-radios']
    search_word = request.form['search-word'].lower()
    if " " in search_word:
            search_word = search_word.replace(" ", "-")
    if seacrh_radio == 'genre':
        rawg_req = requests.get(f"https://rawg.io/api/games/?genres={search_word}")
    else:
        rawg_req = requests.get(f"https://rawg.io/api/games/{search_word}/suggested")
    
    if rawg_req.ok:
        rawg_req = rawg_req.json()
        return render_template('search.html', APIreqcont=rawg_req["results"])
    else:
        return index()

@app.route('/')
def index():
    rawg_req = requests.get(f"https://rawg.io/api/games/{GAME_OF_THE_WEEK['name']}")
    if rawg_req.ok:
        rawg_req = rawg_req.json()
    return render_template('index.html', gotw=rawg_req, rating=GAME_OF_THE_WEEK['rating'], opinion=GAME_OF_THE_WEEK['opinion'])
    