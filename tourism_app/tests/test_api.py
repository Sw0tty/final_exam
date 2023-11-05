"""
API test requests logic
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from .tests import TestSetModels
from tourism_app.models import MountainPass, MountainCoords, MountainLevel
from tourism_app.views import SubmitData, ListMountainPasses, DetailMountainPass


class MountainPassCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = SubmitData.as_view()
        self.url = reverse('create_pass')
        self.sample_pass = TestSetModels().setUp()

    def test_create_pass(self):
        request = self.factory.post(self.url, self.sample_pass, format='json')       
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MountainPass.objects.get(id=response.data['id']).title, 'п. Дятлова')
        self.assertEqual(MountainCoords.objects.get(mountain_pass=response.data['id']).height, 123)
        self.assertEqual(MountainLevel.objects.get(mountain_pass=response.data['id']).summer, 'A')
        self.assertEqual(MountainPass.objects.get(id=response.data['id']).user.email, 'vanya@mail.ru')
    
    
class MountainPassPatchTestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = DetailMountainPass.as_view()
        self.url = reverse('update_pass', args=[1])
        self.sample_pass = TestSetModels().setUp()

    def test_patch_pass_good(self):
        """
        Request: with GOOD data
        """
        request = self.factory.patch(self.url, self.sample_pass, format='json')
        response = self.view(request, 1)
        self.assertEqual(response.data['message'], 'Запись обновлена')
        

    def test_patch_pass_bad(self):
        """
        Request: with BAD data
        """
        self.sample_pass['level']['summer'] = ''
        request = self.factory.patch(self.url, self.sample_pass, format='json')
        response = self.view(request, 1)
        self.assertEqual(response.data['message'], 'Введены недопустимые значения')


class MountainPassFilterTestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = ListMountainPasses.as_view()
        self.user_email = 'vanya@mail.ru'
        self.url = reverse('filter_pass')
        self.sample_pass = TestSetModels().setUp()
    
    def test_filter_pass_good(self):
        """
        Request: with GOOD data
        """
        request = self.factory.get(self.url, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        request = self.factory.get(f'{self.url}/?user_email={self.user_email}', format='json')
        response = self.view(request)
        self.assertEqual(response.data[0]['user']['email'], self.user_email)

    def test_filter_pass_bad(self):
        """
        Request: with BAD data
        """
        self.user_email = 'notexist@mail.ru'
        request = self.factory.get(f'{self.url}/?user_email={self.user_email}', format='json')
        response = self.view(request)
        self.assertEqual(response.data['message'], 'Ничего не найдено')
