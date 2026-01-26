import pandas as pd

'''
DataFrame New Column Insertion Example
'''

data = {
    "Customer_ID": [1, 2, 3, 4],
    "Age": [24, 45, 31, 28]
}

df = pd.DataFrame(data)

df.insert(2, "Age_Group", ["<25" if x < 25 else "25-35" if 25 <= x <= 36 else "36+" for x in df["Age"]] )
print(df)