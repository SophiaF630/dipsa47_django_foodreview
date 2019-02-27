from rest_framework import serializers
from .models import Restaurant, Customer, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'url', 'name', 'category', 'address')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'url', 'name', 'email')

class ReviewSerializer(serializers.ModelSerializer):
     class Meta:
        model = Review
        fields = ('id', 'url', 'restaurant_id', 'comments', 'posted_by', 'comment_to_commentid', 
        'posted_date', 'rating', 'likes')