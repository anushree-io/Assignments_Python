import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

def main():
    
    sns.scatterplot(
        data=df,
        x= "StudyHours",
        y= "PreviousScore",
        hue="FinalResult",           # tells Seaborn to group the points by pass/fail.
        palette={0:"red",1:"green"}, #assigns red for failures and green for passes 
        legend='brief')              # A legend will be drawn automatically showing which colour corresponds to each class.
    
    plt.title("ScatterPlot of StudyHours vs PreviousScore")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    
    plt.show()

if __name__ == "__main__":
    main()

