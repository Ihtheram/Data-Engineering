import pandas as pd

'''
DataFrame Grouping and Aggregation Example
'''

data = {
    "Customer_ID": [1, 2, 3, 4],
    "City": ["NY", "SF", "LA", "NY"],
    "Purchase_Amount_USD": [253, 364, 540, 120]
}

df = pd.DataFrame(data)

df = df.groupby("City").agg({"Purchase_Amount_USD": "mean"})
print(df)
