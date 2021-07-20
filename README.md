# CabFare Prediction using Machine Learning

## Table of Contents

- [About](#about)
- [Usage](#usage)
- [Contributing](#contributing)

## About <a name = "about"></a>

This project uses Machine Learning methods to predict the fare of a cab travels, This project is a minimal example to learn MLops such as Docker, DVC and feature stores



## Usage <a name = "usage"></a>

To test this app locally, I would recommend you to create a virtual environment


```bash
conda create venv python=3.7
conda activate venv
git clone https://github.com/seanbenhur/cabfare_prediction.git
python app.py
python test.py
```
## Repostory Structure.
```
=== data                        Datsets in CSV, serialized jobib files and parquet file
=== features                    Feature store repository
=== src
====== evaluate.py              Code for evaluating the machine learning model
====== prepare_data.py          Scripts for cleaning the data
====== train.py                 Script for training the LGBM model
=== model                       Folder containing the saved model in joblib format
=== outputs                     Contains the metrics saved as a  JSON file
```



## Contributing <a name = "contributing">

If you found any issues please feel free to contribute


## TODO

<ol><li>Add Github actions</li></ol>
