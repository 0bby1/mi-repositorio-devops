from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hola desde Flask en Docker y Jenkins!, Antes de que mi partner haga commit, Cambio hecho por Lashmi Adame"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
