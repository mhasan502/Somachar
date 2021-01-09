from news.models import News
from rest_framework import serializers
from rest_framework.permissions import AllowAny


# Serialize Json data
class newsSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = News
        fields = ('heading', 'imagelink', 'newslink', 'papername', 'time', 'details')
