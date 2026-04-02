from sklearn.model_selection import train_test_split
from sklearn.linear_model  import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

def DataPreprocessing():

    df = pd.read_csv("Advertising.csv")
    print(df.head())

    df = df.drop('Unnamed: 0', axis= 1)
    print("Dataset after removing Unnamed column:")
    print(df.head())

    print("Missing values in dataset:", df.isnull().sum())

    return df

def SplitData(df):
    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of independent variables:", X.shape)
    print("Shape of dependent variables:", Y.shape)


    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Shape of X_train:", X_train.shape)
    print("Shape of X_test:", X_test.shape)
    print("Shape of Y_train:", Y_train.shape)
    print("Shape of Y_test:", Y_test.shape)

    return X_train,X_test,Y_train,Y_test

def TrainData(X_train,Y_train):

    model = LinearRegression()

    model.fit(X_train,Y_train)

    return model

def PredictData(model,X_test):

    Y_pred = model.predict(X_test)
    print("Predicted values are:", Y_pred)

def EvaluateData(model,X_test,Y_test):

    Y_pred = model.predict(X_test)
    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error : ",MSE)
    print("Root Mean Squared Error : ",RMSE)
    print("R Squar value : ",R2)

    print("Coefficient:", model.coef_)
    print("Intercept:", model.intercept_)

    print("Comparing the actual and predicted values")
    Result = pd.DataFrame({
        'Actual sale' : Y_test.values, 
        'Predicted sale' : Y_pred
        })
    
    print(Result.head())
   
def main():
    df = DataPreprocessing()
    X_train, X_test, Y_train, Y_test = SplitData(df)  
    model = TrainData(X_train, Y_train)
    PredictData(model, X_test)
    EvaluateData(model, X_test, Y_test)

if __name__ == "__main__":
    main()
