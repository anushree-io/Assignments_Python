from matplotlib import cm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,f1_score,precision_score,recall_score

from sklearn.preprocessing import StandardScaler

# Step 1: Load the datset
def LoadData(DataPath):
    df = pd.read_csv(DataPath)
    return df

def AnalyzeData(df):

    print("First few records:")
    print( df.head(5))

    print("Check for Missing Values:")
    print( df.isnull().sum())

    print("Staistical Summary:")
    print(df.describe())

def VisualizeData(df):

    plt.figure(figsize=(8,6))
    sns.pairplot(df, hue='Outcome')
    plt.show()

def SplitData(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    return X_train,X_test,Y_train,Y_test

def StdScaler(X,Y,X_train,X_test):

    print("Shape of X:", X.shape)
    print("Shape of Y:", Y.shape)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled,X_test_scaled

def BuildModels(X_train_scaled,Y_train):

    model_lr = LogisticRegression(max_iter =50000)
    model_dt = DecisionTreeClassifier(random_state=42)
    model_knn = KNeighborsClassifier(n_neighbors=5)

    model_lr.fit(X_train_scaled,Y_train)
    model_dt.fit(X_train_scaled,Y_train)
    model_knn.fit(X_train_scaled,Y_train)

    return model_lr,model_dt,model_knn

def BuildVotingModel(X_train_scaled,Y_train):

    model_lr = LogisticRegression(max_iter =50000)
    model_dt = DecisionTreeClassifier(random_state=42)
    model_knn = KNeighborsClassifier(n_neighbors=5)

    voting_model = VotingClassifier(
        estimators=[
            ('lr', model_lr),
            ('dt', model_dt),
            ('knn', model_knn)
        ]
    )
    voting_model.fit(X_train_scaled,Y_train)
    return voting_model

def EvaluateModels(model_lr,model_dt,model_knn,X_test_scaled,Y_test):

    pred_lr = model_lr.predict(X_test_scaled)
    pred_dt = model_dt.predict(X_test_scaled)
    pred_knn = model_knn.predict(X_test_scaled)

    acc_lr = accuracy_score(Y_test,pred_lr)
    acc_dt = accuracy_score(Y_test,pred_dt)
    acc_knn = accuracy_score(Y_test,pred_knn)

    print("Indidivisual Model Accuracy : ")
    print("Logistic Regression : ",acc_lr)
    print("Decision Tree : ",acc_dt)
    print("KNN : ",acc_knn)

    print("Logistic Regression Metrics:")
    print("Precision:", precision_score(Y_test, pred_lr))
    print("Recall:", recall_score(Y_test, pred_lr))
    print("F1 Score:", f1_score(Y_test, pred_lr))

    print("Decision Tree Metrics:")
    print("Precision:", precision_score(Y_test, pred_dt))
    print("Recall:", recall_score(Y_test, pred_dt))
    print("F1 Score:", f1_score(Y_test, pred_dt))

    print("KNN Metrics:")
    print("Precision:", precision_score(Y_test, pred_knn))
    print("Recall:", recall_score(Y_test, pred_knn))
    print("F1 Score:", f1_score(Y_test, pred_knn))

    cm = confusion_matrix(Y_test, pred_lr)
    print("Confusion Matrix for Logistic Regression:")
    print(cm)

    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.show()

def SavePredictionsinCSV(predictions,filename):

    pred_df = pd.DataFrame(predictions, columns=['Predicted_Outcome', 'Actual_Outcome'])
    pred_df.to_csv(filename, index=False)
    print(f"Predictions saved to {filename}")

def main():

    DataPath = "diabetes.csv"

    df= LoadData(DataPath)

    AnalyzeData(df)
    VisualizeData(df)

    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']

    X_train,X_test,Y_train,Y_test = SplitData(X,Y)

    X_train_scaled,X_test_scaled = StdScaler(X,Y,X_train,X_test)

    model_lr,model_dt,model_knn = BuildModels(X_train_scaled,Y_train)

    EvaluateModels(model_lr,model_dt,model_knn,X_test_scaled,Y_test)

    voting_model = BuildVotingModel(X_train_scaled,Y_train)

    pred_voting = voting_model.predict(X_test_scaled)

    print("\nVoting Classifier Accuracy:")
    print(accuracy_score(Y_test, pred_voting))

    # Step 11: Save voting predictions in CSV
    predictions = list(zip(pred_voting, Y_test))
    SavePredictionsinCSV(predictions, "Voting_Predictions.csv")

if __name__ == "__main__":
    main()