"""
Skeleton code for random forest

TMR hackathon team 2
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

#Reading the data
employee_data = pd.read_csv('HackathonMockDataDraft.csv')


#Cleaning non-predictive attributes
employee_data.drop(['Employee ID'], axis=1)
#print(employee_data.head())

#Digitizing the data with one hot encoding
one_hot_data = pd.get_dummies(employee_data[['Role','Hourly/Salary','Badges', 'Visited page']],drop_first=True)
#print(one_hot_data.head())

frames = [one_hot_data, employee_data[['# of Badges','Yeats at Company']]]
final_df = pd.concat(frames, axis=1)
#print(final_df.head())


#Creating X and y
X = final_df.drop('Recommended page', axis=1)
y = final_df['Recommended page']

#Creating training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=11)


#Making an object for RFC
rfc = RandomForestClassifier(n_estimators=100,criterion="entropy",max_features="sqrt")

#Fitting the model
rfc.fit(X_train, y_train.values.ravel())

#Predicting on test set
rfc_pred = rfc.predict(X_test)

#Printing the confusion matrix
print(confusion_matrix(y_test,rfc_pred))

#Printing the classification report
print(classification_report(y_test,rfc_pred))

#Printing the accuracy score
print(accuracy_score(y_test,rfc_pred))


