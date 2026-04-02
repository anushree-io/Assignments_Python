import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def MarvellousClassifier(DataPath):

    # Step 1: Get Data
    df = pd.read_csv(DataPath)
    print("Dataset:")
    print(df.head())

    # Step 2: Clean / Prepare Data
    df.dropna(inplace=True)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    # Step 3 and Step 4: Train Data and Test Data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    # Step 5: Calculate Accuracy
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of model is:", accuracy * 100)

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()