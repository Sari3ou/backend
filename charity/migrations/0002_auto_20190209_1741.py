# Generated by Django 2.0.9 on 2019-02-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='necessiteux',
            name='date_de_naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='necessiteux',
            name='pointure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='necessiteux',
            name='taille',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
