from django.test import TestCase
from django.urls import reverse

class LandRecordIntegrationTest(TestCase):
    def test_create_land_record_and_retrieve(self):
        response = self.client.post(reverse('create_land'), {
            'owner': 'Alice',
            'land_id': '123',
            'location': 'Plot 22B',
        })
        self.assertEqual(response.status_code, 201)

        get_response = self.client.get(reverse('get_land', args=['123']))
        self.assertContains(get_response, 'Alice')
