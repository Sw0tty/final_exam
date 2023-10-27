from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from .resources import HARDEST_TYPE, STATUS_TYPE


class Tourist(models.Model):
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)


class MountainPass(models.Model):
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS_TYPE, default='new', blank=False)
    person_add = models.OneToOneField("Tourist", on_delete=models.CASCADE, related_name='person_add')
    

class MountainCoords(models.Model):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    height = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    mountain_pass = models.OneToOneField("MountainPass", on_delete=models.CASCADE)


class Image(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=255, unique=True)
    mountain_pass = models.OneToOneField("MountainPass", on_delete=models.CASCADE)


class MountainLevel(models.Model):
    summer = models.CharField(max_length=2, choices=HARDEST_TYPE)
    autumn = models.CharField(max_length=2, choices=HARDEST_TYPE)
    spring = models.CharField(max_length=2, choices=HARDEST_TYPE)
    winter = models.CharField(max_length=2, choices=HARDEST_TYPE)
    mountain_pass = models.OneToOneField("MountainPass", on_delete=models.CASCADE)

# {
#   "beauty_title": "пер. ",
#   "title": "Пхия",
#   "other_titles": "Триев",
#   "connect": "", // что соединяет, текстовое поле
 
#   "add_time": "2021-09-22 13:18:13",
#   "user": {"email": "qwerty@mail.ru", 		
#         "fam": "Пупкин",
# 		 "name": "Василий",
# 		 "otc": "Иванович",
#         "phone": "+7 555 55 55"}, 
 
#    "coords":{
#   "latitude": "45.3842",
#   "longitude": "7.1525",
#   "height": "1200"}
 
 
#   level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
#   "summer": "1А",
#   "autumn": "1А",
#   "spring": ""},
 
#    images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
# }