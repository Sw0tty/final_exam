from django.db import models
from django.core.validators import MinValueValidator

from .resources import HARDEST_TYPE, STATUS_TYPE


class Tourist(models.Model):
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
<<<<<<< HEAD

    def __str__(self) -> str:
        return f"{self.fam} {self.name} {self.otc}"
=======
>>>>>>> master


class MountainPass(models.Model):
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS_TYPE, default='new', blank=False)
    user = models.OneToOneField("Tourist", on_delete=models.CASCADE, related_name='user')

    def __str__(self) -> str:
        return self.title


class MountainCoords(models.Model):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    height = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    mountain_pass = models.OneToOneField("MountainPass", on_delete=models.CASCADE, related_name='coords')

    def __str__(self) -> str:
        return f"{self.latitude} {self.longitude} {self.height}"


class Image(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=255, unique=True)
    mountain_pass = models.ForeignKey("MountainPass", on_delete=models.CASCADE, related_name='images')

    def __str__(self) -> str:
        return self.title


class MountainLevel(models.Model):
    summer = models.CharField(max_length=2, choices=HARDEST_TYPE)
    autumn = models.CharField(max_length=2, choices=HARDEST_TYPE)
    spring = models.CharField(max_length=2, choices=HARDEST_TYPE)
    winter = models.CharField(max_length=2, choices=HARDEST_TYPE)
    mountain_pass = models.OneToOneField("MountainPass", on_delete=models.CASCADE, related_name='level')
