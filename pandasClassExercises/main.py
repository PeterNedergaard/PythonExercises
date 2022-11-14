import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', None)

data = pd.read_csv("titanic_train.csv")
df_data = pd.DataFrame(data)


def reformat_name(name):
    first_name = name.split(",")[1].split(".")[1].split(" ")[1]
    last_name = name.split(", ")[0]

    return first_name + " " + last_name


def embarked_fullname(col):
    if col is None:
        return
    if col == "C":
        return "Cherbourg"
    if col == "Q":
        return "Queenstown"
    if col == "S":
        return "Southampton"


df_data_newId = df_data.set_index("PassengerId")

df_data_fare = df_data.sort_values("Fare")

df_data['Name'] = df_data['Name'].apply(reformat_name)

df_data_ticket = df_data[df_data['Ticket'].isin(["350406", "248706", "382652", "244373", "345763", "2649", "239865"])]

df_data = df_data.dropna(axis=0, subset=['Age'])
df_data['Age'].astype(int)
df_data_kids = df_data[df_data['Age'] <= 18]

df_data_cabin = df_data.dropna(axis=0, subset=['Cabin'])

df_data['Embarked'] = df_data['Embarked'].apply(embarked_fullname)

df_data['Relations'] = df_data['SibSp'] + df_data['Parch']

print(df_data)
