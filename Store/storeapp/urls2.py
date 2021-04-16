from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.categorie_form,name='categorie_insert'),
    path('<int:id>/',views.categorie_form,name='categorie_update'),
    path('delete/<int:id>/',views.categorie_delete,name='categorie_delete'),
    path('list/',views.categorie_list,name='categorie_list')
]
