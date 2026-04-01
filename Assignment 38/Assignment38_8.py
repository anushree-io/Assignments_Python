import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

def main():
    
    sns.boxplot(data=df,x= "Attendance")              
    
    plt.title("BoxPlot for Attendance to Check Outliers")
    plt.xlabel("Attendance")
  
    
    plt.show()

if __name__ == "__main__":
    main()

