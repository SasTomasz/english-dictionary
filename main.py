from flask import Flask, render_template
import requests
from app_logs.app_logger import set_base_logging

app = Flask(__name__)
logger = set_base_logging()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dictionary/v1/<word>")
def translate(word):
    try:
        r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
    except requests.exceptions.RequestException as error:
        return "There is a problem with Your internet connection. Check it and try again"

    try:
        definition = r[0]['meanings'][0]["definitions"][0]["definition"]
        return {"word": word,
                "definition": definition}
    except (KeyError, TypeError) as error:
        logger.exception("Error occurred when trying get word definition from response")
        return "Sorry we don't find Your word, try another one"


if __name__ == "__main__":
    app.run(debug=True)
