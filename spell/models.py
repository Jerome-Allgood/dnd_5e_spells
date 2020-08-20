from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField


class Spell(models.Model):
	class Components(models.TextChoices):
		VERBAL = 'V', _('Verbal')
		SOMATIC = 'S', _('Somatic')
		MATERIAL = 'M', _('Material')

	class Schools(models.TextChoices):
		ILLUSION = 'IL', _('Illusion')
		ENCHANTMENT = 'EN', _('Enchantment')
		DIVINATION = 'DV', _('Divination')
		NECROMANCY = 'NC', _('Necromancy')
		EVOCATION = 'EV', _('Evocation')
		CONJURATION = 'CN', _('Conjuration')
		TRANSMUTATION = 'TR', _('Transmutation')
		ABJURATION = 'AB', _('Abjuration')

	name = models.CharField(max_length=255)
	level = models.IntegerField(blank=True, null=True)
	text = models.TextField(blank=True, null=True)
	school = models.CharField(choices=Schools.choices, max_length=2, blank=True,
							  null=True)
	casting_time = models.CharField(max_length=255, blank=True, null=True)
	range = models.CharField(max_length=255, blank=True, null=True)
	materials = models.CharField(max_length=255, blank=True, null=True)
	duration = models.CharField(max_length=255, blank=True, null=True)
	source = models.CharField(max_length=255, blank=True, null=True)
	ritual = models.BooleanField(default=False, blank=True, null=True)
	concentration = models.BooleanField(default=False, blank=True, null=True)
	name_en = models.CharField(max_length=255, blank=True, null=True)
	text_en = models.TextField(blank=True, null=True)
	materials_en = models.CharField(max_length=255, blank=True, null=True)
	components = MultiSelectField(
		choices=Components.choices, max_length=7, max_choices=3, null=True,
		blank=True
	)

	class Meta:
		verbose_name = _('Spell')
		verbose_name_plural = _('Spells')

	def __str__(self):
		return self.name
