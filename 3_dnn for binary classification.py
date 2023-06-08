from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# Load the dataset
dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
# Separate the input features and labels
X=dataset[:,0:8]
Y=dataset[:,8]

model=Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(X,Y,epochs =150,batch_size=10)

accuracy=model.evaluate(X,Y)
print('Accuracy of model is', (accuracy*100))
prediction=model.predict(X)
for i in range(5):
    print(X[i].tolist(),prediction[i],Y[i])

# X[i].tolist(): It retrieves the input features for the i-th sample in X and converts them to a list. 
# prediction[i]: It retrieves the predicted output for the i-th sample from the prediction variable. 
# Y[i]: It retrieves the true label for the i-th sample in Y. This line prints the true label.

# The reason for converting the input features to a list is for the purpose of printing them. The print function in Python expects a list-like object or individual values as arguments. By using tolist(), the input features, which are originally stored as a NumPy array, are converted into a list representation so that they can be printed using the print function.