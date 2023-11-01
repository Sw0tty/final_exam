from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from tourism_app.models import Tourist
from tourism_app.views import SubmitData, ListMountainPasses


# class TouristCreateTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.tourist = Tourist.objects.create(fam="Иванов", name="Иван", otc="Иванович", email="vanya@mail.ru", phone="89919019090")
#         return super().setUp()
    
#     def test_get_tourist(self):
#         response = self.client.get(reverse(""))


class MountainPassCreateTest(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = SubmitData.as_view()
        self.url = reverse('create_pass')

    def test_create_pass(self):
        sample_pass = {
             "user": {
                    "fam": "Иванов",
                    "name": "Иван",
                    "otc": "Иванович",
                    "email": "vanya@mail.ru",
                    "phone": "89919019090"
                },
                "coords": {
                    "latitude": "1,34G",
                    "longitude": "2,34.324G",
                    "height": 123
                },
                "level": {
                    "summer": "A",
                    "autumn": "B",
                    "spring": "B",
                    "winter": "D"
                },
                "images": [],
                "beauty_title": "Дятлова перевал",
                "title": "п. Дятлова",
                "other_titles": "Дятлова",
                "connect": "-"
        }

        request = self.factory.post(self.url, sample_pass, format='json')

        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class FilterMountainsPassesTestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = ListMountainPasses.as_view()
        self.url = reverse('filter_pass')

    def test_filter_data(self):
        email_user = 'vanya@mail.ru'
        request = self.factory.get(self.url, email_user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
