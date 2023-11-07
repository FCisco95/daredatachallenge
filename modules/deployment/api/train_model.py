import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle  # model serialization



import psycopg2
import pandas as pd

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="daredatachallenge",
    user="admin",
    password="admin",
)



def query_database(connection, query):
    try:
        # Execute the SQL query
        df = pd.read_sql(query, connection)
        return df
    except Exception as error:
        print(f"Error: {error}")

sql_query = "SELECT * FROM padel_players;"

# Query the database and store the results in a DataFrame
df = query_database(connection, sql_query)

# Feature and target
X = df[['2020_Rendimiento', '2020_Torneos ganados', '2020_Finales', 'partidosganados']]
y = df['puntuacion']

# Data Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model as 'model.pkl'
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Model Evaluation
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')


