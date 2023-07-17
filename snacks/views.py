from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class SnackListView(ListView):
    template_name ='snacks_list.html'
    model = Snack
class SnackDetailView(DetailView):
    template_name ='snacks_detail.html'
    model = Snack
class SnackCreateView(ListView):
    template_name='snack_create.html'
    model=Snack
    fields= ['title', 'purchaser', 'description'] 
class SnackUpdateView(UpdateView): 
    template_name='snack_update.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snacks_list')   
class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snacks_list')