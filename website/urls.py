from django.conf.urls import url
from website import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url('^/about$', views.AboutPageView.as_view()),
    url(r'^admin/', admin.site.urls)
]