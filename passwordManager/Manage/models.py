from django.db import models

# Create your models here.
class passwords(models.Model):
    user = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    password =models.CharField(max_length=20)

    @classmethod
    def create(cls, user,service,password):
        book = cls(user=user,service =service,password=password)
        # do something with the book
        return book
