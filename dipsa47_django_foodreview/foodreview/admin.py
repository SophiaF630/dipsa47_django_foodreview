from django.contrib import admin
from .models import Restaurant, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('restaurant_id', 'comments', 'posted_by', 'posted_date', 'rating')
    list_filter = ['posted_date', 'posted_by']
    search_fields = ['comments']

admin.site.register(Restaurant)
admin.site.register(Review, ReviewAdmin)
