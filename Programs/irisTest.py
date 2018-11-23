# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:58:59 2018

@author: Hi
"""

from sklearn.datasets import load_iris
from sklearn import tree

iris=load_iris()
#for i in range(len(iris.target)):
#    print("Example: %d: Label: %s, Features: %s" % (i+1,iris.target_names[iris.target[i]],iris.data[i]))

flowerClassifier=tree.DecisionTreeClassifier();
flowerClassifier=flowerClassifier.fit(iris.data,iris.target)

print(iris.target_names[flowerClassifier.predict([[6.6,2.4,4.9,2.1]])]) #just try giving random values inside predict and check if the
# -results are correct   