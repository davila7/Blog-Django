from django.db import models
from django.template.defaultfilters import slugify



class Entrada(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Entrada, self).save(*args, **kwargs)
