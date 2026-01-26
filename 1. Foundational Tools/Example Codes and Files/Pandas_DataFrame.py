import pandas

"""
DataFrame Example
"""

data = {
    'Product': ['Apple', 'Banana', 'Orange'],
    'Price': [1.2, 0.5, 0.8],
    'Quantity': [10, 20, 15]
}

# Creates DataFrame
dataframe = pandas.DataFrame(data)

# Displays the DataFrame
print(dataframe)
