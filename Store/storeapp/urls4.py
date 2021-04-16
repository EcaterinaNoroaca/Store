from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.comanda_form,name='comanda_insert'),
    path('<int:id>/',views.comanda_form,name='comanda_update'),
    path('delete/<int:id>/',views.comanda_delete,name='comanda_delete'),
    path('list/',views.comanda_list,name='comanda_list')
]
