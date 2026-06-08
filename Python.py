from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/styles.css')
def styles():
    return send_file('styles.css')

if __name__ == '__main__':
    print("Servidor iniciado en http://localhost:5000")
    app.run(debug=True)
