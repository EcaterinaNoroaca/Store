from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.job_form,name='job_insert'),
    path('<int:id>/',views.job_form,name='job_update'),
    path('delete/<int:id>/',views.job_delete,name='job_delete'),
    path('list/',views.job_list,name='job_list')
]
