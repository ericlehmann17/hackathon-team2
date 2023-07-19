"""
Skeleton code for neural net

TMR hackathon team 2
"""

from sklearn.neural_network import MLPClassifier
from joblib import dump
import os

## input - preprocessed user browsing data
## output - serialized trained model to be sent to the decision-making service


if __name__ == '__main__':

    ## TODO: load preprocessed data here
    df = read_csv('ProcessedHackathonMockDataDraft.csv', header=0)
    df.drop('Employee ID')
    X, y = df.drop('Recommended page', axis=1), df['Recommended page']

    ## parameters:
    ## - max iterations
    max_iter = 300
    ## - random state. basically seed for bootstrapping
    random_state = 1

    ## initialize the model
    nn = MLPClassifier(max_iter=max_iter, random_state=random_state)
    ## TODO: uncomment below once we have X and y
    nn.fit(X, y)

    ## now, dump to a file
    os.makedirs("models", exist_ok=True)
    dump(nn, 'models/trained_network.joblib')

    ## to load, use load('/../models/trained_network.joblib')
