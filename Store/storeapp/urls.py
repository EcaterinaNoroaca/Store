from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.produse_form,name='produse_insert'),
    path('<int:id>/',views.produse_form,name='produse_update'),
    path('delete/<int:id>/',views.produse_delete,name='produse_delete'),
    path('list/',views.produse_list,name='produse_list')
]
