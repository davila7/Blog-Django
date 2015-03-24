from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entrada

class IndexView(ListView):
	
	template_name = 'entrada_list.html'
	model = Entrada

class EntradaDetailView(DetailView):

	template_name = 'entrada_detail.html'
	model = Entrada

