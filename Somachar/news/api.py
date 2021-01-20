from news.models import News
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from news.serializers import newsSerializer


# Return searched news by user (API)
class NewsList(APIView):
    permission_classes = [AllowAny]

    # Getting queryset and returning news
    def get(self, requests, searchitem):
        print(requests)
        search = searchitem
        if search is None or bool(search) == False:
            result = News.objects.order_by('-time')[:30]
        else:
            result = News.objects.filter(heading__icontains=search).order_by('-time')[:30]
        serializer = newsSerializer(result, many=True)              # queryset contains multiple items
        return Response(serializer.data)


# Return last 30 news (API)
class AllNewsList(APIView):
    permission_classes = [AllowAny]

    # Getting queryset and returning news
    def get(self, requests):
        result = News.objects.order_by('-time')[:30]
        serializer = newsSerializer(result, many=True)              # queryset contains multiple items
        return Response(serializer.data)
