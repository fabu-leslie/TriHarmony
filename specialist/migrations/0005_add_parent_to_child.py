# Generated by Django 4.1.5 on 2023-01-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0004_remove_parent_child_behavior_behavior1_details_and_more'),
    ]

    operations = [
        migrations.AddField(
        model_name='child',
        name='parent',
        field=models.ForeignKey(null=True, on_delete=models.CASCADE, to='specialist.Parent'),
    ),
    ]
