# import necessary packages
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.style.use('fivethirtyeight')


# def cost_func(x, c):
#     sum = 0
#     for i in range(len(x)):
#         min = math.inf
#         for j in range(len(c)):
#             temp = math.dist(x[i], c[j])**2
#             if temp <= min:
#                 min = temp
#         sum += min
#     return sum
#
#
# data = np.loadtxt('data.txt', dtype='float')
# c1 = np.loadtxt('c1.txt', dtype='float')
# c2 = np.loadtxt('c2.txt', dtype='float')
#
# MAX_ITER = 25
# k = 10
# # for i in range(MAX_ITER):
# c = [c1, c2]
# label = ['C1: Random', 'C2: kmeans++']
# for h in range(len(c)):
#     cc = c[h]
#     cost_c = []
#     cost_c.append(cost_func(data, cc))
#     for i in range(MAX_ITER):
#         clust_loc = []
#         for j in range(len(data)):
#             dist = math.inf
#             temp_cluster = 0
#             for m in range(k):
#                 temp = math.dist(data[j], cc[m])
#                 if temp <= dist:
#                     dist = temp
#                     temp_cluster = m
#             clust_loc.append(temp_cluster)
#         cluster = [[],[],[],[],[],[],[],[],[],[]]
#         for j in range(len(clust_loc)):
#             cluster[clust_loc[j]].append(data[j])
#         cluster = np.array(cluster)
#         cc = []
#         for j in range(len(cluster)):
#             cc.append(np.mean(cluster[j], axis=0))
#         cc = np.array(cc)
#         cost_c.append(cost_func(data, cc))
#     plt.plot(cost_c)
# plt.xlabel('Relation')
# plt.ylabel('Cost')
# plt.legend(label)
# plt.tight_layout()
# plt.show()

import pyspark
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf
# # create the session
# conf = SparkConf().set("spark.ui.port", "4050")
#
# # create the context
# sc = pyspark.SparkContext(conf=conf)
# spark = SparkSession.builder.getOrCreate()
#
# training = spark.read.format("libsvm").load("mnist-digits-train.txt")
# test = spark.read.format("libsvm").load("mnist-digits-test.txt")
#
# # Cache data for multiple uses
# print(training.cache())
# print(test.cache())
#
# print(training.show(truncate=False))
#
# print(training.printSchema())
#
# print(test.printSchema())
#
# print(training.count())
#
# from pyspark.ml.classification import DecisionTreeClassifier
#
# # Train a DecisionTree model.
# dt = DecisionTreeClassifier(labelCol="label", featuresCol="features")
# # Train model.
# model = dt.fit(training)
# # Make predictions.
# predictions = model.transform(test)
# # Select example rows to display.
# predictions.select("prediction", "label", "features").show(10)

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext
import pandas as pd

# create the Spark Session
spark = SparkSession.builder.getOrCreate()

# create the Spark Context
sc = spark.sparkContext

data = sc.textFile('./data.txt')
c1 = sc.textFile('./c1.txt')
c2 = sc.textFile('./c2.txt')



MAX_ITER = 25
k = 10

