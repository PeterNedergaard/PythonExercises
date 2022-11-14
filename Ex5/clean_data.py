import pandas as pd

# df = pd.read_csv("FOLK1Afraskilt.csv", delimiter=";")
# df['TID'] = df['TID'].map(lambda x: x[:-2])
# df.to_csv('task5A.csv')

# df = pd.read_csv("FOLK1Augift.csv", delimiter=";")
# df['TID'] = df['TID'].map(lambda x: x[:-2])
# df.to_csv('task5B.csv')

# df = pd.read_csv("FOLK1Acivilstand.csv", delimiter=";")
# df['TID'] = df['TID'].map(lambda x: x[:-2])
# df.to_csv('task5C.csv')

df = pd.read_csv("FOLK1AgiftVSugift.csv", delimiter=";")
df['TID'] = df['TID'].map(lambda x: x[:-2])
df.to_csv('task5D.csv')
