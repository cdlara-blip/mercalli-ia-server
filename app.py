from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB

@app.route('/')
def home():
    return "Servidor Mercalli activo"

# Endpoint principal para análisis de archivos (Mercalli)
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No se envió archivo"}), 400

    file = request.files['file']
    filename = file.filename

    # Crear carpeta 'uploads' si no existe
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    # Guardar archivo
    file.save(os.path.join("uploads", filename))

    # Simulación de análisis
    return jsonify({
        "mercalli_estimado": "VI",
        "descripcion": "Daños leves a moderados en estructuras",
        "confianza": 0.82
    })

# Endpoint de prueba para mensajes simples (Kodular)
@app.route('/mensaje', methods=['POST'])
def recibir_mensaje():
    data = request.json
    texto = data.get("texto", "")
    return jsonify({
        "status": "recibido",
        "respuesta": f"Tu mensaje fue: {texto}"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

