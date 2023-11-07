# main.py
from database import connect_to_database, query_database
from data_processing import perform_eda_and_preprocessing
from model import split_data, train_and_evaluate_model

# Connect to the database
connection = connect_to_database()

# Query the data
df = query_database(connection, "SELECT * FROM padel_players;")

# Perform EDA and data preprocessing
df = perform_eda_and_preprocessing(df)

# Split data
X_train, X_test, y_train, y_test = split_data(df)

# Train and evaluate the model
mse, r2, coefficients = train_and_evaluate_model(X_train, X_test, y_train, y_test)

# Print results
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
for feature, coefficient in zip(feature_names, coefficients):
    print(f'{feature}: {coefficient}')
