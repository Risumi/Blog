from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Post
from .serializers import PostSerializers
from django.urls import reverse

class BaseViewTest(APITestCase):
    client = APIClient()

# Create your tests here.
class GetAllPostTest(BaseViewTest):
    def test_get_all_post(self):
        response = self.client.get(reverse('post-all', kwargs={"version": "v1"}))
        expected = Post.objects.all()
        serialized = PostSerializers(expected,many=True)
        self.assertEqual(response.data,serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)