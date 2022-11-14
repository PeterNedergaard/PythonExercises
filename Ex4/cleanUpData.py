import pandas as pd

url = "FOLK1A.csv"
df = pd.read_csv(url, sep=';')
df['TID'] = df['TID'].map(lambda x: x[:-2])
df.to_csv('demographic_cleaned.csv', header=False, index=False)
