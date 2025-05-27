from django.test import TestCase

class LandFunctionalityTest(TestCase):
    def test_land_registration_flow(self):
        response = self.client.post('/register/', {
            'owner': 'Bob',
            'land_id': '789',
            'location': 'Zone C'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Transaction Successful', response.content.decode())
