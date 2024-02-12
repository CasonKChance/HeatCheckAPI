from django.urls import path
from .views import UserRetrieveUpdateDestroy, UserCreate, UserListCreate


app_name = 'users'  # Django app naming (namespacing)

urlpatterns = [
    path('<int:pk>/', UserRetrieveUpdateDestroy.as_view(),
         name='user-retrieve-update-destroy'),
    path('', UserListCreate.as_view(), name='user-list-create'),
    path('create/', UserCreate.as_view(), name='user_create'),
]
