from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Mercalli activo"

# Mini laboratorio de prueba
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json(force=True, silent = True)
    
    if not data :
        return jsonify({"respuesta": "No se recibió mensaje"}), 400
    
    texto = data.get("mensaje")
    
    return jsonify({
        "respuesta": f"Servidor recibió: {texto}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
