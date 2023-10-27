from django.contrib import admin

from tourism_app.models import Tourist, MountainPass, MountainCoords, Image, MountainLevel


admin.site.register(Tourist)
admin.site.register(MountainPass)
admin.site.register(MountainCoords)
admin.site.register(Image)
admin.site.register(MountainLevel)
