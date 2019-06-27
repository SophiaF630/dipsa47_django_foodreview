from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'foodreview'
urlpatterns = [
    # ex: /restaurant/
    path('restaurant/', views.RestaurantListView.as_view(), name='restaurant_list'),
    # ex: /
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    # ex: /restaurant/5/
    path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),

    # path('<int:restaurant_id>/like/', views.like, name='like'),
]
