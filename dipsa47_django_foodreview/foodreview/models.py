from django.db import models
import numpy as np

class Restaurant(models.Model):
    #restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    #commentid	
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    restaurant_id = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField()
    #posted_by = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    posted_by = models.CharField(max_length=100)
    comment_to_commentid = models.TextField()
    posted_date	= models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField()

    def __str__(self):
        return self.restaurant_id

 