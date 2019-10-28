from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from datetime import date
from base.models import Commune, NiveauScolaire, SituationFamiliale, SituationProfessionelle, CentreType, \
    DonType, DonneurType
from staff.models import Membre, Association


class Famille(models.Model):
    nom = models.CharField(max_length=500)
    nombre_enfant = models.SmallIntegerField(default=0, blank=True, null=True)
    archivé = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.nom)


class Centre(models.Model):
    nom = models.CharField(max_length=500)
    address = models.TextField()
    type = models.ForeignKey(CentreType, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.nom, self.type)


class Necessiteux(models.Model):
    association = models.ForeignKey(Association, null=True, on_delete=models.SET_NULL, related_name="members")
    nom = models.CharField(max_length=500)
    prenom = models.CharField('prénom', max_length=100)
    jeune_fille = models.CharField('Nom de jeune fille', max_length=100, blank=True, null=True)
    part_de = models.CharField('De la part de', max_length=100, blank=True, null=True)
    nin = models.CharField('Numéro pièce d’identité', max_length=9, blank=True, null=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    sexe = models.CharField(max_length=1, choices=[("F", "Female"), ("M", "Male")])
    type = models.SmallIntegerField(default=0,
                                    choices=[(0, 'Permanent'), (1, 'Temporaire'), (2, 'Voyageur en détresse')])
    niveau_scolaire = models.ForeignKey(NiveauScolaire, on_delete=models.SET_NULL, blank=True, null=True)
    tel = models.CharField('Téléphone 1', max_length=20, blank=True, null=True)
    tel_2 = models.CharField('Téléphone 2', max_length=20, blank=True, null=True)
    pointure = models.IntegerField(null=True)  # TODO validation 20 - 50
    taille = models.CharField(max_length=100, null=True)
    pointure = models.IntegerField(blank=True, null=True, default=36,
                                   validators=[
                                       MaxValueValidator(50),
                                       MinValueValidator(20)
                                   ])
    taille = models.CharField(max_length=100, blank=True, null=True)
    situation_familiale = models.ForeignKey(SituationFamiliale, on_delete=models.SET_NULL, null=True)
    situation_professionelle = models.ForeignKey(SituationProfessionelle, on_delete=models.SET_NULL, null=True)
    health_state =  models.SmallIntegerField('état de santé', default=0,
                                               choices=[(0, 'En bonne santé'), (1, 'Malade'), (2, 'Maladie chronique')])
    est_orphelin = models.BooleanField()
    degré_nécessite = models.SmallIntegerField(default=0,
                                               choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    appartient_famille = models.ForeignKey(Famille, verbose_name='appartient-il à une famille?', on_delete=models.SET_NULL, blank=True, null=True)
    represent_famille = models.BooleanField('représente-il une famille?', default=False)
    archivé = models.BooleanField(default=False)
    investigated = models.BooleanField('investigation effectuée?', default=False)
    other_infos = models.TextField('informations supplémentaires',  blank=True, null=True)

    def get_need(self):
        needs_qs = Besoin.objects.filter(necessiteux=self.id).values_list('nom', flat=True)
        return list(needs_qs)

    def get_age(self):
        today = date.today()
        date_naissance = self.date_de_naissance
        if date_naissance is None:
            return None
        return today.year - date_naissance.year - (
                (today.month, today.day) < (date_naissance.month, date_naissance.day))

    class Meta:
        verbose_name_plural = "Nécessiteux"
        verbose_name = "Nécessiteux"

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)


class Besoin(models.Model):
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    necessiteux = models.ManyToManyField(Necessiteux, null=True, blank=True)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(DonType, on_delete=models.CASCADE)
    est_urgent = models.BooleanField(default=False)
    date_limite = models.DateField(blank=True, null=True)
    expire_le = models.DateField(blank=True, null=True)
    montant = models.IntegerField(default=0, null=True, blank=True)
    date_planification = models.DateField(blank=True, null=True)
    date_remise_don = models.DateField(blank=True, null=True)
    est_satisfait = models.BooleanField(default=False)
    délivré_par = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nom)


class Donneur(models.Model):
    association = models.ForeignKey(Association, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=100)
    tel = models.CharField(max_length=20, null=True, blank=True)
    type = models.ForeignKey(DonneurType, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=False)
    anonyme = models.BooleanField(default=True)

    def __str__(self):
        return "{} ({})".format(self.nom, self.type)


class AideRecu(models.Model):
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    donneur = models.ForeignKey(Donneur, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(DonType, on_delete=models.SET_NULL, null=True)
    date_reception = models.DateField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Aide reçu"
        verbose_name_plural = "Aides reçus"

    def __str__(self):
        return "Don #{} ({})".format(self.id, self.type)
