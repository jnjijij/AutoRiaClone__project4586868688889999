from django.test import TestCase
from .models import Auto

class AutoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Auto.objects.create(title='Test Auto 1', description='Test Auto 1 Description')
        Auto.objects.create(title='Test Auto 2', description='Test Auto 2 Description')

    def test_auto_content(self):
        auto = Auto.objects.get(id=1)
        expected_object_name = f'{auto.title}'
        self.assertEquals(expected_object_name, str(auto))

    def test_auto_list_view(self):
        response = self.client.get('/autos/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Auto 1')
        self.assertContains(response, 'Test Auto 2')

    def test_auto_detail_view(self):
        response = self.client.get('/autos/1/')
        no_response = self.client.get('/autos/100/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Auto 1')
        self.assertContains(response, 'Test Auto 1 Description')
        self.assertEqual(no_response.status_code, 404)

    def test_auto_create_view(self):
        response = self.client.post('/autos/create/', {'title': 'Test Auto 3', 'description': 'Test Auto 3 Description'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/autos/3/')

    def test_auto_update_view(self):
        response = self.client.post('/autos/1/update/', {'title': 'Updated Auto 1', 'description': 'Updated Auto 1 Description'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/autos/1/')

    def test_auto_delete_view(self):
        response = self.client.get('/autos/1/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/autos/')

    from django.test import TestCase
    from .models import Auto

    class AutoModelTest(TestCase):
        @classmethod
        def setUpTestData(cls):
            Auto.objects.create(title='Test Auto 1', description='Test Auto 1 Description')
            Auto.objects.create(title='Test Auto 2', description='Test Auto 2 Description')

        def test_auto_content(self):
            auto = Auto.objects.get(id=1)
            expected_object_name = f'{auto.title}'
            self.assertEquals(expected_object_name, str(auto))

        def test_auto_list_view(self):
            response = self.client.get('/autos/')
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Test Auto 1')
            self.assertContains(response, 'Test Auto 2')

        def test_auto_detail_view(self):
            response = self.client.get('/autos/1/')
            no_response = self.client.get('/autos/100/')
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Test Auto 1')
            self.assertContains(response, 'Test Auto 1 Description')
            self.assertEqual(no_response.status_code, 404)

        def test_auto_create_view(self):
            response = self.client.post('/autos/create/',
                                        {'title': 'Test Auto 3', 'description': 'Test Auto 3 Description'})
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/autos/3/')

        def test_auto_update_view(self):
            response = self.client.post('/autos/1/update/',
                                        {'title': 'Updated Auto 1', 'description': 'Updated Auto 1 Description'})
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/autos/1/')

        def test_auto_delete_view(self):
            response = self.client.get('/autos/1/delete/')
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/autos/')
