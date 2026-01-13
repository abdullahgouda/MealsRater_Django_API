
from rest_framework import serializers
from api.models import *


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description' , 'number_of_ratings' , 'average_rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'meal', 'user', 'stars']