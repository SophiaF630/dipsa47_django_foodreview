from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'foodreview'
urlpatterns = [
    # path('', views.home),
    # ex: /
    # url(r'^$', views.review_list, name='review_list'),
    # path('review/', views.review_list, name='review_list'),
    # ex: /review/5/
    # url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    # ex: /restaurant/
    # url(r'^restaurant$', views.restaurant_list, name='restaurant_list'),
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    # ex: /restaurant/5/
    # url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),

    # path('<int:restaurant_id>/like/', views.like, name='like'),
]
