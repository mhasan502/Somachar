from django.contrib import admin
from django.contrib.auth.models import User
from news.models import News

# Register Models to admin panel
admin.site.register(User)
admin.site.register(News)
