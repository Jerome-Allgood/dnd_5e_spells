from django.urls import path, include
from spell.api.views import SpellListView

urlpatterns = [
	path('api/spells/', SpellListView.as_view()),
]