from django.db import models
import numpy as np

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    address = models.CharField(max_length=50)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(list(all_ratings))

    def total_reviews(self):
        total_reviews = map(lambda x: x.comment, self.review_set.all())
        return len(list(total_reviews))

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    comment_to_commentid = models.TextField()
    posted_date	= models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField()

    def __str__(self):
        return self.comment

 

 