from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/')# default endpoint, we can update it to be different if we want
def hello_world():
    return "Hello World, from Team 2"

@app.route('/default')
def default_recommended_pages():
    return [1,2,3,4,5,6,7,8], 200 #mock return in place of ML, I used it for testing

@app.route('/recommendPages', methods=['POST'])
def recommended_pages():
    request.get_json()

    # ML code stuff

    return [1,2,3,4,5,6,7,8], 200 #mock return in place of ML 

@app.route('/addEmployee', methods=['POST'])
def add_empoloyee():
    request.get_json()
    return '', 200

@app.route('/updateUserHistory', methods=['POST'])
def update_user_history():
    #search the user and add their visited page to the database
    return '',204

app.run(port=5555, host='0.0.0.0')