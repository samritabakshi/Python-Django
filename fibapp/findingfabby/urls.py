# findingfabby/urls.py
from django.conf.urls import url
from findingfabby import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^takeInput/$', views.takeInput.as_view()),
]


