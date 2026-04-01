import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ( accuracy_score,confusion_matrix, ConfusionMatrixDisplay,classification_report)

def main():
    Border = "=" * 50

    #####################################################################
    # Step 1 : Load the Dataset
    #####################################################################
    print(Border)
    print("Step 1: Load the Dataset")
    print(Border)

    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully!")
    print("First few records from the dataset are: ")
    print(df.head())

    #####################################################################
    # Step 2 : Data Analysis
    #####################################################################
    print(Border)
    print("Step 2: Data Analysis")
    print(Border)

    print("Shape of the Dataset:")
    print(df.shape)

    print("Missing Values in the Dataset:")
    print(df.isnull().sum())

    print("Statistical Report of the Dataset:")
    print(df.describe())

    #####################################################################
    # Step 3 : Decide Independent and Dependent Variables
    #####################################################################
    print(Border)
    print("Step 3: Decide Independent and Dependent Variables")
    print(Border)

    feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"]

    X = df[feature_cols]
    Y = df["FinalResult"]

    print("X Shape:", X.shape)
    print("Y Shape: ",Y.shape)

    #####################################################################
    # Step 4 : Visualization of Dataset
    #####################################################################
    print(Border)
    print("Step 4 : Visualization of Dataset")
    print(Border)

    plt.figure(figsize=(7,5))

    plt.scatter(df['StudyHours'], df['FinalResult'])

    plt.xlabel("Study Hours")
    plt.ylabel("Final Result (0 = Fail, 1 = Pass)")
    plt.title("Study Hours vs Final Result")

    plt.grid(True)
    plt.show()

    #####################################################################
    # Step 5 : Split the Dataset for Training and Testing
    #####################################################################
    print(Border)
    print("Step 5: Split the Dataset for Training and Testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Data Splitting Done!")

    print("X shape:",X.shape)
    print("Y shape:",Y.shape)

    print("X train shape:",X_train.shape)
    print("X test shape:",X_test.shape)
    print("Y train shape:",Y_train.shape)
    print("Y test shape:",Y_test.shape)

    #####################################################################
    # Step 6 : Build the Model
    #####################################################################
    print(Border)
    print("Step 6: Build the Model")
    print(Border)

    model = DecisionTreeClassifier(criterion="gini",max_depth=3,random_state=42)

    print("Model Created Successfully")

    #####################################################################
    # Step 7 : Train the Model
    #####################################################################
    print(Border)
    print("Step 7: Train the Model")
    print(Border)

    model.fit(X_train,Y_train)
    print("Model training done!")

    #####################################################################
    # Step 8 : Evaluate the Model
    #####################################################################
    print(Border)
    print("Step 8: Evaluate the Model")
    print(Border)

    Y_pred = model.predict(X_test)
    Y_train_pred = model.predict(X_train)

    print("Model Testing Done!")
 
    print("Expected Answers:")
    print(Y_test.to_list())

    print("Predicted Answers:")
    print(Y_pred)

    #####################################################################
    # Step 9 : Evaluate the Model Performance
    #####################################################################
    print(Border)
    print("Step 9: Evaluate the Model Performance")
    print(Border)

    train_accuracy = accuracy_score(Y_train,Y_train_pred)
    print("Training accuracy of the model is:",train_accuracy * 100)

    test_accuracy = accuracy_score(Y_test,Y_pred)
    print("Testing accuracy of the model is:",train_accuracy * 100)
    
    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion Matrix:")
    print(cm)

    tn, fp, fn, tp = cm.ravel() 

    print("True Negative (TN):", tn)
    print("False Positive (FP):", fp)
    print("False Negative (FN):", fn)
    print("True Positive (TP):", tp)

    disp_cm = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp_cm.plot()
    plt.show()

    print("Classification Report")
    print(classification_report(Y_test,Y_pred))

    if train_accuracy > test_accuracy:
        print("The model may be slightly overfitting because training accuracy is higher than testing accuracy.")
    elif train_accuracy < test_accuracy:
        print("The model is generalizing well on the testing data.")
    else:
        print("The model has equal training and testing accuracy.")

    #####################################################################
    # Step 10 : Predict for new student
    #####################################################################
    print(Border)
    print("Step 10 : Predict for new student")
    print(Border)

    new_student = pd.DataFrame({
        "StudyHours": [6],
        "Attendance": [85],
        "PreviousScore": [66],
        "AssignmentsCompleted": [7],
        "SleepHours": [7]
    })

    new_student = model.predict(new_student)

    print("Prediction for new student:", new_student[0])

    if new_student[0] == 1:
        print("The student will Pass.")
    else:
        print("The student will Fail.")

if __name__ == "__main__":
    main()