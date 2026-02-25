from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Mercalli activo"

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No se envió archivo"}), 400

    file = request.files['file']
    file.save(file.filename)

    resultado = {
        "mercalli_estimado": "VI",
        "descripcion": "Daños leves a moderados en estructuras",
        "confianza": "0.82"
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run()
