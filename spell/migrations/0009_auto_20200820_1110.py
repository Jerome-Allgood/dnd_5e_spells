# Generated by Django 3.1 on 2020-08-20 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spell', '0008_remove_spell_components'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='test_components',
            new_name='components',
        ),
    ]
