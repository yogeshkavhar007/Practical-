import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']


data['IsAlone']= np.where(data['FamilySize'] > 0, 0, 1)


data['Sex']=data['Sex'].map({'male': 0, 'female': 1})



data=pd.get_dummies (data, columns=['Embarked'], drop_first=True)


print(data['Age'].mean())


print(data['Fare'].median())

print(data['Pclass'].value_counts())

print(data['Sex'].value_counts())



print(data['Survived'].value_counts())



print(data['Survived'].mean())


print(data.groupby('Sex') ['Survived'].mean())




