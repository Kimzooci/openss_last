import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_get_data(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello, this is data from data.txt!", response.get_json()["data"])
        print("Test Ended")

if __name__ == '__main__':
    unittest.main()
