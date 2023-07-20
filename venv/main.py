from flask import Flask, jsonify, request
from joblib import load
from numpy import Infinity
from sklearn.neural_network import MLPClassifier
app = Flask(__name__)

## deserialized ML model
nn = load("ml/models/trained_network.joblib")

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

    ## for now, user is hardcoded
    user = [0.2,0.10344827586206896,7,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1]
    ## get prediction vector
    prediction = list(nn.predict_log_proba([user])[0])

    ## get recommendations
    recs = []
    for i in range(3):
        max = -Infinity
        max_index = None
        for j in range(len(prediction)):
            probability = prediction[j]
            if probability > max:
                max = probability
                max_index = j
        ## if no index of max, then the list is empty, so break loop
        if max_index == None:
            break
        ## add recommendation, and repeat to find others
        recs.append(max_index)
        prediction.pop(max_index)

    return recs, 200 #mock return in place of ML 

@app.route('/addEmployee', methods=['POST'])
def add_empoloyee():
    request.get_json()
    return '', 200

@app.route('/updateUserHistory', methods=['POST'])
def update_user_history():
    #search the user and add their visited page to the database
    return '',204

app.run(port=5555, host='0.0.0.0')