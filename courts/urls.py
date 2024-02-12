from django.urls import path
from . import views

app_name = 'courts'  # Django app naming (namespacing)

urlpatterns = [
    path('available/', views.available_courts, name='available_courts'),
    path('<int:courtID>/', views.court_detail, name='court_detail'),
    path('new/', views.court_create, name='court_create'),
    path('<int:courtID>/edit/', views.court_edit, name='court_edit'),
    path('<int:courtID>/delete/', views.court_delete, name='court_delete'),
]
