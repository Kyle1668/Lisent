import os

import nltk
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from sentiment_analyzer import analyzer

app = Flask(__name__)


@app.route("/")
def home():
    """[Renders the welcome page]

    Returns:
        [Flask Template] -- [Welcome HTML Page]
    """

    return render_template("about.html")


@app.route("/api/")
def api():
    """[Handles API requests and returns results.]

    Returns:
        [flask.Response] -- [JSON results from the sentiment analyzer.]
    """

    input_text = request.args.get("text")

    if input_text is None:
        return jsonify(code=400, error="Empty Argument", results={})
    else:
        input_text = input_text.replace("\"", "")
        return jsonify(
            code=200,
            input=input_text,
            results=analyzer.sentiment_analyzer(input_text)
        )


def configure_app():
    """[Downloads the necessary NLTK and Textblob dependencies and determines which port to listen on.]

    Returns:
        [int] -- [The port to listen on. Will default to 5000 for local development.]
    """

    nltk.download('punkt')
    os.system("python -m textblob.download_corpora")

    port = int(os.environ.get('PORT', 5000))

    return port


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=configure_app(), debug=True)
