
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def split_data(df):
    X = df[['2020_Rendimiento', '2020_Torneos ganados', '2020_Finales', 'partidosganados']]
    y = df['puntuacion']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    coefficients = model.coef_
    feature_names = ['2020_Rendimiento', '2020_Torneos ganados', '2020_Finales', 'partidosganados']
    return mse, r2, coefficients
