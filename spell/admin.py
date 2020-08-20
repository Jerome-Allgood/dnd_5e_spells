from django.contrib import admin

from spell.models import Spell


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
	list_display = (
		'name', 'name_en', 'level', 'school', 'text', 'casting_time',
		'range', 'materials', 'materials_en', 'components', 'ritual',
		'concentration', 'duration', 'source'
	)
	search_fields = ('name', 'source', 'name_en')
	fields = (
		'name', 'name_en', 'level', 'school', 'text', 'text_en', 'casting_time',
		'range', 'components', 'materials', 'materials_en',
		('ritual', 'concentration'), 'duration', 'source'
	)
