"""
Series Example
List, Dictionary, and Single Value with Custom Indices
"""
import pandas

data = [100, 200, 300, 400]

series = pandas.Series(data)
print("\nBasic Series:")
print(series)

data2 = {'Math' : 90,
    'Science' : 85,
    'English' : 88}
    
series2 = pandas.Series(data2)
print("\nSeries with Custom Indices:")
print(series2)

data3 = 10
index = ['a', 'b', 'c', 'd']

series3 = pandas.Series(data3, index)
print("\nSeries with Single Value and Custom Indices:")
print(series3)