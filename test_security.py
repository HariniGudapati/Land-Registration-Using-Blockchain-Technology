from django.test import TestCase

class SecurityTestCase(TestCase):
    def test_prevent_unauthorized_access(self):
        response = self.client.get('/admin/landrecords/')
        self.assertNotEqual(response.status_code, 200)
