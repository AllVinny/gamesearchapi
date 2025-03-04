from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="API is working")


@app.route("/game_price", methods=["GET"])
def game_price():
    return jsonify(message="Game price")


# @app.route("/game_price/id", methods=["POST"])
# def game_price():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
