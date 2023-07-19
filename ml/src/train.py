"""
Skeleton code for neural net

TMR hackathon team 2
"""

from sklearn.neural_network import MLPClassifier
from joblib import dump, load
from pandas import read_csv
import os

## input - preprocessed user browsing data
## output - serialized trained model to be sent to the decision-making service


if __name__ == '__main__':

    ## TODO: load preprocessed data here
    ## Training data
    df_train = read_csv('data/processed/train.csv', header=0)
    df_train = df_train.drop('Employee ID', axis=1)
    X_train, y_train = df_train.drop('Recommended page', axis=1), df_train['Recommended page']

    ## Testing data
    df_test = read_csv('data/processed/test.csv', header=0)
    df_test = df_test.drop('Employee ID', axis=1)
    X_test, y_test = df_test.drop('Recommended page', axis=1), df_test['Recommended page']

    ## parameters:
    ## - max iterations
    max_iter = 300
    ## - random state. basically seed for bootstrapping
    random_state = 1

    ## initialize the model
    nn = MLPClassifier(max_iter=max_iter, random_state=random_state)
    ## TODO: uncomment below once we have X and y
    nn.fit(X_train, y_train)

    ## now, dump to a file
    os.makedirs("models", exist_ok=True)
    dump(nn, 'models/trained_network.joblib')

    ## to load, use load('models/trained_network.joblib')
    nn_deserialized = load('models/trained_network.joblib')

    ## test network
    nn_deserialized.predict(X_train)
    
    ## show accuracy
    print(nn_deserialized.score(X_test, y_test))

    ## show log of probability outputs
    print(nn_deserialized.predict_log_proba(X_test))
