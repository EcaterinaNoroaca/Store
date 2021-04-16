from django.db import models
from datetime import datetime,date

# Create your models here.
class Producator(models.Model):
    nume_producator = models.CharField(max_length=20,blank=False)
    tara_origine = models.CharField(max_length=20)
    adresa_fiscala = models.CharField(max_length=50)
    cod_fiscal = models.CharField(max_length=13)
    numar_contact = models.IntegerField(max_length=15)

    def __str__(self):
        return self.nume_producator


class Categorie(models.Model):
    nume_categorie = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.nume_categorie


class Producator_Categorie(models.Model):
    producator = models.ForeignKey(Producator,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)

class Produse(models.Model):
    nume_produs = models.CharField(max_length=30,blank=False)
    data_producerii = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    data_expirarii = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    pret = models.FloatField(max_length=10)
    barcode = models.CharField(max_length=13)
    detalii = models.CharField(max_length=50)
    producator = models.ForeignKey(Producator,on_delete=models.CASCADE, null=True)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nume_produs

class Furnizor(models.Model):
    nume_furnizor = models.CharField(max_length=20,blank=False)
    adresa_fiscala = models.CharField(max_length=50)
    cod_fiscal = models.CharField(max_length=13)

    def __str__(self):
        return self.nume_furnizor

class Comanda(models.Model):
    furnizor = models.ForeignKey(Furnizor,on_delete=models.CASCADE)
    produs = models.ForeignKey(Produse,on_delete=models.CASCADE)
    suma_comanda = models.FloatField(max_length=10)
    data_comanda = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    cantitate = models.FloatField(max_length=10)
    unitate_masura = models.CharField(max_length=15)

class Vanzari(models.Model):
    suma_vanzare = models.FloatField(max_length=10)
    data_vanzarii = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    cantitate = models.FloatField(max_length=10)
    unitate_masura = models.CharField(max_length=15)
    produs = models.ForeignKey(Produse,on_delete=models.CASCADE)

class Job(models.Model):
    denumire = models.CharField(max_length=20,blank=False)
    def __str__(self):
        return self.denumire

class Angajat(models.Model):
    nume = models.CharField(max_length=15,blank=False)
    prenume = models.CharField(max_length=15,blank=False)
    data_angajarii = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    nr_contract = models.IntegerField(max_length=25)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)   

TABLES = (
    ('produse','produse'),
    ('producator', 'producator'),
    ('categorie','categorie'),
    ('furnizor','furnizor'),
    ('comanda','comanda'),
    ('vanzari','vanzari'),
    ('job','job'),
    ('angajat','angajat'),
)

class Tables(models.Model):
  table = models.CharField(max_length=10, choices=TABLES, default='produse')
