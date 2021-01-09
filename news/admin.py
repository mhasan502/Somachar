from django.contrib import admin
from news.models import News

# Admin can edit News Model
admin.site.register(News)
