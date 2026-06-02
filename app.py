import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print("ML environment ready!")

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv')

print("First 5 rows")
print(df.head())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())

print("\nStatistics")
print(df.describe())