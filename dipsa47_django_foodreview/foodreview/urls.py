from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('restaurant', views.RestaurantView)
router.register('customer', views.CustomerView)
router.register('restaurant/review', views.ReviewView)

urlpatterns = [
    path('', include(router.urls))
]
