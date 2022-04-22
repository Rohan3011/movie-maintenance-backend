from dataclasses import field
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image
        return request.build_absolute_uri(photo_url)
