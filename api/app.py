from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World"


@app.route("/api/")
def api():
    input_text = request.args.get("text")

    if input_text is None:
        return jsonify(error="Empty Argument", results={})
    else:
        return jsonify(
            input=input_text.replace("\"", ""),
            result={
                "classification": None,
                "P_Pos": None,
                "P_Neg": None
            }
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
