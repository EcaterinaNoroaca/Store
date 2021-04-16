from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.angajat_form,name='angajat_insert'),
    path('<int:id>/',views.angajat_form,name='angajat_update'),
    path('delete/<int:id>/',views.angajat_delete,name='angajat_delete'),
    path('list/',views.angajat_list,name='angajat_list')
]
