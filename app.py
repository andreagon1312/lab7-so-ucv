import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route('/')
def home():
    try:
        visitas = r.incr('contador_visitas')
        estado_db = "Conectado"
    except Exception as e:
        visitas = 0
        estado_db = f"Error: {str(e)}"
    
    return jsonify({
        "mensaje": "Sistemas Operativos UCV - Contenerizacion Exitosa",
        "total_visitas": visitas,
        "estado_db": estado_db,
        "hostname_contenedor": os.uname()[1]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
