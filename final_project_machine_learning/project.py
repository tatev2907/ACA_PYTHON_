from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import json
import pymongo
import pandas as pd


def conn_to_db():
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['House_price']
    return mng_db


def add_train_into_collection(data):
    db = conn_to_db()
    collection_name = 'train'
    db_cm = db[collection_name]
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)


def exist_in_db(ID):
    db = conn_to_db()
    collection_test = 'test'
    db_test = db[collection_test]
    if db.train.find({'Unnamed: 0': ID}).count() > 0:
        a = db.train.find({"Unnamed: 0": ID})
        for b in a:
            db_test.remove()
            db_test.insert(b)
        return True
    return False


def add_to_resault_collection(data):
    db = conn_to_db()
    collection_test = 'test'
    db_cm = db[collection_test]
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.insert(data_json)


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


class PricePredict:
    def __init__(self):
        r1 = LinearRegression()
        r = GradientBoostingRegressor(alpha=0.9, init=None, learning_rate=0.2, loss='ls', max_depth=4, max_features=1.0,
                                      max_leaf_nodes=None, min_samples_leaf=5, min_samples_split=2, n_estimators=100,
                                      random_state=0, subsample=1.0, verbose=0, warm_start=False)
        self.model = r

    def preprocessing(self, X):
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "

        district = {'Norq Marash': 101, 'Achapnyak': 10, 'Arabkir': 20, 'Avan': 30, 'Center': 40, 'Davtashen': 50,
                    'Erebuni': 60, 'Malatia-Sebastia': 70, 'Nor Norq': 80, 'Nubarashen': 90, 'Qanaqer-Zeytun': 100,
                    'Shengavit': 110, 'Vahagni district': 120}
        condition = {'zero condition': 5, 'good': 6, 'newly repaired': 7}
        building_type = {'panel': 1, 'monolit': 2.1, 'stone': 2.2, 'other': 2.3}
        X = X.drop(['region', 'url', 'street'], axis=1)
        X['condition'] = X['condition'].apply(lambda x: condition[x])
        X['building_type'] = X['building_type'].apply(lambda x: building_type[x])
        X['district'] = X['district'].apply(lambda x: district[x])
        X = pd.get_dummies(X)
        return X

    def fit(self, X, y):
        assert isinstance(y, pd.Series), "Data must be pd.DataFrame "
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "
        X = self.preprocessing(X)
        self.model.fit(X, y)

    def predict(self, X):
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "
        X = self.preprocessing(X)
        return self.model.predict(X)

    def predict_for_test(self, X):
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "
        ls = list(X['Unnamed: 0'])
        for i in ls:
            if exist_in_db(i):
                index_of = X[X['Unnamed: 0'] == i].index
                X.drop(index_of, inplace=True)
        X = self.preprocessing(X)
        return self.model.predict(X)

    def add_predict_to_db(self, X):
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "
        price = self.predict(X)
        X = self.preprocessing(X)
        X['price'] = price
        add_train_into_collection(X)

    def add_test_to_db(self, X):
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "
        price = self.predict_for_test(X)
        X = self.preprocessing(X)
        X['price'] = price
        add_to_resault_collection(X)

    def score(self, X, y):
        assert isinstance(y, pd.Series), "Data must be pd.DataFrame "
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "
        y_predict = self.predict(X)
        return mean_squared_error(y_predict, y, squared=False)

    def plot(self, X, col_name):
        assert isinstance(X, pd.DataFrame), "Data must be pd.DataFrame "
        assert isinstance(col_name, str), "col_name must be string "
        X = self.preprocessing(X)
        plt.scatter(X.price, X.col_name)
        plt.title("Price vs area")


data = pd.read_csv('houses_train.csv')
test = pd.read_csv('test.csv') #user testing file
X = data.drop('price', axis=1)
y = data['price']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
print(x_train)
a = PricePredict()
a.fit(x_train, y_train)
# a.predict(X)
a.add_predict_to_db(X)
# a.predict_for_test(test)
a.add_test_to_db(test)
print(a.score(x_test, y_test))
a.plot(test, 'area')
