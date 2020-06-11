import os
from flask import Flask, render_template, jsonify, request
from models.main import *


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login/data', methods = ['GET', 'POST'])
def login_data():
    print('login')

    return jsonify(parse_data(request.data))


@app.route('/login', methods = ['GET'])
def login():
    accounts_detail_data = process_login_data(request.args['accessToken'])
    global access_token
    access_token = request.args['accessToken']
    return render_template(
        'login.html',
        bussiness_data = accounts_detail_data
    )


@app.route('/details', methods = ['GET', 'POST'])
def details():
    return render_template('details.html')


@app.route('/dashboard')
def dashboard():
    print(access_token)
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
