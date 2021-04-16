from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.furnizor_form,name='furnizor_insert'),
    path('<int:id>/',views.furnizor_form,name='furnizor_update'),
    path('delete/<int:id>/',views.furnizor_delete,name='furnizor_delete'),
    path('list/',views.furnizor_list,name='furnizor_list')
]
