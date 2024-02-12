from django.urls import path
from . import views

app_name = 'games'  # Django app naming (namespacing)

urlpatterns = [
    path('<int:gameID>/', views.game_detail, name='game_detail'),
    path('new/', views.game_create, name='game_create'),
    path('<int:gameID>/edit/', views.game_edit, name='game_edit'),
    path('<int:gameID>/delete/', views.game_delete, name='game_delete'),
    path('user/<int:user_id>/games/', views.user_games, name='user_games'),
]
