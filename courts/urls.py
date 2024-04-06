from django.urls import path
from .views import CourtListCreate, CourtRetrieveUpdateDestroy, CourtListView, CourtSpecificView

urlpatterns = [
    path('', CourtListCreate.as_view(), name='court-list-create'),
    path('<int:pk>/', CourtRetrieveUpdateDestroy.as_view(),
         name='court-retrieve-update-destroy'),
    path('court-list/', CourtListView.as_view(), name='court-list'),
    path('<int:pk>/detail/', CourtSpecificView.as_view(),
         name='court-specific'),
]
