import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

def main():

    # Plot distribution of SleepHours grouped by FinalResult (0=Fail, 1=Pass)
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x="FinalResult", y="SleepHours", palette=['red', 'green'], order=[0, 1])
    sns.swarmplot(data=df, x="FinalResult", y="SleepHours", order=[0, 1], color=".25", alpha=0.8)
    plt.title("Sleep Hours by Final Result (0=Fail, 1=Pass)")
    plt.xlabel("Final Result")
    plt.ylabel("Sleep Hours")
    plt.xticks([0, 1], ["Fail", "Pass"])
    plt.tight_layout()
    plt.show()

    # Print simple summary and interpretation
    mean_sleep = df.groupby('FinalResult')['SleepHours'].mean()
    print("Average SleepHours by FinalResult:")
    print(mean_sleep)
    print("\nObservation: Although passing students may have a slightly higher average sleep, distributions overlap — sleeping more does not guarantee success. Other factors also influence FinalResult.")

if __name__ == "__main__":
    main()

