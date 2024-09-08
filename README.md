Madrid Airbnb Data Explorer
==============================

Analyze Madrid Airbnb dataset from [Kaggle](https://www.kaggle.com/datasets/rusiano/madrid-airbnb-data). Create SQL database with PostgreSQL, dashboard with Grafana and machine learning models with Tensorflow. Deployment with Docker and easy install with pip.

## Todo list
- Make the project pip installable.
- Create docker image.
- Add image and introduction chapter to notebook.
- Create graphs in Jupyter Notebook.
- Create models and save it at /models folder.

## How to install

For devs:
1. Run **pip install -r requirements.txt** in the root directoy. Create [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) environment if needed.
2. Install [postgreSQL](https://www.postgresql.org).
3. Install [Grafana](https://grafana.com).
4. Add **.env** file with variable **project_dir** pointing to root folder.

For users:

1. Make it easy, make it docker. Or, **pip install .** in the root directoy to install it as a python package.

## Resources in this project
Currently implemented you can find:
- Creation of SQL database and tables. See [**src/data/sql_manager.py**](https://github.com/mrvgME/Airbnb_Project/blob/master/src/data/sql_manager.py) and [**test/src/data/sql_manager.py**](https://github.com/mrvgME/Airbnb_Project/blob/master/test/src/data/sql_manager.py).
- Creation of airbnb data table using listing.csv file. See [**src/data/onboard_airbnb_data.py**](https://github.com/mrvgME/Airbnb_Project/blob/master/src/data/onboard_airbnb_data.py).
- Jupyter notebook for data exploration. See [**notebooks/explore_data.ipynb**](https://github.com/mrvgME/Airbnb_Project/blob/master/notebooks/explore_data.ipynb).
- Grafana dashboard at [**reports/Airbnb_Explorer.json**](https://github.com/mrvgME/Airbnb_Project/blob/master/reports/Airbnb_Explorer.json). See dashboard below.

![alt text](https://github.com/mrvgME/Airbnb_Project/blob/master/reports/figures/grafana_dashboard.png?raw=true)

## How to contribute

Just fork the repository and ask for merge request. Otherwise, create issue in the repository with suggestions.


Project organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
