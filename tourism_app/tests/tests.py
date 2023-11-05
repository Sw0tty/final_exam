"""
Tests base data
"""
from django.test import TestCase
from django.forms.models import model_to_dict

from tourism_app import models


class TestSetModels(TestCase):
    def setUp(self):
        self.tourist = models.Tourist.objects.create(
            fam="Иванов",
            name="Иван",
            otc="Иванович",
            email="vanya@mail.ru",
            phone="89919019090"
        )

        self.mountain_pass = models.MountainPass.objects.create(
            beauty_title="Дятлова перевал",
            title="п. Дятлова",
            other_titles="Дятлова",
            connect="-",
            user=self.tourist
        )

        self.mountain_coords = models.MountainCoords.objects.create(
            latitude="1,34G",
            longitude="2,34.324G",
            height=123,
            mountain_pass=self.mountain_pass
        )

        self.mountain_level = models.MountainLevel.objects.create(
            summer="A",
            autumn="B",
            spring="B",
            winter="D",
            mountain_pass=self.mountain_pass
        )

        images = [
            model_to_dict(models.Image.objects.create(
                data='tourism_app\\tests\\test.jpg',
                title=f'Перевал{image_number}',
                mountain_pass=self.mountain_pass
            ))
            for image_number in range(3)
        ]

        clear_images = []
        for i in images:
            del i['mountain_pass']
            clear_images.append(i)

        self.mountain_pass_dict = model_to_dict(self.mountain_pass)
        self.mountain_pass_dict['user'] = model_to_dict(self.tourist)
        coords_dict = model_to_dict(self.mountain_coords)
        del coords_dict['mountain_pass']
        self.mountain_pass_dict['coords'] = coords_dict
        level_dict = model_to_dict(self.mountain_level)
        del level_dict['mountain_pass']
        self.mountain_pass_dict['level'] = level_dict
        self.mountain_pass_dict['images'] = []
        return self.get_test_data()
    
    def get_test_data(self):
        return self.mountain_pass_dict

    def test_created_models(self):
        self.assertEqual(self.mountain_pass.__str__(), "п. Дятлова")
        self.assertEqual(self.mountain_coords.__str__(), "1,34G 2,34.324G 123")
