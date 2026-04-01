import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

def main():

# show how assignment completion relates to pass/fail
    # a countplot lets us see the number of students in each assignments-completed bucket
    sns.countplot(
        data=df, 
        x="AssignmentsCompleted",
        hue="FinalResult", 
        palette={0: "red", 1: "green"}
        )
    
    plt.title("Assignments Completed vs Final Result")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Number of Students")
    plt.legend(title="Final Result", labels=["Fail", "Pass"])
    
    plt.show()

if __name__ == "__main__":
    main()

