from django.urls import path

from .views import MusicappListView

urlpatterns = [
    path("", MusicappListView.as_view(), name="home"),

]
