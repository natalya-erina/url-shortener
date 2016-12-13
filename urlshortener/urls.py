from django.conf.urls import url

from urlshortener import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^templates/index.html', views.index, name='index'),
    url(r'^short_url/', views.redirect_and_show_ad, name='short_url')
]
