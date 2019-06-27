from django.contrib import admin
from .models import Restaurant, Review, Category

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('restaurant', 'customer', 'posted_date', 'rating')
    list_filter = ['posted_date', 'customer', 'rating']
    search_fields = ['restaurant']

admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Review, ReviewAdmin)
