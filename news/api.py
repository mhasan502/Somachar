from news.models import News
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny


# Converting queryset to Json data
class NewsSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = News
        fields = (
            'heading',
            'imagelink',
            'newslink',
            'papername',
            'time',
            'details'
        )


# Return searched news by user (API)
class NewsList(APIView):
    permission_classes = [AllowAny]

    # Getting queryset and returning news
    def get(self, requests, searchitem=None):
        search = searchitem
        if search is None or bool(search) is False:
            result = News.objects.order_by('-time')[:30]
        else:
            result = News.objects.filter(heading__icontains=search).order_by('-time')[:30]
        serializer = NewsSerializer(result, many=True)  # queryset contains multiple items
        return Response(serializer.data)


# Return last 30 news (API)
class AllNewsList(APIView):
    permission_classes = [AllowAny]

    # Getting queryset and returning news
    def get(self, requests):
        serializer = NewsSerializer(News.objects.order_by('-time')[:30], many=True)  # queryset contains multiple items
        return Response(serializer.data)


# News Details Serializer
class NewsDetailSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = News
        fields = ['details']


# Return news details
class NewsDetails(APIView):
    permission_classes = [AllowAny]

    def get(self, requests, news_id):
        result = News.objects.filter(id=news_id)
        serializer = NewsDetailSerializer(result, many=True)
        return Response(serializer.data)
