from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta principal para verificar que el servidor vive
@app.route('/')
def home():
    return "Servidor MercalliVision Activo y Listado"

# Esta es la ruta que usará Kodular (asegúrate que tu URL termine en /mensaje)
@app.route("/mensaje", methods=["POST"])
def mensaje():
    # Recibimos el JSON de Kodular
    data = request.get_json(force=True, silent=True) or {}
    
    lat = data.get("lat", "Sin GPS")
    lon = data.get("lon", "Sin GPS")
    msg = data.get("mensaje", "Sin texto")

    # Esto se verá en la pestaña 'Console' de Replit
    print(f"--- NUEVO REPORTE ---")
    print(f"📍 Coordenadas: {lat}, {lon}")
    print(f"💬 Mensaje: {msg}")

    return jsonify({
        "status": "recibido",
        "confirmacion": f"Ubicación {lat}, {lon} guardada con éxito"
    })

if __name__ == "__main__":
    # Importante: el puerto 5000 es el que Replit usa por defecto en esta vista
    app.run(host='0.0.0.0', port=5000)
