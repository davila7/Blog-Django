from django.contrib import admin
from .models import Entrada
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


@admin.register(Entrada)
class EntradaAdmin(MarkdownModelAdmin):
	list_display = ("titulo", "created")
	propopulated_fields = {"slug":("titulo",)}
	# Next line is a workaround for Python 2.x
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


