from flask import jsonify

from sentiment_analyzer import analyzer


def api(text):
    """[Handles API requests and returns results.]

    Returns:
        [flask.Response] -- [JSON results from the sentiment analyzer.]
    """

    input_text = text

    if input_text is None:
        return jsonify(error="Empty Argument", results={})
    else:
        input_text = input_text.replace("\"", "")
        return jsonify(
            input=input_text,
            results=analyzer.sentiment_analyzer(input_text)
        )


def test_app():
    assert 1 + 1 == 2
