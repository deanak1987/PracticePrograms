import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


age_classes_file='data/age_classes.txt'
# print(age_classes_file, "======================")
# with open(age_classes_file, "r") as f:
#     for i in range(20):
#         print(i, "\t", repr(f.readline()))

age_class_columns = ['code', 'age_range']
age_classes = pd.read_csv('data/age_classes.txt', sep=' ',#separated by space
                          header=None, names=age_class_columns)

# remove potential leading or trailing whitespace
age_classes['code'] = age_classes['code'].str.strip()
age_classes['age_range'] = age_classes['age_range'].str.strip()

# print(age_classes)

age_classes[['age_min', 'age_max']] = (
    age_classes['age_range']
    .str.split("-", expand=True)
    .astype('int') #pay attention that we need to specify the type for analysis
)
# print(age_classes)

age_classes['age_center'] = (age_classes['age_max'] + age_classes['age_min']) / 2.
# print(age_classes)

# type the code here to check the raw data in the txt file
residence_area_file ='data/residence_area.txt'
# print(residence_area_file, "======================")
# with open(residence_area_file, "r") as f:
#     for i in range(20):
#         print(i, "\t", repr(f.readline()))
# ...

# import the data into dataframe
# if you use a single character delimiter, it uses the faster engine ...
residence_area__column = ['code', 'area']
residence_areas = pd.read_csv('data/residence_area.txt', sep=' ',#separated by space
                              header=None, names=residence_area__column)

# remove potential leading or trailing whitespace
residence_areas['code'] = residence_areas['code'].str.strip()
residence_areas['area'] = residence_areas['area'].str.strip()

# print(residence_areas)


# type your code here (feel free to have more cells)
'''
tafeng_full ='data/TaFengTransactions.txt'
print(tafeng_full, "======================")
with open(tafeng_full, "r") as f:
    for i in range(20):
        print(i, "\t", repr(f.readline()))
'''
header_labels = ['entry_date', 'transaction_time','customer_id','age_code','residence_area','product_subclass','product_id','amount','asset','sales_price']
tafeng_transactions = pd.read_csv('data/TaFengTransactions.txt', sep=';',#separated by semicolon
                                  header=None, names=header_labels)
tafeng_transactions['residence_area'] = tafeng_transactions['residence_area'].str.strip()
tafeng_transactions = tafeng_transactions.iloc[1: , :]
...

# print(tafeng_transactions.head())

# type your code here
age_classes_rename = age_classes.rename(columns = {'code':'age_code'})
age_classes_rename['age_code'] = age_classes_rename['age_code'].str.strip()
tafeng_transactions['age_code'] = tafeng_transactions['age_code'].str.strip()
residence_areas_rename = residence_areas.rename(columns= {'code':'residence_area'})
residence_areas_rename.loc[:,'residence_area'].replace(':','')
residence_areas_rename['residence_area'] = residence_areas_rename['residence_area'].str.strip()

tafeng_full = pd.merge(tafeng_transactions, age_classes_rename, on='age_code', how='left')
# tafeng_full = pd.merge(tafeng_transactions, residence_areas_rename, on='residence_area', how='left')

...
#age_classes_rename.head()
# print(tafeng_transactions)
# print(residence_areas_rename.loc[:,'residence_area'])
# print(tafeng_transactions.loc[:,'residence_area'].isin(residence_areas_rename.loc[:,'residence_area']))
# print(tafeng_full.head())

# type your code here

time_format = "%Y-%m-%d %H:%M:%S"
tafeng_full['transaction_time'] = pd.to_datetime(tafeng_full['transaction_time'],
                                                 format = time_format)
tafeng_full.to_csv('tafeng_full.csv')

header = ['transaction_time','customer_id','num_items','total_value','num_unique']
carts = pd.DataFrame()
carts['num_items'] = tafeng_full.groupby(['transaction_time', 'customer_id'])['amount'].agg(
    lambda x: x.astype(int).sum()).to_frame(
    name='num_items')['num_items']
carts['total_value'] = tafeng_full.groupby(['transaction_time', 'customer_id'])['sales_price'].agg(
    lambda x: x.astype(int).sum()).to_frame(
    name='sales_price')['sales_price']
carts['num_unique']  = tafeng_full.groupby(['transaction_time', 'customer_id'])['product_id'].count().to_frame(
    name='num_unique')['num_unique']
carts = carts.reset_index()
# carts.to_csv('crts.csv')
# print(carts['num_items'].max())
...
carts['log_num_items'] = np.log(carts['num_items'])
carts['log_total_value'] = np.log(carts['total_value'])
# carts.plot.scatter('log_num_items','log_total_value',c='black')


# sns.lmplot(x='num_items', y='total_value', data=carts)
# plt.show()

customer_age = tafeng_full.groupby('age_range')['customer_id'].count()
customer_age = customer_age.to_frame(name='count').reset_index()
print(customer_age)
customer_age.plot.bar(x='age_range', y='count')
plt.xlabel('Age Range')
plt.ylabel('Number of Customers')
plt.title('Age Distribution of Shoppers')
plt.show()