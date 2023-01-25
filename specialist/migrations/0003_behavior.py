# Generated by Django 4.1.5 on 2023-01-25 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0002_child_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Behavior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behavior1', models.CharField(max_length=255)),
                ('behavior1_intensity', models.IntegerField()),
                ('behavior1_frequency', models.IntegerField()),
                ('behavior2', models.CharField(max_length=255)),
                ('behavior2_intensity', models.IntegerField()),
                ('behavior2_frequency', models.IntegerField()),
                ('behavior3', models.CharField(max_length=255)),
                ('behavior3_intensity', models.IntegerField()),
                ('behavior3_frequency', models.IntegerField()),
                ('notes', models.CharField(max_length=255)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialist.child')),
            ],
        ),
    ]