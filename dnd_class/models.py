from django.db import models
from spell.models import Spell
from django.utils.translation import gettext_lazy as _


class DndClass(models.Model):
	name = models.CharField(max_length=255)
	spell_list = models.ManyToManyField(Spell, blank=True, null=True)

	class Meta:
		verbose_name = _('DnD Class')
		verbose_name_plural = _('DnD Classes')

	def __str__(self):
		return self.name
