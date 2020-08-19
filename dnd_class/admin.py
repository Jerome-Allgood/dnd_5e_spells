from django.contrib import admin


from dnd_class.models import DndClass


@admin.register(DndClass)
class DndClassAdmin(admin.ModelAdmin):
	pass
