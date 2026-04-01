import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

Border = "*" * 50
print(Border)
print("Dataset Loaded Successfully")
print(Border)
print("Initial Entries from Dataset:")
print(df.head(5))     
print(Border)
print("Last Entries from Dataset:")
print(df.tail(5))
print(Border)
print("Total Number of Rows and Columns:")
print(df.shape)
print(Border)
print("List of Column Names:")
print(list(df.columns))
print(Border)
print("Datatype of each Column:")
print(df.dtypes)
print(Border)
#print(df.info())



