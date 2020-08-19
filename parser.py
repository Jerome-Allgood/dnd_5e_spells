import json
from spell.models import Spell

with open('DnD5e_spells_BD.dtn', encoding='utf-8-sig') as file:
	json_data = json.load(file)

print(json_data['allSpells'][0]['en'].keys())
print(json_data)