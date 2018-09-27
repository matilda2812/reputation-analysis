from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server working"


@app.route('/analyse_feed',methods=['POST'])
