import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("placement.csv")

df=df.iloc[:,1:]
print(df.head())
plt.scatter(df["cgpa"],df["iq"],c=df["placement"])
plt.show()

# step2 sepreating inut and output cols
x=df.iloc[:,0:2]
y=df.iloc[:,2]

# step 3 train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)
# print(x_train)

# step4 scaling
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
x_train=scalar.fit_transform(x_train)
# print(x_train)
x_test=scalar.transform(x_test)


# step 5 model training 
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
clf.fit(x_train,y_train)

# step 6 checking prediction 
y_pred=clf.predict(x_test)
# print(y_test)

# step 7 calculating accuraccy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))

# step 8 plotting decision boundary 
# from mlxtend.ploting import plot_decision_regions
# print(plot_decision_regions(x_train,y_train,clf=clf,legend=2))

# step9 exporting the ml model 
import pickle
pickle.dump(clf,open("model.pkl","wb"))