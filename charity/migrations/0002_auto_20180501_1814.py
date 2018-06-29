# Generated by Django 2.0.3 on 2018-05-01 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('charity', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='responsable',
            field=models.ForeignKey(limit_choices_to=('profile', 2), null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aiderecu',
            name='association',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.Association'),
        ),
        migrations.AddField(
            model_name='aiderecu',
            name='donneur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.Donneur'),
        ),
        migrations.AddField(
            model_name='aiderecu',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.DonType'),
        ),
    ]