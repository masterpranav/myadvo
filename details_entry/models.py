from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
class Member(models.Model):

       
       residing_state = models.CharField(max_length=50)
       residing_city = models.CharField(max_length=50)



class State(models.Model):

         state=models.CharField(max_length=20)
         country = models.ForeignKey(Country)       

class City(models.Model):

        city=models.CharField(max_length=20)
        state=models.ForeignKey(State)