import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

print("Total number of Students in the dataset:", df.shape[0])

# the dataset uses a 'final result' column where 1 indicates pass and 0 indicates fail
status_col = 'FinalResult'  

# alternatively, compute the two totals explicitly
passed = print("Number of students Passed:",(df[status_col] == 1).sum())
failed = print("Number of students Failed: ",(df[status_col] == 0).sum())


