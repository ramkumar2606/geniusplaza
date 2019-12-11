from django.urls import path

from .views import RecipeList, RecipeDetail

urlpatterns = [
    path('recipes/', RecipeList.as_view()),
    path('recipes/<int:pk>/', RecipeDetail.as_view()),
   
]
