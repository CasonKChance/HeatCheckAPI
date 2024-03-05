from django.urls import path
from .views import UserRetrieveUpdateDestroy, UserListCreate
from .views import UserRegistrationView, UserLoginView


app_name = 'users'  # Django app naming (namespacing)

urlpatterns = [
    path('<int:pk>/', UserRetrieveUpdateDestroy.as_view(),
         name='user-retrieve-update-destroy'),
    path('', UserListCreate.as_view(), name='user-list-create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]
