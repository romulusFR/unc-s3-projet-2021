"""
Projet de programmation 2021 à l'UNC : application web de vote
"""

import requests
from flask import Flask, render_template

URL = "https://simpsons-quotes-api.herokuapp.com/quotes"

app = Flask(__name__)

def get_citations():
    """Télécharge des citations des Simpsons depuis une API rest publique"""
    # TODO : modifier pour renvoyer n citations
    resp = requests.get(URL, {"count" : 2})
    if resp.status_code != 200:
        raise Exception("GET {}".format(resp.status_code))
    citations = resp.json()
    return citations

@app.route("/")
def index():
    """Racine de l'application : proposer le choix entre 2 personnages"""
    citations = get_citations()
    return render_template("index.html.jinja", citations=citations)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
