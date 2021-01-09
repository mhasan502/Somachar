from news.models import News
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from news.serializers import newsSerializer


# Return searched news by user (API)
class NewsList(APIView):
    permission_classes = [AllowAny]

    # Checking GET method
    def get(self, requests, s):
        print(requests)
        search = s
        if search is None or bool(search) == False:
            result = News.objects.order_by('-time')
        else:
            result = News.objects.filter(heading__icontains=search).order_by('-time')
        serializer = newsSerializer(result, many=True)
        return Response(serializer.data)


# Return last 20 news (API)
class AllNewsList(APIView):
    permission_classes = [AllowAny]

    # Checking GET method
    def get(self, requests):
        result = News.objects.order_by('-time')[:20]
        serializer = newsSerializer(result, many=True)
        return Response(serializer.data)