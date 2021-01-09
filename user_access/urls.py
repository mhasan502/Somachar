from django.conf.urls import url
from user_access.api import UserList


urlpatterns = [
    url(r'(?P<uname>[._A-Za-z0-9]+)/$', UserList.as_view()),
]
