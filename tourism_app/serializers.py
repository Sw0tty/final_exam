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
    id = serializers.IntegerField()

    class Meta:
        model = Image
        exclude = ('mountain_pass',)


class BaseMountainPassSerializer(serializers.ModelSerializer):
    """
    Base API serializer to construct main serializer
    """
    user = TouristSerializer()
    coords = MountainCoordsSerializer()
    level = MountainLevelSerializer()
    images = ImageSerializer(many=True)


class MountainPassSerializer(BaseMountainPassSerializer, serializers.ModelSerializer):
    """
    API serializer for get detail mountain pass
    """
    class Meta:
        model = MountainPass
        exclude = ('status',)

    def get_tourist(self, user_email):
        if Tourist.objects.filter(email=user_email):
            return Tourist.objects.get(email=user_email)
        return None

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')
        tourist = self.get_tourist(user_email=user_data['email'])

        if not tourist:
            tourist = Tourist.objects.create(**user_data)   
               
        mountain_pass = MountainPass.objects.create(user=tourist, **validated_data)    
        MountainCoords.objects.create(mountain_pass=mountain_pass, **coords_data)
        MountainLevel.objects.create(mountain_pass=mountain_pass, **level_data)

        if images_data:
            for image_data in images_data:
                Image.objects.create(mountain_pass=mountain_pass, **image_data)

        return mountain_pass


class DetailMountainPassSerializer(BaseMountainPassSerializer, serializers.ModelSerializer):
    """
    API serializer for get, patch detail mountain pass
    """
    class Meta:
        model = MountainPass
        fields = '__all__'

    def get_existing_fk(self, pk):
        return Image.objects.filter(mountain_pass=pk).values_list('id', flat=True)
    
    def update(self, instance, validated_data):

        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')
        existing_images_id = [*self.get_existing_fk(instance.pk)]

        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.save()

        MountainCoords.objects.filter(id=instance.id).update(
            latitude=coords_data.get('latitude'),
            longitude=coords_data.get('longitude'),
            height=coords_data.get('height')
        )   

        MountainLevel.objects.filter(id=instance.id).update(
            summer=level_data.get('summer'),
            autumn=level_data.get('autumn'),
            spring=level_data.get('spring'),
            winter=level_data.get('winter')
        )

        if images_data:
            for image_data in images_data:
                if "id" in image_data.keys():
                    existing_images_id.remove(image_data['id'])
                    Image.objects.filter(id=image_data['id']).update(
                        data=image_data.get('data'),
                        title=image_data.get('title')
                    )
                else:
                    Image.objects.create(mountain_pass=instance, **image_data)
        
        if existing_images_id:
            for exist_id in existing_images_id:
                Image.objects.get(id=exist_id).delete()

        return instance
    