import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

print("Average of Study Hours: ",df["StudyHours"].mean())
print("Average of Attendance: ",df["Attendance"].mean())
print("Maximum of Previous Score: ",df["PreviousScore"].max())
print("Minimum of Sleep Hours: ",df["SleepHours"].min())




