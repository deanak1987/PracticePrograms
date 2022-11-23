# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Used for deternining age groups
def age_to_agegroup(age):
    if age < 16:
        return "0-15"
    elif age < 35:
        return "16-34"
    elif age < 50:
        return "35-49"
    elif age > 49:
        return "50+"
    else:
        return "No Data"

# Used for determining cabin level
def C_level(cabin):
    if 'A'in cabin:
        return 'A'
    elif 'B'in cabin:
        return 'B'
    elif 'C'in cabin:
        return 'C'
    elif 'D'in cabin:
        return 'D'
    elif 'E'in cabin:
        return 'E'
    elif not 'Z' in cabin:
        return 'F or G'
    else:
        return 'No Data'

df_train = pd.read_csv('titanic/train.csv')
df_test = pd.read_csv('titanic/test.csv')
df_gender = pd.read_csv('titanic/gender_submission.csv')
df_train = df_train.rename(columns={'Pclass': 'Class'})
df_test = df_test.rename(columns={'Pclass': 'Class'})
df_train['Survived'] = df_train['Survived'].agg(lambda x: 'survived' if x == 1 else 'deceased')
df_train['Age Range'] = df_train['Age'].agg(lambda x: age_to_agegroup(x))
df_train['Embarked'].fillna(df_train['Embarked'].mode()[0],inplace=True)
df_train['Cabin Level'] = df_train['Cabin'].fillna('Z').agg(lambda x: C_level(x))
df_train['SexPlural'] = df_train['Sex'].agg(lambda x: 'Men' if x == 'male' else 'Women')
gensurv = df_train.groupby(['SexPlural'])['Survived'].value_counts()
class_srv = df_train.groupby('Class')['Survived'].value_counts().unstack().fillna(0)
agesurv = df_train.groupby(['Age Range'])['Survived'].value_counts().unstack(['Age Range']).fillna(0)
cabin = df_train.groupby(['Cabin Level'])['Survived'].value_counts().unstack(['Cabin Level']).fillna(0)
df_train['Has Family Onboard'] = df_train['SibSp'] + df_train['Parch']
df_train['Has Family Onboard'] = df_train['Has Family Onboard'].agg(lambda x: 'Yes' if x != 0 else 'None')
famsurv = df_train.groupby(['Has Family Onboard'])['Survived'].value_counts().unstack('Has Family Onboard').fillna(0)
embarked = df_train.groupby(['Embarked'])['Survived'].value_counts().unstack()
embarkedclass = df_train.groupby(['Embarked'])['Class'].value_counts().unstack()
df_prediction = df_train.drop(['Cabin','Cabin Level','Age','Age Range','SexPlural','Embarked','SibSp','Parch','Name','Ticket','Fare'],axis=1)
df_prediction['Survived'] = df_prediction['Survived'].agg(lambda x: 1 if x == 'survived' else 0)
df_prediction['Sex'] = df_prediction['Sex'].agg(lambda x: 1 if x == 'male' else 0)
df_prediction['Has Family Onboard'] = df_prediction['Has Family Onboard'].agg(lambda x: 1 if x == 'Yes' else 0)
print(df_prediction.head())

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
modelA = make_pipeline(StandardScaler(), LogisticRegression())
X_train = df_prediction.drop('Survived', axis=1)
Y_train = df_prediction[['Survived']]
X_test = df_test
modelA.fit(X_train, Y_train)

df_test = df_test.rename(columns={'Pclass': 'Class'})
df_test['Age Range'] = df_test['Age'].agg(lambda x: age_to_agegroup(x))
df_test['Embarked'].fillna(df_test['Embarked'].mode()[0],inplace=True)
df_test['Cabin Level'] = df_test['Cabin'].fillna('Z').agg(lambda x: C_level(x))
df_test['SexPlural'] = df_test['Sex'].agg(lambda x: 'Men' if x == 'male' else 'Women')

