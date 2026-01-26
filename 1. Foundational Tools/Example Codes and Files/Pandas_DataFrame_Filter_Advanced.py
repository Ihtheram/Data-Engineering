import pandas as pd
data = {
    "Customer_ID": [1, 2, 3, 4],
    "Purchase_Amount_USD": [253, 400, 540, 120],
    "Review_Rating": [4.2, 3.8, 4.8, 4.0]
}

df = pd.DataFrame(data)
print(df)

print("\nFiltered customers who have a Purchase_Amount_USD greater than 300 and a Review_Rating of 4.0 or higher:")

df = df[(df["Purchase_Amount_USD"] > 300) & (df["Review_Rating"] >= 4.0)]
print(df)