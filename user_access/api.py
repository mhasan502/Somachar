from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from user_access.serializers import userSerializer


# User Information in API
class UserList(APIView):

    def get(self, requests, uname):
        print(uname)
        u = User.objects.filter(username=uname)
        serializer = userSerializer(u, many=True)
        return Response(serializer.data)

    def User(self):
        pass
