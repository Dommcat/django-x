from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, HomePageView, AboutPageView
from .models import Snack




class HomePageView(HomePageView):
    template_name = "snack/home.html"
    model = Snack
    context_object_name = 'Home_snack_tracking_project'

class AboutPageView(AboutPageView):
    template_name = "snack/about.html"
    model = Snack

class SnackListView(ListView):
    template_name = 'snack/list.html'
    model = Snack
    context_object_name = 'snack_tracking_project'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
    context_object_name = 'detail_snack_tracking_project'
    
class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snacks/snack_create.html'
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snacks/snack_update.html'
    fields = ['title', 'purchaser', 'description']

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snacks/snack_delete.html'
    success_url = '/'


