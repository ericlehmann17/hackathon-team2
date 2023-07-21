from flask import Flask, jsonify, request
import requests 
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
    ## TODO: from Sharepoint (injected JS) make POST request to this endpoint sending user data
    request_body = request.get_json()

    ## for now, user is hardcoded
    ## TODO: pull user data out of request_body and format into a row that the neural network can understand
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

        #Prepare recs to be sent back up to the Sharepoint
    
    # This is where the SharePoint API endpoint and access token are defined
    sharepoint_api_url = 'https://kempath.sharepoint.com/sites/KEMPATHIntranet/api/receive_recommendations'
    access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2tlbXBhdGguc2hhcmVwb2ludC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yMDNjMDM3YS04ZWU5LTQ5ODAtOTY5OC01ZWY2OTEyNzc2NTkvIiwiaWF0IjoxNjg5ODgwMDE4LCJuYmYiOjE2ODk4ODAwMTgsImV4cCI6MTY4OTg4MzkxOCwiYWlvIjoiRTJaZ1lGRHJ1bGJ4TFBEUGZIdEhaY1llWTZOSUFBPT0iLCJhcHBfZGlzcGxheW5hbWUiOiJLRU1QQVRIIFNoYXJlUG9pbnQiLCJhcHBpZCI6IjkxMTFhZTRlLWVlNzAtNGYzMC1iN2Y5LTFhNzhkMzE5OTgwOSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzIwM2MwMzdhLThlZTktNDk4MC05Njk4LTVlZjY5MTI3NzY1OS8iLCJpZHR5cCI6ImFwcCIsIm9pZCI6IjllOTBlMWQxLWY0YzMtNDA4NC05MjVlLTFkYmUzZDcxNDM2MSIsInJoIjoiMC5BYmNBZWdNOElPbU9nRW1XbUY3MmtTZDJXUU1BQUFBQUFQRVB6Z0FBQUFBQUFBQzNBQUEuIiwic2lkIjoiZDhjZmNhYTAtNjljNi00ZjUxLThkMjAtYjU0YWZiZWNlMDE5Iiwic3ViIjoiOWU5MGUxZDEtZjRjMy00MDg0LTkyNWUtMWRiZTNkNzE0MzYxIiwidGlkIjoiMjAzYzAzN2EtOGVlOS00OTgwLTk2OTgtNWVmNjkxMjc3NjU5IiwidXRpIjoiMWRKbnhRVmJaVS1TSkxxMkZOOG9BQSIsInZlciI6IjEuMCJ9.VRtuSHhjdWI_MOFhrVjBUeeardQ0oiWaiBbCdkDP6P-2i1rsZOaaJHziXATaejyrITVZKwPmFzBifoHsMO35HOKVhTE7xFKrVyRWMZO2Eg45qqZrNRw4AFWbgLn_063Fi5m27owVgCeTOTGDyNZhNB_HVcNuSqY_aF85xBizTiYylkzW1n23pSCVTBcbfXjDYLXILOnmHffx9gzp8fY0GfKdMPHsFreowwzQTefMyMmJbAyJCpdSJibxKft6T5k9UIclwmstK4NKP3vh_14cdONg7RvbNfMgVEi0JA0K9USkca7nk7hH0dEslqdtp8htsgOgdWEwEQfSLlPvXev0dQ'

    # Set up the HTTP headers containing the access token
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    # Send the recommendation data to the SharePoint API using POST request
    response = requests.post(sharepoint_api_url, json=recs, headers=headers)

    return recs, 200 #mock return in place of Sharepoint list 

@app.route('/addEmployee', methods=['POST'])
def add_empoloyee():
    request.get_json()
    return '', 200

@app.route('/updateUserHistory', methods=['POST'])
def update_user_history():
    #search the user and add their visited page to the database
    return '',204

app.run(port=5555, host='0.0.0.0')
