from rest_framework import serializers

from .models import Tourist, MountainCoords, MountainPass , Image, MountainLevel


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'


class MountainCoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainCoords
        exclude = ('mountain_pass',)


class MountainLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainLevel
        exclude = ('mountain_pass',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('mountain_pass',)


class MountainPassSerializer(serializers.ModelSerializer):
    user = TouristSerializer()
    coords = MountainCoordsSerializer()
    level = MountainLevelSerializer()
    images = ImageSerializer(many=True)


    class Meta:
        model = MountainPass
        exclude = ('status',)


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')

        tourist = Tourist.objects.create(**user_data)      
        mountain_pass = MountainPass.objects.create(user=tourist, **validated_data)    
        MountainCoords.objects.create(mountain_pass=mountain_pass, **coords_data)
        MountainLevel.objects.create(mountain_pass=mountain_pass, **level_data)

        if images_data:
            for image_data in images_data:
                Image.objects.create(mountain_pass=mountain_pass, **image_data)

        return mountain_pass
