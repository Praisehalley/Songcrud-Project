from django.urls import path
from .import views


urlpatterns = [
    path('song/', views.SongAPIView.as_view()),
    path('artiste/', views.ArtisteAPIView.as_view()),

]
