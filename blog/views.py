from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView
from . import models

class IndexView(ListView):
	
	template_name = 'entrada_list.html'
	queryset = models.Entrada.objects.published()
	paginate_by = 3

class EntradaDetailView(DetailView):

	template_name = 'entrada_detail.html'
	model = models.Entrada

def Logout(request):
	logout(request)
	return redirect('/')
