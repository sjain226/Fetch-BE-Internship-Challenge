import unittest
import json
from points_manager import app 

class PointsManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_add(self): 
        response = self.app.post('/add', json={
            "payer": "DANNON",
            "points": 5000,
            "timestamp": "2020-11-02T14:00:00Z"
        })
        self.assertEqual(response.status_code, 200)

    def test_spend(self): 
        self.app.post('/add', json={
            "payer": "DANNON",
            "points": 5000,
            "timestamp": "2020-11-02T14:00:00Z"
        })

        response = self.app.post('/spend', json={
            "points": 3000
        })
        self.assertEqual(response.status_code, 200)

        spend_data = json.loads(response.data.decode())
        
        self.assertEqual(spend_data, [ 
            {"payer": "DANNON", "points": -3000}
        ])

    def test_balance(self): 
        self.app.post('/add', json={
            "payer": "DANNON",
            "points": 5000,
            "timestamp": "2020-11-02T14:00:00Z"
        })
        self.app.post('/spend', json={
            "points": 3000
        })

        response = self.app.get('/balance')
        self.assertEqual(response.status_code, 200)

        balance_data = json.loads(response.data.decode())
        self.assertEqual(balance_data, {"DANNON": 2000}) 


if __name__ == '__main__':
    unittest.main()
