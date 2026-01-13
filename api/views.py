from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


    @action(detail=True , methods=['post'])
    def rate_meal(self , request , pk=None):
        # # update the meal rate or create a new one
        # if 'stars' in request.data:
        #     # first check if the meal exists , you will update else you will create

        #     meal = Meal.objects.get(id=pk)
        #     username = request.data['username']
        #     stars = request.data['stars']
        #     user = User.objects.get(username=username)
        #     try:
        #         rating = Rating.objects.get(user=user.id , meal=meal.id)
        #         rating.stars = stars
        #         rating.save()
        #         serializer = RatingSerializer(rating , many=False)
        #         json = {'message': 'Rating updated' , 'result': serializer.data}
        #         return Response(json , status=status.HTTP_200_OK)

        #     except:
        #         # create a new instant
        #         rating = Rating.objects.create(user=user , meal=meal , stars=stars)
        #         serializer = RatingSerializer(rating , many=False)
        #         json = {'message': 'Rating created' , 'result': serializer.data}
        #         return Response(json , status=status.HTTP_201_CREATED)
            
        # else:
        #     json = {'message': 'You need to provide stars'}
        #     return Response(json ,status=status.HTTP_400_BAD_REQUEST)

        stars = request.data.get('stars')
        username = request.data.get('username')

        if not stars or not username:
            return Response({'message': 'You need to provide stars and username'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            meal = Meal.objects.get(id=pk)
            user = User.objects.get(username=username)

            rating , created = Rating.objects.update_or_create(
                user=user,
                meal=meal,
                defaults={'stars': stars}
            )

            serializer = RatingSerializer(rating , many=False)

            response = {
                'message':'rating created' if created else 'rating updated',
                'result': serializer.data
            }

            return Response(response , status=status.HTTP_200_OK)
        except Meal.DoesNotExist:
            return Response({'message': 'Meal not found'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer