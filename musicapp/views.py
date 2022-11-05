from django.views.generic import ListView

from .models import Artiste


class MusicappListView(ListView):
    model = Artiste
    template_name = "musicapp_list.html"

# Create your views here.
