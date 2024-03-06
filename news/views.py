from django.views.generic import ListView
from .models import News


class NewsListView(ListView):
    """
    Show news/searched-news to user
    """
    model = News
    paginate_by = 30
    template_name = 'news.html'
    context_object_name = 'news'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            queryset = self.model.objects.filter(heading__icontains=search).order_by('-time')
        else:
            queryset = self.model.objects.order_by('-time')[:30]

        return queryset
