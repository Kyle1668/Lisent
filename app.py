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

    print("Log: Rendered HTML")
    return render_template("about.html")


@app.route("/api/")
def api():
    """[Handles API requests and returns results.]

    Returns:
        [flask.Response] -- [JSON results from the sentiment analyzer.]
    """

    input_text = request.args.get("text")

    if input_text is None:
        response = {
            "code": 400,
            "error": True,
            "errorMessage": "Empty Argument",
            "results": {}
        }
        print(response)
        return jsonify(response)
    else:
        input_text = input_text.replace("\"", "")
        response = {
            "code": 200,
            "error": False,
            "results": analyzer.sentiment_analyzer(input_text)
        }
        print(response)
        return jsonify(response)


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
