from .models import blogData
from rest_framework import serializers


class blogDataSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = blogData
        fields = "__all__"
