
from joblib import load
import sklearn.metrics as metrics
import json
import numpy as np

#data path
test_data_path =  "data/test_data.joblib"
model_path = "model/lgbm.joblib"
#ouput score path
metrics_path = "outputs/metrics.json"

#load test data
with open(test_data_path, 'rb') as f:
    test = load(f)

#load model
with open(model_path, 'rb') as f:
    model = load(f)



test_data = test.iloc[:,:-1]
labels = test['fare']

#predict on the  test data
lgbm_preds = model.predict(test_data)
msle = metrics.mean_squared_log_error(labels,lgbm_preds)
mse = metrics.mean_squared_error(labels,lgbm_preds)
rmse = np.sqrt(mse)
r2_score = metrics.r2_score(labels,lgbm_preds)

with open(metrics_path, 'w') as outfile:
        json.dump({ "rmse": rmse, "mse": msle, "r2_score":r2_score}, outfile)