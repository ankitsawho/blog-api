from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    slug = serializers.SlugField(max_length=100)
    createdAt = serializers.DateTimeField()
    title = serializers.CharField(max_length=250)
    intro = serializers.CharField()
    content = serializers.CharField()


class PostIntroSerializer(serializers.Serializer):
    slug = serializers.SlugField(max_length=100)
    title = serializers.CharField(max_length=250)
    intro = serializers.CharField()


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    url = serializers.CharField(max_length=50)