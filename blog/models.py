from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime 

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)


class Entrada(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	slug = models.SlugField(max_length=200, editable=False)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True, default=datetime.now)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True, default=datetime.now)

	objects = EntryQuerySet.as_manager()

	class Meta:
		verbose_name = "Entrada"
		verbose_name_plural = "Entradas"
		ordering = ["-created"]

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Entrada, self).save(*args, **kwargs)