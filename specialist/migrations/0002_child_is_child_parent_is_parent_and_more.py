# Generated by Django 4.1.5 on 2023-02-06 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('specialist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='parent',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='specialist',
            name='is_specialist',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='child',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]