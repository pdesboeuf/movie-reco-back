from flask import Flask
from flask import jsonify
from flask_cors import CORS
from markupsafe import escape

import recommendation as rec
import rest as rst

app = Flask(__name__)
CORS(app)


@app.route('/match/id/<string:movie_id>', methods=['GET'])
def match_movie_byId(movie_id):
    # show the movie
    df_recommendation = rec.get_recommendation_by_NearestNeighbors(movie_id)
    return jsonify([rec for rec in df_recommendation.to_dict('records')])
    

@app.route('/search/id/<string:movie_id>', methods=['GET'])
def search_movie_byId(movie_id):
    # show the movie
    return rst.get_byId(movie_id)
    #return jsonify(rst.get_byId(movie_id))

@app.route('/search2/id/<string:movie_id>', methods=['GET'])
def search_movie_byId2(movie_id):
    # show the movie
    return rst.get_byId2(movie_id)
    #return jsonify(rst.get_byId(movie_id))
    

@app.route('/list/', methods=['GET'])
def get_list_movies():
    # show the movie
    df_list = rec.get_list_movies()
    return jsonify([rec for rec in df_list.to_dict('records')])

if __name__ == "__main__":
    app.run(debug=True)
    
