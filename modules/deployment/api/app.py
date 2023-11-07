from flask import Flask, render_template, request
import os
import numpy as np
import pickle

# Create a Flask application instance
app = Flask(__name__)
app.env = "development"

# Initialize a global variable to store the prediction result
result = ""

# Print a message indicating the Flask app is running
print("Flask app up and running!")

# Route for the home page
@app.route('/', methods=['GET'])
def hello():
    # Print a message indicating the function is being called
    print("I am In hello. Made some changes")

    # Render the index.html template
    return render_template('index.html')

# Route for handling prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    # Print information about the request method and type
    print("Request.method:", request.method)
    print("Request.TYPE", type(request))

    # Print a message indicating the prediction process is starting
    print("In the process of making a prediction.")

    # Check if the request method is POST
    if request.method == 'POST':
        # Extract form data values
        torneos = float(request.form['2020_Torneos ganados'])
        finales = float(request.form['2020_Finales'])
        rendimiento = float(request.form['2020_Rendimiento'])
        partidosganados = float(request.form['partidosganados'])

        # Convert form data into a NumPy array
        test_arr = np.array([torneos, finales, rendimiento, partidosganados]).reshape(1, -1)

        # Load the trained model from the pickle file
        model = pickle.load(open('model.pkl', 'rb'))
        print("Model Object: ", model)

        # Make a prediction using the loaded model
        prediction = model.predict(test_arr)

        # Determine the predicted class based on a threshold of 0.5
        predicted = "Not close" if prediction[0] > 0.5 else "Close"

        # Update the global result variable with the prediction and predicted class
        result = f"The model predicts that the player would have {prediction[0]:.2f} points. {predicted}"

        return render_template('index.html', result=result)

    # Render the index.html template if the request method is not POST
    return render_template('index.html')

# Run the Flask application on port 5001
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=False)
