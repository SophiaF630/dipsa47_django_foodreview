from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Category, Restaurant, Review


class RestaurantListView(generic.ListView):
    template_name = 'foodreview/restaurant_list.html'
    context_object_name = 'restaurant_list'
    def get_queryset(self):
        return Restaurant.objects.order_by('name')

class ReviewListView(generic.ListView):
    template_name = 'foodreview/restaurant_detail.html'
    context_object_name = 'latest_review_list'
    def get_queryset(self):
        return Review.objects.order_by('-posted_date')

class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = 'foodreview/restaurant_detail.html'

def home(request):
    category_list = Category.objects.order_by('category_name')
    context = {'category_list':category_list}
    return render(request, 'foodreview/home.html', context)
