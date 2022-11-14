import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import seaborn as sbn
from scipy import stats

pd.set_option('mode.chained_assignment', None)

# pd.set_option('display.max_columns', None)

data = pd.read_csv("ds_salaries.csv", delimiter=",")

data_prune = data[['work_year', 'experience_level', 'salary_in_usd', 'job_title', 'company_location', 'company_size']]

onehot_exp = pd.get_dummies(data_prune['experience_level'])
# print(onehot_exp)

le = preprocessing.LabelEncoder()
data_prune['company_location'] = le.fit_transform(data_prune['company_location'])
# print(data_prune)

scaler = MinMaxScaler()
scaler.fit(data_prune[['company_location']])
scaled_data = scaler.transform(data_prune[['company_location']])
# print(scaled_data)

cut_data, bins = pd.cut(data_prune['salary_in_usd'], bins=4, labels=['low', 'medium', 'high', 'extra'], retbins=True)
data_prune['salary_cut'] = cut_data


def bin_plot(group_input):
    data_prune.groupby(['salary_cut', group_input]).size().unstack().plot(kind='bar', stacked=False)
    plt.show()


# bin_plot('experience_level')

experience = {'EN': 10, 'EX': 20, 'MI': 30, 'SE': 40}
data_prune = data_prune.replace({"experience_level": experience})

# sbn.pairplot(data_prune[['salary_in_usd', 'experience_level']])
# plt.show()

x_data = data_prune['salary_in_usd']
y_data = data_prune['experience_level']

plt.scatter(x_data, y_data)

slope, intercept, r, p, std_err = stats.linregress(x_data, y_data)


def myfunc(x):
    return slope * x + intercept


regression_line = list(map(myfunc, x_data))

plt.plot(x_data, regression_line)
plt.show()
