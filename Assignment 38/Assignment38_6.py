import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

def main():
    
    # Continuous values
    sns.histplot(data=df,x= "StudyHours")
    plt.title("Histogram of StudyHours")
    plt.xlabel("StudyHours (hours)")
    plt.ylabel("Frequency")
    
    
    plt.show()

if __name__ == "__main__":
    main()


