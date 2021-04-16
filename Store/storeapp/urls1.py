from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.producator_form,name='producator_insert'),
    path('<int:id>/',views.producator_form,name='producator_update'),
    path('delete/<int:id>/',views.producator_delete,name='producator_delete'),
    path('list/',views.producator_list,name='producator_list')
]
