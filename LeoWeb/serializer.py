from rest_framework import serializers
from .models import ContentModel,TagModel



class ContentSerializer(serializers.ModelSerializer):
    slug =serializers.SlugField(
        read_only=True,
        )
    class Meta:
        model=ContentModel
        fields  =['title','article','slug','tag']


class TagSerializer(serializers.ModelSerializer):
    content=ContentSerializer(many=True,)
    class Meta:
        model = TagModel
        fields = ['catagory','content']
        
    def create(self, validated_data):
        tracks_data = validated_data.pop('content')
        tag = TagModel.objects.create(**validated_data)
        for track_data in tracks_data:
            ContentModel.objects.create(tag=tag, **track_data)
        return tag
    
    def update(self, instance, validated_data):
        content = validated_data.pop('content')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance





