from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hola desde Flask en Docker y Jenkins!, Despues del commit final V1"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
