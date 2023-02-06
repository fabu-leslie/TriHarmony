# Generated by Django 4.1.5 on 2023-02-06 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0002_child_is_child_parent_is_parent_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'permissions': (('view_client_child', 'Can view child'),)},
        ),
        migrations.AlterModelOptions(
            name='parent',
            options={'permissions': (('view_client_parent', 'Can view parent'),)},
        ),
        migrations.AlterModelOptions(
            name='specialist',
            options={'permissions': (('view_client_specialist', 'Can view specialist'),)},
        ),
    ]