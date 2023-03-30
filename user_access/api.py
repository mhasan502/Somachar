from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated


# Serialize Json data
class userSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
        )


# User Information in API
class UserList(APIView):

    def get(self, requests, uname):
        u = User.objects.filter(username=uname)
        serializer = userSerializer(u, many=True)
        return Response(serializer.data)

    def User(self):
        pass
