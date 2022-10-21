import matplotlib.pyplot as plt
import pandas as pd


df_train = pd.read_csv('titanic/train.csv')

# print(df_train)
print('Males: ' + str(df_train['Sex'].value_counts()['male']))
print('Females: ' + str(df_train['Sex'].value_counts()['female']))
df_train['status'] = df_train['Survived'].agg(lambda x: 'survived' if x == 1 else 'deceased')
print(df_train.head())
gensurv = df_train.groupby(['Sex'])['status'].value_counts()
print(gensurv.head())
genclasssurv = df_train.groupby(['Sex','Pclass'])['status'].value_counts()
print(genclasssurv)
genclasssurv.plot.bar()
plt.show()
