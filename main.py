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
    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
    try:
        definition = r[0]['meanings'][0]["definitions"][0]["definition"]
        return {"word": word,
                "definition": definition}
    except (KeyError, TypeError) as error:
        # TODO: Show more info in error message
        logger.error(error)
        return "Sorry we don't find Your word, try another one"


if __name__ == "__main__":
    app.run(debug=True)
