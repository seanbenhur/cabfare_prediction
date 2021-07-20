from joblib import load, dump
import lightgbm as lgbm
from sklearn.metrics import  mean_squared_log_error
import numpy as np


#load the train data
with open('data/train_data.joblib', 'rb') as f:
    train = load(f)
#load the test data
with open('data/test_data.joblib', 'rb') as f:
    test = load(f)
#set output dir for model
model_path = "model/lgbm.joblib"

#extract the label columns
train_label = train.pop('fare')
test_label = test.pop('fare')

train_data = lgbm.Dataset(train, label=train_label)
test_data = lgbm.Dataset(test, label=test_label)

param = {'objective': 'regression',
         'boosting': 'gbdt',  
         'metric': 'l2_root',
         'learning_rate': 0.01, 
         'num_iterations': 1000,
         'num_leaves': 20,
         'max_depth': -1,
         'min_data_in_leaf': 11,
         'bagging_fraction': 0.90,
         'bagging_freq': 1,
         'bagging_seed': 3,
         'feature_fraction': 0.90,
         'feature_fraction_seed': 2,
         'early_stopping_round': 200,
         'max_bin': 100
         }

lgbm = lgbm.train(params=param, verbose_eval=100, train_set=train_data, valid_sets=[test_data])


with open(model_path, "wb") as fd:
    dump(lgbm, fd)
