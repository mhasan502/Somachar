from django.shortcuts import render
from news.models import News


# Show news/searched-news to user
def NewsView(request):
    search = request.GET.get('search')
    if search is None or bool(search) is False:
        result = News.objects.order_by('-time')[:30]
    else:
        result = News.objects.filter(heading__icontains=search).order_by('-time')[:30]

    return render(request, 'news.html', {'news': result})
