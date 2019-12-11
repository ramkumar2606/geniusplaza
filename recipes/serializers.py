from django.contrib.auth.models import User, Group
from .models import Recipe,Step,Ingredient
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'user_id']
    
    def create(self, validated_data):
        r = Recipe()
        r.name = validated_data['name']
        r.user = validated_data['user_id']
        r.save()
        return r
        
class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    recipe_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Recipe.objects.all())
    class Meta:
        model = Ingredient
        fields = ['id', 'text', 'recipe_id']
    
    def create(self, validated_data):
        i = Ingredient()
        i.text = validated_data['text']
        i.recipe = validated_data['recipe_id']
        i.save()
        return i

