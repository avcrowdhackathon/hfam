# Generated by Django 3.0.5 on 2020-04-04 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hfamAPI', '0009_auto_20200404_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='disease',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disease_of', to='hfamAPI.Disease'),
        ),
    ]
