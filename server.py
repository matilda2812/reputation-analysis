from flask import Flask, request, jsonify
from recast_nlp import sentiment_analysis

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server working"


@app.route('/analyse_feed',methods=['POST'])
def analyse():
    data = json.loads(request.get_data())
    source = data['search_term']
    result = sentiment_analysis(source)
    return jsonify(
        status=200,
        replies=[{
        'type': 'text/json',
        'content': result
        }])
