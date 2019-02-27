from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant, Customer, Review
from .serializers import RestaurantSerializer, CustomerSerializer, ReviewSerializer

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer