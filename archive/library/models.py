from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
 
    STATUS_CHOICES = [
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
        ('COLL', 'Collection'),
    ]
    reading_status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='UNREAD'
    )
    
    is_borrowed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Collection(models.Model): 
    name = models.CharField(max_length=255)
    wishlist = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name

class Reminder(models.Model):
    date = models.DateTimeField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.TextField(blank=True)
