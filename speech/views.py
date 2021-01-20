from django.shortcuts import render
from news.models import News


# Show searched news to user
def newsView(request):
    search = request.GET.get('search')
    if search is None or bool(search) == False:
        result = News.objects.order_by('-time')[:30]
        number = result.count()
    else:
        print(search)
        result = News.objects.filter(heading__icontains=search).order_by('-time')[:30]
        number = result.count()
    data = {
        'news': result,
        'number': number,
    }
    return render(request, 'news.html', data)
