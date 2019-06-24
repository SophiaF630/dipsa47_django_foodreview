from django.contrib import admin
from .models import Restaurant, Review, Category

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('restaurant_name', 'comment', 'posted_by', 'posted_date', 'rating')
    list_filter = ['posted_date', 'posted_by', 'rating']
    search_fields = ['restaurant_name', 'comment']

admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Review, ReviewAdmin)
