from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Mercalli activo"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    return jsonify({
        "mercalli_estimado": "VI",
        "descripcion": "Daños leves a moderados en estructuras",
        "confianza": 0.82,
        "recibido": data
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
