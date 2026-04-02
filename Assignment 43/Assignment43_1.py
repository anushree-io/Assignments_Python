from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def DataPreprocessing():

    df = pd.read_csv("PlayPredictor.csv")
    print(df.head())
    
    encode_Whether = LabelEncoder()
    encode_Temperature = LabelEncoder()
    encode_Play = LabelEncoder()

    df['Whether'] = encode_Whether.fit_transform(df['Whether'])
    df['Temperature'] = encode_Temperature.fit_transform(df['Temperature'])
    df['Play'] = encode_Play.fit_transform(df['Play'])
    
    print("After Encoding:")
    print(df.head())

    df = df.drop('Unnamed: 0', axis= 1)
    print("Dataset after removing Unnamed column:")
    print(df.head())

    return df

def TrainData(df):

    X = df[['Whether', 'Temperature']]
    Y = df['Play']

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)

    return model

def Predict(model):

    test_x = int(input("Enter Whether (2-Sunny , 0-Overcast , 1-Rainy): "))
    test_y = int(input("Enter the Temperature (1-Hot, 2-Mild, 0-Cool): "))
    
    test_data = pd.DataFrame([[test_x,test_y]], columns=['Whether', 'Temperature'])

    prediction = model.predict(test_data)

    if prediction[0] == 1:
        print("Play")
    else:
        print("Don't Play")

def CheckAccuracy(df):

    X = df[['Whether', 'Temperature']]
    Y = df['Play']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    k = int(input("Enter the value of k:"))

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of the model is:", accuracy)

def main():
    df = DataPreprocessing()
    model = TrainData(df)
    Predict(model)
    CheckAccuracy(df)

if __name__ == "__main__":
    main()
