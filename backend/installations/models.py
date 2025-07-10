from django.db import models


class Installation(models.Model):
    gid = models.IntegerField(primary_key=True)
    gml_id = models.CharField(max_length=100)
    codeaiot = models.CharField(max_length=100)
    raisonsociale = models.CharField(max_length=255)
    adresse1 = models.CharField(max_length=255, null=True, blank=True)
    codepostal = models.CharField(max_length=20)
    codeinsee = models.CharField(max_length=20)
    commune = models.CharField(max_length=255)
    statutseveso = models.CharField(max_length=100, null=True, blank=True)
    etatactivite = models.CharField(max_length=100, null=True, blank=True)
    regimevigueur = models.CharField(max_length=100)
    serviceaiot = models.CharField(max_length=100)
    siret = models.CharField(max_length=20, null=True, blank=True)
    geo_point_lat = models.FloatField()
    geo_point_lon = models.FloatField()
    bovins = models.BooleanField()
    porcs = models.BooleanField()
    volailles = models.BooleanField()
    carriere = models.BooleanField()
    eolienne = models.BooleanField()
    industrie = models.BooleanField()
    prioritenationale = models.BooleanField()
    ied = models.BooleanField()
    departement = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.raisonsociale} ({self.commune})"
