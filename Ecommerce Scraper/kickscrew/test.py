import pandas as pd

df = pd.read_csv('products_sample.csv')
a = []
a = df['Link'].tolist()
print(a)