import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")

# distribution of final results (1=pass, 0=fail)
status_col = 'FinalResult'    # calls final result from dataset
counts = df[status_col].value_counts()  # counts occurences of each value in column(1s and 0s)
print("Final result counts:")
print(counts)   # diaplays counts of 1 and 0

# calculate percentages
percentages = counts / counts.sum() * 100   # converts counts to percentage of total by dividing sum of all counts and *100
df_percent = percentages.round(2)  # rounds the percentage to two decimal places
print("\nPercentages of each outcome:")
print(df_percent) 

# check if dataset is balanced
# here we consider it balanced if both classes are roughly equal (within ~5-10%)
balance_threshold = 10  # percent difference threshold
diff = abs(df_percent.get(1,0) - df_percent.get(0,0)) 

if diff <= balance_threshold:
    balance_msg = "Dataset is approximately balanced."
else:
    balance_msg = "Dataset is imbalanced."
print("\nBalance check:", balance_msg)


