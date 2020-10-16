from rest_framework	 import serializers
from spell.models import Spell, Component


class ComponentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Component
		fields = ('name', )


class SpellRuSerializer(serializers.ModelSerializer):
	components = ComponentSerializer(read_only=True, many=True)

	class Meta:
		model = Spell
		fields = (
			'id', 'name', 'level', 'school', 'text', 'casting_time', 'range',
			'components', 'materials', 'duration', 'ritual', 'concentration'
		)
