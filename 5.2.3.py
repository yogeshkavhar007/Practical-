import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)
# Write your code here for Bar Plot for Survival Rate

count = data.groupby('Survived').size()
plt.bar(count.index,count.values,width=0.4)

count.plot(kind='bar')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.title('Survival Count')

plt.show()
