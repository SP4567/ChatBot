import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ask_endpoint(self):
        response = self.app.post('/ask', json={'question': 'What is the best course for machine learning?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('course', response.json)

if __name__ == '__main__':
    unittest.main()