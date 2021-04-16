from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProduseForm(forms.ModelForm):

    class Meta:
        model = Produse
        fields = '__all__'
        labels = {
            'data_expirarii' : 'Data Expirării',
            'data_producerii' : 'Data Producerii',
            'pret' : 'Preț',
            'producator' : 'Producător',
            'nume_produs' : 'Nume Produs'
        }

    def __init__(self, *args, **kwargs):
        super(ProduseForm,self).__init__(*args, **kwargs)
        self.fields['categorie'].empty_label = "Selectează Categoria"
        self.fields['producator'].empty_label = "Selectează Producătorul"

class ProducatorForm(forms.ModelForm):

    class Meta:
        model = Producator
        fields = '__all__'
        labels = {
            'nume_producator' : 'Nume Producător',
            'tara_origine' : 'Țara de origine',
            'adresa_fiscala' : 'Adresa Fiscală',
            'cod_fiscal' : 'Cod Fiscal',
            'numar_contact' : 'Număr de contact'
        }

    def __init__(self, *args, **kwargs):
        super(ProducatorForm,self).__init__(*args, **kwargs)



class CategorieForm(forms.ModelForm):

    class Meta:
        model = Categorie
        fields = '__all__'
        labels = {
            'nume_categorie' : 'Nume Categorie'
        }

    def __init__(self, *args, **kwargs):
        super(CategorieForm,self).__init__(*args, **kwargs)


class FurnizorForm(forms.ModelForm):

    class Meta:
        model = Furnizor
        fields = '__all__'
        labels = {
            'nume_furnizor' : 'Nume Furnizor',
            'adresa_fiscala' : 'Adresa Fiscală',
            'cod_fiscal' : 'Cod Fiscal'
        }

    def __init__(self, *args, **kwargs):
        super(FurnizorForm,self).__init__(*args, **kwargs)


class ComandaForm(forms.ModelForm):

    class Meta:
        model = Comanda
        fields = '__all__'
        labels = {
            'furnizor' : 'Furnizor',
            'suma_comanda' : 'Suma',
            'produs' : 'Produs',
            'data_comanda' : 'Data',
            'cantitate' : 'Cantitate',
            'unitate_masura' : 'Unitatea de măsură'
        }

    def __init__(self, *args, **kwargs):
        super(ComandaForm,self).__init__(*args, **kwargs)
        self.fields['furnizor'].empty_label = "Selectează Furnizorul"
        self.fields['produs'].empty_label = "Selectează Produsul"



class VanzariForm(forms.ModelForm):

    class Meta:
        model = Vanzari
        fields = '__all__'
        labels = {
            'suma_vanzare' : 'Suma',
            'produs' : 'Produs',
            'data_vanzarii' : 'Data',
            'cantitate' : 'Cantitate',
            'unitate_masura' : 'Unitatea de măsură'
        }

    def __init__(self, *args, **kwargs):
        super(VanzariForm,self).__init__(*args, **kwargs)
        self.fields['produs'].empty_label = "Selectează Produsul"


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = '__all__'
        labels = {
            'denumire' : 'Denumirea Job-ului'
        }

    def __init__(self, *args, **kwargs):
        super(JobForm,self).__init__(*args, **kwargs)



class AngajatForm(forms.ModelForm):

    class Meta:
        model = Angajat
        fields = '__all__'
        labels = {
            'nume' : 'Nume',
            'prenume' : 'Prenume',
            'job' : 'Job',
            'data_angajarii' : 'Data Angajării',
            'nr_contract' : 'Nr. Contractului'
        }

    def __init__(self, *args, **kwargs):
        super(AngajatForm,self).__init__(*args, **kwargs)
        self.fields['job'].empty_label = "Selectează Job-ul"


class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['table']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


