import os
from flask import Flask, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    print("=" * 40)
    print("  TiendaPython — Servidor Flask")
    print("  http://localhost:5000")
    print("=" * 40)
    app.run(debug=True, port=5000)
