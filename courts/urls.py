from django.urls import path
from .views import CourtListView, CourtSpecificView

app_name = 'courts'  # Django app naming (namespacing)

urlpatterns = [
    path('', CourtListView.as_view(), name='court_list'),
    path('<int:pk>/', CourtSpecificView.as_view(),
         name='court_specific'),
]
