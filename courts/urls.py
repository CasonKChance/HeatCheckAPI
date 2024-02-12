from django.urls import path
from .views import CourtListCreate, CourtRetrieveUpdateDestroy

app_name = 'courts'  # Django app naming (namespacing)

urlpatterns = [
    path('', CourtListCreate.as_view(), name='court-list-create'),
    path('<int:pk>/', CourtRetrieveUpdateDestroy.as_view(),
         name='court-retrieve-update-destroy'),
]
