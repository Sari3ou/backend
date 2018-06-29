# Generated by Django 2.0.3 on 2018-05-01 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AideRecu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_reception', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500, unique=True)),
                ('surnom', models.CharField(blank=True, max_length=100, unique=True)),
                ('telephone', models.CharField(max_length=20, unique=True)),
                ('telephone_2', models.CharField(blank=True, max_length=20)),
                ('address', models.TextField()),
                ('website', models.CharField(blank=True, max_length=500)),
                ('facebook', models.CharField(blank=True, max_length=500)),
                ('youtube', models.CharField(blank=True, max_length=500)),
                ('commune', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='Besoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('est_urgent', models.BooleanField(default=False)),
                ('date_limite', models.DateField()),
                ('montant', models.IntegerField(default=0)),
                ('date_planification', models.DateField()),
                ('date_remise_don', models.DateField(blank=True, null=True)),
                ('besoin_satisfait', models.BooleanField(default=False)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.Association')),
            ],
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('associations', models.ManyToManyField(to='charity.Association')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.CentreType')),
            ],
        ),
        migrations.CreateModel(
            name='Donneur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('est_active', models.BooleanField(default=False)),
                ('anonyme', models.BooleanField(default=True)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.Association')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.DonneurType')),
            ],
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('nombre_enfant', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Necessiteux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('prenom', models.CharField(max_length=100)),
                ('date_de_naissance', models.DateField()),
                ('sexe', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('tel', models.CharField(max_length=20)),
                ('pointure', models.IntegerField()),
                ('taille', models.CharField(max_length=100)),
                ('est_orphelin', models.BooleanField()),
                ('represent_famille', models.BooleanField(default=False)),
                ('degre_necessite', models.SmallIntegerField(default=0)),
                ('archive', models.BooleanField(default=False)),
                ('appartient_famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.Famille')),
                ('association', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='charity.Association')),
                ('niveau_scolaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.NiveauScolaire')),
                ('situation_familiale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.SituationFamiliale')),
                ('situation_professionelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.SituationProfessionelle')),
            ],
            options={
                'verbose_name_plural': 'Necessiteux',
            },
        ),
        migrations.AddField(
            model_name='besoin',
            name='necessiteux',
            field=models.ManyToManyField(to='charity.Necessiteux'),
        ),
        migrations.AddField(
            model_name='besoin',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.DonType'),
        ),
    ]