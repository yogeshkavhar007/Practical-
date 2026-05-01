import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


print(data.groupby ('Pclass') ['Survived'].mean())

print(data.groupby('Embarked_S') ['Survived'].mean())


print(data.groupby('FamilySize') ['Survived'].mean())

print(data.groupby ('IsAlone') ['Survived'].mean())


print(data.groupby ('Pclass') ['Fare'].mean())


print(data.groupby ('Pclass') ['Age'].mean())


print(data.groupby('Survived')['Age'].mean())

print(data.groupby('Survived') ['Fare'].mean())

print(data[data['Survived'] == 1] ['Pclass'].value_counts())


print(data[data['Survived']==0]['Pclass'].value_counts())








