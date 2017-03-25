from sklearn.neighbors import KNeighborsClassifier as kn
import pandas as pd
train=pd.read_csv("dataset/income_training_shelf.csv")
test=pd.read_csv("dataset/income_test_shelf.csv")
training= train.ix[:,1:12]
target=train.ix[:,-1]
trn_list=[]
trg_list=[]
for x in range(0,len(training)):
    rowin=training.iloc[x]
    rowout=[]
    for i in range(0,len(rowin)):
        rowout.append(rowin.iloc[i])
    if "?" not in target.iloc[x] and  "?" not in rowout:
        trn_list.append(rowout)
        trg_list.append(target.iloc[x])



test= train.ix[:,1:12]
actual=train.ix[:,-1]
test_list=[]
act_list=[]
for x in range(0,len(test)):
    rowin=test.iloc[x]
    rowout=[]
    for i in range(0,len(rowin)):
        rowout.append(rowin.iloc[i])
    if "?" not in test.iloc[x] and "?" not in rowout:
        test_list.append(rowout)
        act_list.append(actual.iloc[x])
