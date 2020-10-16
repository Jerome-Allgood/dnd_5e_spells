import json
from django.core.management import BaseCommand
from spell.models import Spell, Component


class Command(BaseCommand):
	def handle(self, *args, **options):
		with open('DnD5e_spells_BD.dtn', encoding='utf-8-sig') as file:
			json_data = json.load(file)

		print(json_data['allSpells'][0]['ru'].keys())
		for spell in json_data['allSpells']:
			print(f"Start work on <{spell['ru']['name']}>")

			spell_components = []
			if not Spell.objects.filter(name=spell['ru']['name']).exists():
				Spell.objects.create(
					name=spell['ru']['name'],
					level=spell['ru']['level'] if 'level' in spell['ru'] else None,
					text=spell['ru']['text'],
					casting_time=spell['ru']['castingTime'] if 'castingTime' in spell['ru'] else None,
					materials=spell['ru']['materials'] if 'materials' in spell['ru'] else None,
					duration=spell['ru']['duration'] if 'materials' in spell['ru'] else None,
					source=spell['ru']['source'] if 'source' in spell['ru'] else None,
					range=spell['ru']['range'] if 'range' in spell['ru'] else None,
					name_en=spell['en']['name'].capitalize(),
					text_en=spell['en']['text'],
					materials_en=spell['en']['materials'] if 'materials' in spell['en'] else None,
				)

				for school in Spell.Schools.choices:
					if spell['en']['school'] in school:
						print(school[0])
						temp_spell = Spell.objects.get(name=spell['ru']['name'])
						temp_spell.school = school[0]
						temp_spell.save()

				if 'components' in spell['en']:
					for i in spell['en']['components'].split(','):
						if len(i.strip()) > 1:
							for x in i.strip().split():
								if x in ['V', 'M', 'S']:
									spell_components.append(x)
								elif x == '8':
									spell_components.append('S')
						elif i.strip() == '8':
							spell_components.append('S')
						else:
							spell_components.append(i.strip())
				for component in spell_components:
					Spell.objects.get(name=spell['ru']['name']).components.add(
						Component.objects.get(name=component)
					)

				print(f'Spell <{spell["ru"]["name"]}> added.')
