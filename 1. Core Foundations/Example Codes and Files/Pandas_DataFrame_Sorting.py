import pandas as pd
data = {
    "Customer_ID": [1, 2, 3, 4],
    "Purchase_Amount_USD": [253, 364, 540, 120],
    "Review_Rating": [4.2, 3.7, 4.8, 3.2]
}

df = pd.DataFrame(data)
print(df)

print("\nDataFrame Sorted by Purchase_Amount_USD in Ascending Order:")

df = df.sort_values("Review_Rating", ascending=False)
print(df)