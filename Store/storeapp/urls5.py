from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vanzari_form,name='vanzari_insert'),
    path('<int:id>/',views.vanzari_form,name='vanzari_update'),
    path('delete/<int:id>/',views.vanzari_delete,name='vanzari_delete'),
    path('list/',views.vanzari_list,name='vanzari_list')
]
