from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/helloworld", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello World!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

