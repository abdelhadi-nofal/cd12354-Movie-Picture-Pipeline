# starter/backend/movies/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from movies.resources import Movies  # Absolute import

app = Flask(__name__)
CORS(app)

@app.route('/movies')
def get_movies():
    return jsonify(movies=Movies)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)