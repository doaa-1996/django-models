from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,ListView,DetailView
from .models import Snack

class HomeView(TemplateView):
  template_name='home.html'

class SnackView(ListView):
    template_name='snacks.html'
    model=Snack


class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack    