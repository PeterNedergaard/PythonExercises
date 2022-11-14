import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from scipy import stats
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

url = 'https://think.cs.vt.edu/corgis/datasets/csv/cars/cars.csv'

data = pd.read_csv(url)
# print(data.head())

data_df = data[(data['Fuel Information.Fuel Type'] == 'Gasoline') & (data['Identification.Make'] == 'Honda')]

for column in data_df.columns:
    if data_df[column].dtype == 'int64':
        q_hi = data_df[column].quantile(0.99)
        data_df = data_df[(data_df[column] < q_hi)]


scaler = MinMaxScaler()
scaler.fit(data_df[['Fuel Information.Highway mpg']])
mpg_norm = scaler.transform(data_df[['Fuel Information.Highway mpg']])

scaler.fit(data_df[['Engine Information.Engine Statistics.Horsepower']])
hp_norm = scaler.transform(data_df[['Engine Information.Engine Statistics.Horsepower']])


x_data = data_df['Fuel Information.Highway mpg']
y_data = data_df['Engine Information.Engine Statistics.Horsepower']

slope, intercept, r, p, std_err = stats.linregress(x_data, y_data)


def myfunc(x):
    return slope * x + intercept


regression_line = list(map(myfunc, x_data))
plt.plot(x_data, regression_line)

plt.scatter(x_data, y_data)

print("When x = 1, y = " + str(myfunc(1)))

plt.show()
