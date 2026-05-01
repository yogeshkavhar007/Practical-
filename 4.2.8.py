import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)



print(data[data['Survived'] == 1] ['Sex'].value_counts())

print(data[data['Survived'] == 0] ['Sex'].value_counts())

print(data[data['Survived'] == 1]['Embarked_S'].value_counts())

print(data[data['Survived'] == 0]['Embarked_S'].value_counts())


children=data[data['Age'] < 18]
per=children['Survived'].mean()
print(per)
children['Survived'].mean()

adults=data[data['Age'] >= 18]['Survived'].mean()
print(adults)

print(data[data['Survived'] == 1] ['Age'].median())

print(data[data['Survived'] == 0] ['Age'].median())


print(data[data['Survived'] == 1] ['Fare'].median())

print(data[data['Survived']== 0]['Fare'].median())

