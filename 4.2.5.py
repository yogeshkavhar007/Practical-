import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')


print(data.head())


print(data.tail())



print(data.shape)

print(data.info())



print(data.describe())

print(data.isnull().sum())


data['Age'].fillna(data['Age'].median(),inplace=True)


data['Embarked'].fillna(data['Embarked'].mode(),inplace=True)


data.drop('Cabin',axis=1,inplace=True)


data['FamilySize']=data['SibSp'] + data['Parch']






