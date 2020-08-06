import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
d=float(sys.argv[4])
e=float(sys.argv[5])
f=float(sys.argv[6])
g=float(sys.argv[7])
h=float(sys.argv[8])
import pandas as pd
df = pd.read_csv("/home/bikki__maurya/Coding/VSCode/Integration/ML/diabetes.csv")
from sklearn.model_selection import train_test_split
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=7)
from sklearn.linear_model import LogisticRegression
model= LogisticRegression()
model.fit(xtrain,ytrain)#fit the model with data
y_pred=model.predict([[a,b,c,d,e,f,g,h]])
res=y_pred[0]
if(res==0):
    print("Sorry you result is negative")

else:
    print("Congrats you result is positive! Means you have diabetes")
