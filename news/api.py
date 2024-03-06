from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """
    Serializer for News model
    """
    permission_classes = [AllowAny]

    class Meta:
        """
        Meta class for NewsSerializer
        """
        model = News
        exclude = 'id'


class NewsList(APIView):
    """
    APIView for returning searched news by user
    """
    permission_classes = [AllowAny]

    def get(self, requests, searchitem=None):
        search = searchitem
        news_to_return = 30
        if search is None or bool(search) is False:
            result = News.objects.order_by('-time')[:news_to_return]
        else:
            result = News.objects.filter(heading__icontains=search).order_by('-time')[:news_to_return]
        serializer = NewsSerializer(result, many=True)
        return Response(serializer.data)


class AllNewsList(APIView):
    """
    APIView for returning last 30 news
    """
    permission_classes = [AllowAny]

    def get(self, requests):
        news_to_return = 30
        serializer = NewsSerializer(News.objects.order_by('-time')[:news_to_return], many=True)
        return Response(serializer.data)


class NewsDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for News model 'details' field
    """
    permission_classes = [AllowAny]

    class Meta:
        model = News
        fields = ['details']


class NewsDetails(APIView):
    """
    APIView for returning news details
    """
    permission_classes = [AllowAny]

    def get(self, requests, news_id):
        result = News.objects.filter(id=news_id)
        serializer = NewsDetailSerializer(result, many=True)
        return Response(serializer.data)
