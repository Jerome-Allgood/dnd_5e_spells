from rest_framework	 import serializers
from spell.models import Spell


class SpellRuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Spell
		fields = ('id', 'name', 'level', 'school', 'text', 'casting_time',
		          'range', 'components', 'materials', 'duration', 'ritual',
		          'concentration')
