from django.contrib import admin

from spell.models import Spell


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
	pass
