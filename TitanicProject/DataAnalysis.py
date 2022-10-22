import matplotlib.pyplot as plt
import pandas as pd

def age_to_agegroup(age):
    if age < 25:
        return "0-24"
    elif age < 35:
        return "25-34"
    elif age < 50:
        return "35-49"
    else:
        return "50-100"

df_train = pd.read_csv('titanic/train.csv')

# print(df_train)
print('Males: ' + str(df_train['Sex'].value_counts()['male']))
print('Females: ' + str(df_train['Sex'].value_counts()['female']))
df_train['status'] = df_train['Survived'].agg(lambda x: 'survived' if x == 1 else 'deceased')
df_train['sex2'] = df_train['Sex'].agg(lambda x: 'Men' if x == 'male' else 'Women')
df_train['age_range'] = df_train['Age'].agg(lambda x: age_to_agegroup(x))
print(df_train.head())
gensurv = df_train.groupby(['sex2'])['status'].value_counts()
print(gensurv.head())
genclasssurv = df_train.groupby(['Pclass','sex2'])['status'].value_counts().unstack(['Pclass']).fillna(0)
ageclasssurv = df_train.groupby(['age_range','sex2'])['status'].value_counts().unstack(['age_range']).fillna(0)
print(genclasssurv)
print(ageclasssurv)

# plt.figure(layout='constrained')
fig, ax = plt.subplots(1,2)
plt.subplots_adjust(top = 0.9, bottom = 0.1, hspace = 0.6)
genclasssurv.plot(ax=ax[0], kind='bar', stacked=True)
ax[0].set_xlabel('Passengers')
ax[0].set_ylabel('Count')
ax[0].set_title('Men\'s and Women\'s \n Casualties Per Class')
ax[0].grid(axis='y')
ageclasssurv.plot(ax=ax[1], kind='bar', stacked=True)
ax[1].set_xlabel('Passengers')
ax[1].set_ylabel('Count')
ax[1].set_title('Men\'s and Women\'s \n Casualties Per Age Range')
ax[1].grid(axis='y')



# plt.subplots_adjust(left=0.1, right=0.9, bottom=0.4, top=0.9)
plt.tight_layout()
plt.show()
