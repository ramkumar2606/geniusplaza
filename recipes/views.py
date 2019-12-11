
from django.http import JsonResponse
from django.views import View
from .models import Recipe,Step,Ingredient
from django.contrib.auth.models import User,Group
from django.core.exceptions import ObjectDoesNotExist
from .serializers import RecipeSerializer, IngredientSerializer
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response


class RecipeList(APIView):
    """
    API endpoint that allows users to create or list recipes.
    """
    def get(self, request, format=None):
        user_id = request.GET.get('user_id',None)
        if user_id:
            recipes = Recipe.objects.filter(user=user_id)
        else:
            recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecipeDetail(APIView):
    """
    API endpoint that allows users to get,update and delete the recipe.
    """
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"id":pk})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)