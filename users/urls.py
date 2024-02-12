from django.urls import path
from . import views

app_name = 'users'  # Django app naming (namespacing)

urlpatterns = [
    path('<int:pk>/', views.user_detail, name='user_detail'),
    path('new/', views.user_create, name='user_create'),
    path('<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),
]
