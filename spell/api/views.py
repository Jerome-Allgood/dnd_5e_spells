from rest_framework import generics
from spell.models import Spell
from spell.api.serializers import SpellRuSerializer


class SpellListView(generics.ListAPIView):
	queryset = Spell.objects.all()
	serializer_class = SpellRuSerializer
