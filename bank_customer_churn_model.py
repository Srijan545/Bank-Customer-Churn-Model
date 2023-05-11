# -*- coding: utf-8 -*-
"""Bank Customer Churn Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N1nrnQ-hVTheX_TMNBAdQ4FO45d76FO7
"""

#Bank Churn Model Using Ml

# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import Data
df=pd.read_csv('https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Bank%20Churn%20Modelling.csv')

#Analyse Data
df.head()

df.info()

df.describe()

df.duplicated('CustomerId').sum()

df=df.set_index('CustomerId')

df.info()

df.isnull().sum()

# Encoding
df['Geography'].value_counts()

df.replace({'Geography':{'France':2,'Germany':1,'Spain':0}},inplace=True)

df['Gender'].value_counts()

df.replace({'Gender':{'Male':0,'Female':1}},inplace=True)

df['Num Of Products'].value_counts()

df.replace({'Num Of Products':{1:0,2:1,3:1,4:1}},inplace=True)

df['Has Credit Card'].value_counts()

df['Is Active Member'].value_counts()

df.loc[(df['Balance']==0),'Churn'].value_counts()

df['Zero Balance']=np.where(df['Balance']>0,1,0)

df['Zero Balance'].hist()

df.groupby(['Churn','Geography']).count()

#Define Label And Features
df.columns

X=df.drop(['Surname','Churn'],axis=1)

y=df['Churn']

X.shape,y.shape

df['Churn'].value_counts()

sns.countplot(x ='Churn',data=df);

#Random Under Sampling
from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state=2529)

X_rus , y_rus = rus.fit_resample(X,y)

X_rus.shape,y_rus.shape,X.shape,y.shape

y.value_counts()

y_rus.value_counts()

y_rus.plot(kind='hist')

#Random Over Sampling
from imblearn.over_sampling import RandomOverSampler

ros=RandomOverSampler(random_state=2529)

X_ros,y_ros=ros.fit_resample(X,y)

X_ros.shape,y_ros.shape,X.shape,y.shape

y.value_counts()

y_ros.plot(kind='hist')

#Train Test Split
from sklearn.model_selection import train_test_split

#Split Orignal Data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=25)

#Split Random Under Sample Data
X_train_rus,X_test_rus,y_train_rus,y_test_rus=train_test_split(X_rus,y_rus,test_size=0.3)

#Split Random Over Sample Data

X_train_ros,X_test_ros,y_train_ros,y_test_ros=train_test_split(X_ros,y_ros,test_size=0.3)

#Standardize Features

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

#Standardize Orignal Data

X_train[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_train[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

#Standardize Orignal Data

X_test[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_test[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

#Standardize Random Under Sample Data

X_train_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_train_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']])
X_test_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_test_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

#standardize Random over Sample Data
X_train_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_train_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']])
X_test_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_test_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

X_train_rus.head()

X_train_ros.head()

X_test_ros.head()

X_test_rus.head()

#Support Vector Machine Classifier

from sklearn.svm import SVC

svc=SVC()

svc.fit(X_train,y_train)

y_pred = svc.predict(X_test)

y_pred=svc.predict(X_test)

#Model Accuracy
from sklearn.metrics import confusion_matrix,classification_report

confusion_matrix(y_test,y_pred)

print(classification_report(y_test,y_pred))

#Hyperparameter Tunning
from sklearn.model_selection import GridSearchCV

param_grid = {'C':[0.1,1,10],
              'gamma':[1,0.1,0.01],
              'kernel':['rbf'],
              'class_weight':['balanced']}

grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=2,cv=2)
grid.fit(X_train,y_train)

print(grid.best_estimator_)

grid_predictions=grid.predict(X_test)

confusion_matrix(y_test,grid_predictions)

print(classification_report(y_test,grid_predictions))

#Model with Random Under Sampling
svc_rus=SVC()

svc_rus.fit(X_train_rus,y_train_rus)

y_pred_rus=svc_rus.predict(X_test_rus)

#Model Accuracy

confusion_matrix(y_test_rus,y_pred_rus)

print(classification_report(y_test_rus,y_pred_rus))

#Hyperparameter Tunning

param_grid = {'C':[0.1,1,10],
              'gamma':[1,0.1,0.01],
              'kernel':['rbf'],
              'class_weight':['balanced']}

grid_rus = GridSearchCV(SVC(),param_grid,refit=True,verbose=2,cv=2)
grid_rus.fit(X_train_rus,y_train_rus)

print(grid_rus.best_estimator_)

grid_predictions_rus =grid_rus.predict(X_test_rus)

confusion_matrix(y_test_rus,grid_predictions_rus)

print(classification_report(y_test_rus,grid_predictions_rus))

#Model with Random Over Sampling
svc_ros=SVC()

svc_ros.fit(X_train_ros,y_train_ros)

y_pred_ros=svc_ros.predict(X_test_ros)

#Model Accuracy
confusion_matrix(y_test_ros,y_pred_ros)

print(classification_report(y_test_ros,y_pred_ros))

#Hyperparameter Tunning

#Hyperparameter Tunning

param_grid = {'C':[0.1,1,10],
              'gamma':[1,0.1,0.01],
              'kernel':['rbf'],
              'class_weight':['balanced']}

grid_ros = GridSearchCV(SVC(),param_grid,refit=True,verbose=2,cv=2)
grid_ros.fit(X_train_ros,y_train_ros)

print(grid_ros.best_estimator_)

grid_predictions_ros=grid_ros.predict(X_test_ros)

confusion_matrix(y_test_ros,grid_predictions_ros)

print(classification_report(y_test_ros,grid_predictions_ros))

#Lets Compare

print(classification_report(y_test,y_pred))

print(classification_report(y_test,grid_predictions))

print(classification_report(y_test_rus,y_pred_rus))

print(classification_report(y_test_rus,grid_predictions_rus))

print(classification_report(y_test_ros,y_pred_ros))

print(classification_report(y_test_ros,grid_predictions_ros))