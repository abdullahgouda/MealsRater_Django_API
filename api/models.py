from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class Meal(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=350)
    description = models.TextField()


    def number_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return ratings.count()
    
    def average_rating(self):
        ratings = Rating.objects.filter(meal=self)
        sum  = 0
        for x in ratings:
            sum += x.stars
        
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0



    def __str__(self):
        return self.title
    

class Rating(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4, editable=False)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.meal.title} - {self.stars} stars by {self.user.username}"
    

    class Meta:
        unique_together = (('meal', 'user'),)

        indexes = [
        models.Index(fields=['meal', 'user']),
        ]

