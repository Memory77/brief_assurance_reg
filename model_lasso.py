from sklearn.preprocessing import PolynomialFeatures, FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso, Ridge, ElasticNet, LinearRegression
from sklearn.model_selection import GridSearchCV
import math
import pandas as pd
import numpy as np
import streamlit as st




df = pd.read_csv('dataset3.csv')

print(df.head(), df.shape)
# separation des features et de la variable cible
X = df.drop('charges', axis=1)
y = df[['charges']]
print(f'''verif des dimensions X et Y
      X (dataset sans la variable cible): {X.shape}
      Y (la variable cible) : {y.shape}''')


# division du dataset en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.85, random_state=42, stratify=X['smoker'])
print(f''' verif du split 80 20 
80% du dataset : X train -> {X_train.shape}, Y train -> {y_train.shape}
# 20% du dataset : X test -> {X_test.shape}, Y test -> {y_test.shape}''')


#Elasticnet
# préprocesseur pour les variables numériques
def log_transform(x):
    return np.log(x + 1)

log_transformer = FunctionTransformer(log_transform)

preprocessor_num = Pipeline(steps=[
    ('log', log_transformer),
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('scaler', StandardScaler())
])
preprocessor_cat = Pipeline(steps=[
    ('encoder', OneHotEncoder()),
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
])

# preprocessing avec transformation des categories et des nums
preprocessor = ColumnTransformer(
    transformers=[
        ('num', preprocessor_num , ['age', 'bmi', 'children', 'bmi_smoker_interaction']),
        ('cat', preprocessor_cat , ['region']),
    ]
)
# création du pipeline de prétraitement et du modèle elasticnet
pipeline_lasso = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regression', Lasso())])


#test de différents hyperparam d'alpha pour le lasso
param_grid_lasso = {
    'regression__alpha': [5, 5.1, 7],
    'regression__precompute': [True],
    'regression__max_iter': [5000],
    
}

### grid search
grid_lasso = GridSearchCV(pipeline_lasso, param_grid_lasso, cv=5)


# eviter data leakage -> entraîner le pipeline sur les données d'entraînement 
grid_lasso.fit(X_train, y_train)
#puis predire y sur l'ensemble de test avec le meme pipeline
y_pred = grid_lasso.predict(X_test)
# print(y_pred)

