import unittest
from app import app 
import json

class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        """
        Sets up the testing environment for the error handling tests.
        """

        # Set the testing flag in the app configuration
        app.config['TESTING'] = True

        # Create a test client to interact with the API endpoints
        self.app = app.test_client()

    def test_missing_input(self):
        """
        Tests that the API endpoint handles missing input data and returns an appropriate error response.
        """

        incomplete_input_data = {
            '2020_Torneos ganados': 4,  # Number of tournaments won in 2020
            '2020_Rendimiento': 0.8,  # Win rate in 2020 (valid range: 0-1)
            'partidosganados': 300  # Total matches won
        }

        # Omit the '2020_Finales' field to simulate missing input

        # Send a POST request to the '/predict' endpoint with the incomplete input data
        response = self.app.post('/predict', data=json.dumps(incomplete_input_data), content_type='application/json')

        # Verify that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_input_format(self):
        """
        Tests that the API endpoint handles input data with incorrect data types and returns an appropriate error response.
        """

        invalid_input_data = {
            '2020_Torneos ganados': 'string',  # Invalid data type for tournaments won (should be an integer)
            '2020_Finales': 'string',  # Invalid data type for finals reached (should be an integer)
            '2020_Rendimiento': 'string',  # Invalid data type for win rate (should be a float)
            'partidosganados': 'string',  # Invalid data type for total matches won (should be an integer)
        }

        # Send a POST request to the '/predict' endpoint with the invalid input data
        response = self.app.post('/predict', data=json.dumps(invalid_input_data), content_type='application/json')

        # Verify that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
