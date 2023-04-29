from .views import home_page
from django.urls import path, include


urlpatterns = [
    path('', home_page, name = "home_page"),
    # path('review/', , name='review'),
    # path('home/', index_page, name='index')
]