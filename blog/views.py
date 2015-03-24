from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView
from .models import Entrada

class IndexView(ListView):
	
	template_name = 'entrada_list.html'
	model = Entrada

class EntradaDetailView(DetailView):

	template_name = 'entrada_detail.html'
	model = Entrada

def LogOut(request):
	logout(request)
	return redirect('/')
