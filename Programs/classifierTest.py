# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn import tree

# Weight lesser than 50kg are cats represented by 0 else the animal is a dog represented by a dog
animalFeatures=[[50,1],[36,0],[87,1],[24,0]]      #HERE 0'S AND 1'S STANDS FOR THE SIZE OF THE ANIMAL \N 0= SMALL, 1= BIG
animalNames=[1,0,1,0]       

animalClf=tree.DecisionTreeClassifier()
animalClf=animalClf.fit(animalFeatures,animalNames)

while(1==1):
    wt=int(input("Enter the weight of the animal: "));
    print("\nPress:\n0: If the size of the animal is small\n1: If the size of the animal is large")
    size=int(input())
    
    if(not animalClf.predict([[wt,size]])):
        print("The animal having weight<50 and size= small is a\n","\t***** CAT *****")
    else:    
        print("The animal having weight>=50 and size= big is a\n","\t***** DOG *****")

    print("Press:\n0: To continue\nAny other no. to exit\n")
    
    if(int(input())!=0):
        print("Program terminated successfully")
        break

