# starter/backend/movies/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask.views import MethodView
from movies.resources import Movies


app = Flask(__name__)
CORS(app)


class MoviesAPI(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            return jsonify(movies=Movies)
        else:
            return jsonify(movie=Movies[int(movie_id)])


app.add_url_rule('/movies', view_func=MoviesAPI.as_view('movies'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
