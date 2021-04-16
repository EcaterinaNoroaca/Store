from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
#   --------------------------------------  Produse ------------------------------------------------

@login_required(login_url='login')
def produse_list(request):
    context = {'produse_list': Produse.objects.all()}
    return render(request,"storeapp/produse_list.html",context)

@login_required(login_url='login')
def produse_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form = ProduseForm()
          
       else:
            produs = Produse.objects.get(pk=id)
            form = ProduseForm(instance=produs)

       return render(request,"storeapp/produse_form.html",{'form':form})
    else:
       if id == 0:

           form = ProduseForm(request.POST)
       else:
           produs = Produse.objects.get(pk=id)
           form = ProduseForm(request.POST,instance=produs)

       if form.is_valid():
           form.save()   
       else:
           return render(request,"storeapp/produse_form.html",{'form':form})     
       return redirect('/produse/list')

@login_required(login_url='login')
def produse_delete(request, id):
    produs = Produse.objects.get(pk=id)
    produs.delete()
    return redirect('/produse/list') 
#   --------------------------------------  Producator ------------------------------------------------
@login_required(login_url='login')
def producator_list(request):
    context1 = {'producator_list': Producator.objects.all()}
    return render(request,"storeapp/producator_list.html",context1)

@login_required(login_url='login')
def producator_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form1 = ProducatorForm()
          
       else:
            producator = Producator.objects.get(pk=id)
            form1 = ProducatorForm(instance=producator)

       return render(request,"storeapp/producator_form.html",{'form1':form1})
    else:
       if id == 0:

           form1 = ProducatorForm(request.POST)
       else:
           producator = Producator.objects.get(pk=id)
           form1 = ProducatorForm(request.POST,instance=producator)

       if form1.is_valid():
           form1.save()   
       else:
           return render(request,"storeapp/producator_form.html",{'form1':form1})     
       return redirect('/producator/list')

@login_required(login_url='login')
def producator_delete(request, id):
    producator = Producator.objects.get(pk=id)
    producator.delete()
    return redirect('/producator/list') 
#   --------------------------------------  Categorie ---------------------------------------------------
@login_required(login_url='login')
def categorie_list(request):
    context2 = {'categorie_list': Categorie.objects.all()}
    return render(request,"storeapp/categorie_list.html",context2)

@login_required(login_url='login')
def categorie_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form2 = CategorieForm()
          
       else:
            categorie = Categorie.objects.get(pk=id)
            form2 = CategorieForm(instance=categorie)

       return render(request,"storeapp/categorie_form.html",{'form2':form2})
    else:
       if id == 0:

           form2 = CategorieForm(request.POST)
       else:
           categorie = Categorie.objects.get(pk=id)
           form2 = CategorieForm(request.POST,instance=categorie)

       if form2.is_valid():
           form2.save()   
       else:
           return render(request,"storeapp/categorie_form.html",{'form2':form2})     
       return redirect('/categorie/list')

@login_required(login_url='login')
def categorie_delete(request, id):
    categorie = Categorie.objects.get(pk=id)
    categorie.delete()
    return redirect('/categorie/list') 
#   --------------------------------------  Furnizor ---------------------------------------------------
@login_required(login_url='login')
def furnizor_list(request):
    context3 = {'furnizor_list': Furnizor.objects.all()}
    return render(request,"storeapp/furnizor_list.html",context3)

@login_required(login_url='login')
def furnizor_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form3 = FurnizorForm()
          
       else:
            furnizor = Furnizor.objects.get(pk=id)
            form3 = FurnizorForm(instance=furnizor)

       return render(request,"storeapp/furnizor_form.html",{'form3':form3})
    else:
       if id == 0:

           form3 = FurnizorForm(request.POST)
       else:
           furnizor = Furnizor.objects.get(pk=id)
           form3 = FurnizorForm(request.POST,instance=furnizor)

       if form3.is_valid():
           form3.save()   
       else:
           return render(request,"storeapp/furnizor_form.html",{'form3':form3})     
       return redirect('/furnizor/list')

@login_required(login_url='login')
def furnizor_delete(request, id):
    furnizor = Furnizor.objects.get(pk=id)
    furnizor.delete()
    return redirect('/furnizor/list') 
#   --------------------------------------  Comanda ---------------------------------------------------
@login_required(login_url='login')
def comanda_list(request):
    context4 = {'comanda_list': Comanda.objects.all()}
    return render(request,"storeapp/comanda_list.html",context4)

@login_required(login_url='login')
def comanda_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form4 = ComandaForm()
          
       else:
            comanda = Comanda.objects.get(pk=id)
            form4 = ComandaForm(instance=comanda)

       return render(request,"storeapp/comanda_form.html",{'form4':form4})
    else:
       if id == 0:

           form4 = ComandaForm(request.POST)
       else:
           comanda = Comanda.objects.get(pk=id)
           form4 = Comanda(request.POST,instance=comanda)

       if form4.is_valid():
           form4.save()   
       else:
           return render(request,"storeapp/comanda_form.html",{'form4':form4})     
       return redirect('/comanda/list')

@login_required(login_url='login')
def comanda_delete(request, id):
    comanda = Comanda.objects.get(pk=id)
    comanda.delete()
    return redirect('/comanda/list') 
#   --------------------------------------  Vanzari ---------------------------------------------------

@login_required(login_url='login')
def vanzari_list(request):
    context5 = {'vanzari_list': Vanzari.objects.all()}
    return render(request,"storeapp/vanzari_list.html",context5)

@login_required(login_url='login')
def vanzari_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form5 = VanzariForm()
          
       else:
            vanzari = Vanzari.objects.get(pk=id)
            form5 = VanzariForm(instance=vanzari)

       return render(request,"storeapp/vanzari_form.html",{'form5':form5})
    else:
       if id == 0:

           form5 = VanzariForm(request.POST)
       else:
           vanzari = Vanzari.objects.get(pk=id)
           form5 = VanzariForm(request.POST,instance=vanzari)

       if form5.is_valid():
           form5.save()   
       else:
           return render(request,"storeapp/vanzari_form.html",{'form5':form5})     
       return redirect('/vanzari/list')

@login_required(login_url='login')
def vanzari_delete(request, id):
    vanzari = Vanzari.objects.get(pk=id)
    vanzari.delete()
    return redirect('/vanzari/list') 
#   --------------------------------------  Job ---------------------------------------------------
@login_required(login_url='login')
def job_list(request):
    context6 = {'job_list': Job.objects.all()}
    return render(request,"storeapp/job_list.html",context6)

@login_required(login_url='login')
def job_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form6 = JobForm()
          
       else:
            job = Job.objects.get(pk=id)
            form6 = JobForm(instance=job)

       return render(request,"storeapp/job_form.html",{'form6':form6})
    else:
       if id == 0:

           form6 = JobForm(request.POST)
       else:
           job = Job.objects.get(pk=id)
           form6 = JobForm(request.POST,instance=job)

       if form6.is_valid():
           form6.save()   
       else:
           return render(request,"storeapp/job_form.html",{'form6':form6})     
       return redirect('/job/list')

@login_required(login_url='login')
def job_delete(request, id):
    job = Job.objects.get(pk=id)
    job.delete()
    return redirect('/job/list') 
#   --------------------------------------  Angajat ---------------------------------------------------
@login_required(login_url='login')
def angajat_list(request):
    context7 = {'angajat_list': Angajat.objects.all()}
    return render(request,"storeapp/angajat_list.html",context7)

@login_required(login_url='login')
def angajat_form(request, id=0):
    if (request.method == "GET"):
       if id==0: 
          form7 = AngajatForm()
          
       else:
            angajat = Angajat.objects.get(pk=id)
            form7 = AngajatForm(instance=angajat)

       return render(request,"storeapp/angajat_form.html",{'form7':form7})
    else:
       if id == 0:

           form7 = AngajatForm(request.POST)
       else:
           angajat = Angajat.objects.get(pk=id)
           form7 = AngajatForm(request.POST,instance=angajat)

       if form7.is_valid():
           form7.save()   
       else:
           return render(request,"storeapp/angajat_form.html",{'form7':form7})     
       return redirect('/angajat/list')

@login_required(login_url='login')
def angajat_delete(request, id):
    angajat = Angajat.objects.get(pk=id)
    angajat.delete()
    return redirect('/angajat/list') 
#   --------------------------------------  Main ---------------------------------------------------
@login_required(login_url='login')
def main(request):
    return render(request,"storeapp/index.html")     
       

#   --------------------------------------  Login ---------------------------------------------------

def loginPage(request):
     if request.user.is_authenticated:
        return redirect('main')
     else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Username sau password incorect')
        context = {}
        return render(request,"storeapp/login.html",context)     
       

#   --------------------------------------  Register ---------------------------------------------------

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = UserForm()

        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'A fost creat un cont pentru ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request,"storeapp/register.html", context)     
       


#   --------------------------------------  Logout ---------------------------------------------------

def logoutPage(request):
    logout(request)
    return redirect('login')     

