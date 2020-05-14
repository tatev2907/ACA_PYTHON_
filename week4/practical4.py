import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


def ex1():
    df = pd.DataFrame({
        "Name": ["Jack",
                 "John",
                 "Allen",
                 "Jane  "],
        "Surename": ["Fine",
                     "Smith",
                     "Colt",
                     "Jackson"],
        "Age": ["16-25", "16-25", "30-60", "30-60"],
        "Sex": ["male", "male", "male", "female"],
        "status": ["student", "student", "tutor", "tutor"]}
    )
    df.set_index(['Name', "Surename"])
    print(df)


def ex2():
    df = pd.read_csv("netflix_titles.csv")

    print(df[(df['type'] == 'Movie') & (df['release_year'] > 2015) & (
            df["cast"].str.contains('Kevin Spacey') | df['cast'].str.contains('Leonardo DiCaprio'))])


def ex3():
    df = pd.read_csv("netflix_titles.csv")
    df['Count_Column'] = df['director'].map(df['director'].value_counts()).fillna(0)
    print(df)


def ex4():
    df = pd.read_csv("netflix_titles.csv")
    k = df.assign(cast=df['cast'].str.split(',')).explode('cast')
    print(k)


def ex5():
    df = pd.read_csv("netflix_titles.csv")
    df1 = df[(df['type'] == 'Movie') & (df["cast"].str.contains('Antonio Banderas'))].sort_values(by='release_year',
                                                                                                  ascending=True)
    print(df1)
    plt.plot(df1['title'], df1['duration'])
    plt.show()


def ex6():
    df = pd.read_csv("netflix_titles.csv")
    df["date_added"] = pd.to_datetime(df["date_added"]).dt.to_period('M')
    df = df.sort_values(by="date_added")
    s = df['date_added'].map(df['date_added'].value_counts())
    df["date_added"] = df["date_added"].astype(str)
    plt.plot(df['date_added'], s)
    plt.show()
    s.hist()
    plt.show()


def ex7():
    df = pd.read_csv("netflix_titles.csv")
    df["date_added"] = pd.to_datetime(df["date_added"])
    df = df.sort_values(by="date_added")
    df['days_since_last_event'] = df["date_added"].diff().apply(lambda x: x.days)


def ex8():
    df = pd.read_csv("netflix_titles.csv")
    df["date_added"] = pd.to_datetime(df["date_added"])
    df = df.sort_values(by="date_added")
    df['days_since_last_event_director'] = df.groupby('director')["date_added"].diff().apply(lambda x: x.days)
    print(df)
# df.to_csv('new_name.csv')
