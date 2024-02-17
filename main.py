from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dictionary/v1/<word>")
def translate(word):
    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
    definition = r[0]['meanings'][0]["definitions"][0]["definition"]
    return {"word": word,
            "definition": definition}


if __name__ == "__main__":
    app.run(debug=True)
