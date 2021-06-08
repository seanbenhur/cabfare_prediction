"""Code for preprocessing the data and converting them into pickle files"""

import pandas as pd
from joblib import dump
from sklearn.preprocessing import LabelEncoder

#read data
data = pd.read_csv("data/train.csv")
train_data, test_data = data.iloc[0:75000,2:], data.iloc[75001:,2:]

#change the datatype to strings
le  = LabelEncoder()

train_data["cab_provider"] = le.fit_transform(train_data["cab_provider"])
test_data["cab_provider"] = le.transform(test_data["cab_provider"])

train_data["source"] = le.fit_transform(train_data["source"])
test_data["source"] = le.transform(test_data["source"])

train_data["destination"] = le.fit_transform(train_data["destination"])
test_data["destination"] = le.transform(test_data["destination"])

train_data["cab_type"] = le.fit_transform(train_data["cab_type"])
test_data["cab_type"] = le.transform(test_data["cab_type"])

#dump the files
dump(train_data,"data/train_data.joblib")
dump(test_data,"data/test_data.joblib")
