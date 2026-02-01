from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#Simple k-Nearest Neighbours Algorithm

#Load the Iris dataset
X, y = load_iris(return_X_y=True)

#Use 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Use the k-NN classifier to determine what species an iris is based off of 3 nearest neighbours
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("First 5 predictions:", predictions[:5])
print("Actual labels:     ", y_test[:5])

#Print the accuracy of the first 5 predictions
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
