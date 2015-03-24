from django.contrib import admin
from .models import Entrada
from django_markdown.admin import MarkdownModelAdmin


@admin.register(Entrada)
class EntradaAdmin(MarkdownModelAdmin):
	list_display = ("titulo", "created")
	propopulated_fields = {"slug":("titulo",)}


