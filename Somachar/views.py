from django.shortcuts import render
from django.views import View


class IndexView(View):
    """
    Index View
    """
    def get(self, request):
        """
        Handles GET requests for the index view.
        """
        return render(request, template_name='index.html')
