import json
from django.core.management import BaseCommand
from spell.models import Spell


class Command(BaseCommand):
	def handle(self, *args, **options):
		with open('DnD5e_spells_BD.dtn', encoding='utf-8-sig') as file:
			json_data = json.load(file)

		print(json_data['allSpells'][0]['ru'].keys())
		for spell in json_data['allSpells']:
			if not Spell.objects.filter(name=spell['ru']['name']).exists():
				Spell.objects.create(
					name=spell['ru']['name'],
					level=spell['ru']['level'] if 'level' in spell['ru'] else None,
					text=spell['ru']['text'],
					school=spell['ru']['school'] if 'school' in spell['ru'] else None,
					casting_time=spell['ru']['castingTime'] if 'castingTime' in spell['ru'] else None,
					materials=spell['ru']['materials'] if 'materials' in spell['ru'] else None,
					components=spell['ru']['components'] if 'components' in spell['ru'] else None,
					duration=spell['ru']['duration'] if 'materials' in spell['ru'] else None,
					source=spell['ru']['source'] if 'source' in spell['ru'] else None,
					range=spell['ru']['range'] if 'range' in spell['ru'] else None,
					name_en=spell['en']['name'].capitalize(),
					text_en=spell['en']['text'],
					materials_en=spell['en']['materials'] if 'materials' in spell['en'] else None,

				)
				print(f'Spell <{spell["ru"]["name"]}> added.')
