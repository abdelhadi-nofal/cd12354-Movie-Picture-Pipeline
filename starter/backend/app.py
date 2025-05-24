# starter/backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/movies')
def get_movies():
    return jsonify(movies=[
        {"id": "tt0848228", "title": "Avengers: Endgame"},
        {"id": "tt1431045", "title": "The Irishman"},
        {"id": "tt1583421", "title": "Ford v Ferrari"},
        {"id": "tt6231118", "title": "Knives Out"},
        {"id": "tt10272386", "title": "Raya and the Last Dragon"}
    ])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
