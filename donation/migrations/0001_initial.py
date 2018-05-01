# Generated by Django 2.0.3 on 2018-05-01 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500, unique=True)),
                ('surnom', models.CharField(blank=True, max_length=100, unique=True)),
                ('tel1', models.CharField(max_length=20, unique=True)),
                ('tel2', models.CharField(blank=True, max_length=20)),
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
                ('planification_date', models.DateField()),
                ('giving_date', models.DateField(blank=True, null=True)),
                ('is_don_given', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BesoinType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('associations', models.ManyToManyField(to='donation.Association')),
            ],
        ),
        migrations.CreateModel(
            name='CentreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Don',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuer', models.TextField()),
                ('recieving_date', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Donneur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('est_active', models.BooleanField(default=False)),
                ('should_be_anonyme', models.BooleanField(default=True)),
                ('tel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DonneurType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresse', models.CharField(max_length=500)),
                ('nombre_enfant', models.SmallIntegerField(default=0)),
                ('association', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='donation.Association')),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('date_de_naissance', models.DateField()),
                ('tel', models.CharField(max_length=20)),
                ('pointure', models.IntegerField()),
                ('taille', models.CharField(blank=True, max_length=100)),
                ('est_orphelin', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Nécessiteux',
            },
        ),
        migrations.CreateModel(
            name='NiveauScolaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('order', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SituationFamiliale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SituationProfessionelle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Necessiteux',
            fields=[
                ('individual_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='donation.Individual')),
                ('nom', models.CharField(max_length=500)),
                ('degree_de_necissite', models.SmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Nécessiteux',
            },
            bases=('donation.individual',),
        ),
        migrations.AddField(
            model_name='individual',
            name='association',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='donation.Association'),
        ),
        migrations.AddField(
            model_name='individual',
            name='niveau_scolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.NiveauScolaire'),
        ),
        migrations.AddField(
            model_name='individual',
            name='sexe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Gender'),
        ),
        migrations.AddField(
            model_name='individual',
            name='situation_familiale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.SituationFamiliale'),
        ),
        migrations.AddField(
            model_name='individual',
            name='situation_professionelle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.SituationProfessionelle'),
        ),
        migrations.AddField(
            model_name='family',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.Individual'),
        ),
        migrations.AddField(
            model_name='donneur',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.DonneurType'),
        ),
        migrations.AddField(
            model_name='don',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.DonType'),
        ),
        migrations.AddField(
            model_name='centre',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.CentreType'),
        ),
        migrations.AddField(
            model_name='besoin',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.BesoinType'),
        ),
        migrations.AddField(
            model_name='besoin',
            name='necessiteux',
            field=models.ManyToManyField(to='donation.Necessiteux'),
        ),
    ]
