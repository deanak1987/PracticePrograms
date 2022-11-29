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


# Used for determining age index
def agegroup_to_index(age):
    if age == "0-15":
        return 1
    elif age == "16-34":
        return 2
    elif age == "35-49":
        return 3
    elif age == "50+":
        return 4
    else:
        return 0


# Used for departure test
def depart_to_index(loc):
    if loc == 'Q':
        return 0
    elif loc == 'S':
        return 1
    else:
        return 2


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


drop_list = ['Cabin','Cabin Level','Age','SexPlural','SibSp','Parch','Name','Ticket','Fare']
df_train = pd.read_csv('titanic/train.csv')
df_test = pd.read_csv('titanic/test.csv')
df_gender = pd.read_csv('titanic/gender_submission.csv')
print(df_gender)
df_train = df_train.rename(columns={'Pclass': 'Class'})
df_test = df_test.rename(columns={'Pclass': 'Class'})
df_train['Survived'] = df_train['Survived'].agg(lambda x: 'survived' if x == 1 else 'deceased')
df_train['Age Range'] = df_train['Age'].agg(lambda x: age_to_agegroup(x))
print(df_train['Age Range'])
df_train['Embarked'].fillna(df_train['Embarked'].mode()[0], inplace=True)
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
df_prediction = df_train.drop(drop_list,axis=1)
df_prediction['Age Range'] = df_prediction['Age Range'].agg(lambda x: agegroup_to_index(x))
df_prediction['Embarked'] = df_prediction['Embarked'].agg(lambda x: depart_to_index(x))
df_prediction['Survived'] = df_prediction['Survived'].agg(lambda x: 1 if x == 'survived' else 0)
df_prediction['Sex'] = df_prediction['Sex'].agg(lambda x: 1 if x == 'male' else 0)
df_prediction['Has Family Onboard'] = df_prediction['Has Family Onboard'].agg(lambda x: 1 if x == 'Yes' else 0)
print(df_prediction.head())

from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree
from xgboost import XGBClassifier


modelA = make_pipeline(StandardScaler(), LogisticRegression())
modelB = make_pipeline(StandardScaler(), SVC())
modelC = MultinomialNB()
modelD = make_pipeline(StandardScaler(), tree.DecisionTreeClassifier())
modelE = make_pipeline(StandardScaler(), XGBClassifier())
X_train = df_prediction.drop('Survived', axis=1)
Y_train = df_prediction[['Survived']]
modelA.fit(X_train, Y_train)
modelB.fit(X_train, Y_train)
modelC.fit(X_train, Y_train)
modelD.fit(X_train, Y_train)
modelE.fit(X_train, Y_train)


df_test = df_test.rename(columns={'Pclass': 'Class'})
df_test['Age Range'] = df_test['Age'].agg(lambda x: age_to_agegroup(x))
df_test['Embarked'].fillna(df_test['Embarked'].mode()[0],inplace=True)
df_test['Cabin Level'] = df_test['Cabin'].fillna('Z').agg(lambda x: C_level(x))
df_test['SexPlural'] = df_test['Sex'].agg(lambda x: 'Men' if x == 'male' else 'Women')
df_test['Has Family Onboard'] = df_test['SibSp'] + df_test['Parch']
df_test['Has Family Onboard'] = df_test['Has Family Onboard'].agg(lambda x: 'Yes' if x != 0 else 'None')
X_test = df_test.drop(drop_list, axis=1)
X_test['Sex'] = X_test['Sex'].agg(lambda x: 1 if x == 'male' else 0)
X_test['Age Range'] = X_test['Age Range'].agg(lambda x: agegroup_to_index(x))
X_test['Embarked'] = X_test['Embarked'].agg(lambda x: depart_to_index(x))
X_test['Has Family Onboard'] = X_test['Has Family Onboard'].agg(lambda x: 1 if x == 'Yes' else 0)
# print(X_test.head())
df_ensemble = pd.DataFrame()
df_ensemble['logisticReg'] = modelA.predict(X_test)
# df_ensemble['SVC'] = modelB.predict(X_test)
# df_ensemble['NBayes'] = modelC.predict(X_test)
# df_ensemble['Dtree'] = modelD.predict(X_test)
# df_ensemble['XGBoost'] = modelE.predict(X_test)
df_ensemble['avg'] = df_ensemble.sum(axis=1) / df_ensemble.count(axis='columns')
print(df_ensemble)
df_ensemble.to_csv('ensemble.csv')
df_my_prediction = pd.DataFrame()
df_my_prediction['PassengerId'] = df_test['PassengerId']
df_my_prediction['Survived'] = df_ensemble.avg.agg(lambda x: 1 if x >= 0.5 else 0)
df_my_prediction.to_csv('submission.csv',index=False)
print(df_my_prediction)
