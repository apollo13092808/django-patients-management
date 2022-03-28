from django.urls import path
from app import views


urlpatterns = [
    path('', views.frontend, name='frontend'),
    path('backend/', views.backend, name='backend'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('edit-patient/', views.edit_patient, name='edit_patient'),
    path('delete-patient/<str:id>/', views.delete_patient, name='delete_patient'),
    path('patient/<str:id>/', views.patient, name='patient'),
]
