from django.contrib import admin

from spell.models import Spell


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
	list_display = (
		'name', 'level', 'school', 'text', 'casting_time', 'range', 'materials',
		'components', 'ritual', 'concentration', 'duration', 'source'
	)
	search_fields = ('name', 'source', 'name_en')
