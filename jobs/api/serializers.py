from rest_framework import serializers
from jobs.models import Jobpost


class PostSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Jobpost
        fields = '__all__'
