from django.db import models
from django.utils.translation import gettext_lazy as _


class Spell(models.Model):
	name = models.CharField(max_length=255)
	level = models.IntegerField(blank=True, null=True)
	text = models.TextField(blank=True, null=True)
	school = models.CharField(max_length=255, blank=True, null=True)
	casting_time = models.CharField(max_length=255, blank=True, null=True)
	range = models.CharField(max_length=255, blank=True, null=True)
	materials = models.CharField(max_length=255, blank=True, null=True)
	components = models.CharField(max_length=255, blank=True, null=True)
	duration = models.CharField(max_length=255, blank=True, null=True)
	source = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = _('Spell')
		verbose_name_plural = _('Spells')

	def __str__(self):
		return self.name
