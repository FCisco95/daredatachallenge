import unittest
from app import app  # Importing my app
import json

class TestPredictionAPI(unittest.TestCase):
    def setUp(self):
        """
        Sets up the testing environment for the API tests.
        """

        # Set the testing flag in the app configuration
        app.config['TESTING'] = True

        # Create a test client to interact with the API endpoints
        self.app = app.test_client()

    def test_valid_prediction(self):
        """
        Tests that the API endpoint can handle valid input data and returns a valid response.
        """

        valid_input_data = {
            '2020_Torneos ganados': 4,  
            '2020_Finales': 4,  
            '2020_Rendimiento': 0.8,  # Win rate in 2020 (valid range: 0-1)
            'partidosganados': 300  # Total matches won from 2013
        }

        # Send a POST request to the '/predict' endpoint with the valid input data
        response = self.app.post('/predict', data=json.dumps(valid_input_data), content_type='application/json')

        # Verify that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Extract the response data in JSON format
        response_data = json.loads(response.data)

        # Check if the 'prediction' key exists in the response data
        self.assertTrue('prediction' in response_data)

        # Verify that the 'prediction' value is a float
        self.assertIsInstance(response_data['prediction'], float)

    def test_invalid_prediction(self):
        """
        Tests that the API endpoint can handle invalid input data and returns an appropriate error response.
        """

        invalid_input_data = {
            '2020_Torneos ganados': -1,  # Negative value for tournaments won, which is invalid
            '2020_Finales': 4,
            '2020_Rendimiento': 1.5,  # Invalid win rate, greater than 1
            'partidosganados': 300
        }

        # Send a POST request to the '/predict' endpoint with the invalid input data
        response = self.app.post('/predict', data=json.dumps(invalid_input_data), content_type='application/json')

        # Verify that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
