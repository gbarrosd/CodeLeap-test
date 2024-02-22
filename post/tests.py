from django.test import TestCase
from post.models import Post

# Create your tests here.

class BaseTest(TestCase):
    def setUp(self):
        self.post_1 = Post.objects.create(
            username = "user test 1",
            title = "post test 1",
            content = "content test 1",
        )

        return super().setUp()

class PostTestCase(BaseTest):
    def test_create_post(self):
        response = self.client.post('/careers/', data = {
            'username':"jack",
            'title' : "post test 2",
            'content' : "content test 2",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_patch_post(self):
        updated_data = {
            'title': 'Updated Title'
        }
        response = self.client.patch(f'/careers/{self.post_1.id}/', data=updated_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        self.post_1.refresh_from_db()
        self.assertEqual(self.post_1.title, updated_data['title'])

    def test_delete_post(self):
        response = self.client.delete(f'/careers/{self.post_1.id}/')
        self.assertEqual(response.status_code, 204)

        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(id=self.post_1.id)

    def test_retrieve_post(self):
        response = self.client.get(f'/careers/{self.post_1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'post test 1')

    def test_invalid_data(self):
        response = self.client.post('/careers/', data={})
        self.assertEqual(response.status_code, 400) 
        self.assertIn('title', response.data)

