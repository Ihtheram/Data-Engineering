import pandas as pd

# From the dataset, filter all rows where City is "NY" and Discount_Applied is "Yes".

data = {
    "Customer_ID": [1, 2, 3, 4],
    "Age": [24, 45, 31, 28],
    "Gender": ["Male", "Female", "Male", "Female"],
    "Purchase_Amount_USD": [253, 364, 540, 120],
    "Discount_Applied": ["Yes", "No", "Yes", "No"],
    "City": ["NY", "SF", "NY", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

print("\nFiltering all rows where City is 'NY' and Discount_Applied is 'Yes'\n")
df = df[(df["City"]=="NY") & (df["Discount_Applied"]=="Yes") ]
print(df)