from django.urls import path
from .views import GameListCreate, GameRetrieveUpdateDestroy

app_name = 'games'  # Django app naming (namespacing)

urlpatterns = [
    path('', GameListCreate.as_view(), name='game-list-create'),
    path('<int:pk>/', GameRetrieveUpdateDestroy.as_view(),
         name='game-retrieve-update-destroy'),
]
