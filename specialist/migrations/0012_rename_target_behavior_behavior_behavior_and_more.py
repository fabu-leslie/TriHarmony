# Generated by Django 4.1.2 on 2023-02-02 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0011_rename_behavior_behaviorcheckin_target_behavior'),
    ]

    operations = [
        migrations.RenameField(
            model_name='behavior',
            old_name='target_behavior',
            new_name='behavior',
        ),
        migrations.RenameField(
            model_name='behavior',
            old_name='target_behavior_details',
            new_name='behavior_details',
        ),
        migrations.RenameField(
            model_name='behaviorcheckin',
            old_name='target_behavior',
            new_name='behavior',
        ),
    ]