from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split # 75% train 25% test
from sklearn.tree import DecisionTreeClassifier
irds = load_iris()
# print(irds.data)
xtrain, xtest, ytrain, ytest = train_test_split(irds.data, irds.target, random_state=0)
print(ytest)

#mo hinh cay quyet dinh
model = DecisionTreeClassifier()
train_model = model.fit(xtrain,ytrain)
print(model.predict(xtest))
print(model.score(xtest,ytest))