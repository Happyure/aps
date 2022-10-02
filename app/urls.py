from django.urls import path
from.import views

urlpatterns = [
    path('pasien', views.pasien, name='pasien'),
    path('createdatapasien', views.createdatapasien, name='createdatapasien'),
    path('update/<str:id>', views.updatepasien, name='updatepasien'),
    path('dokter', views.dokter, name='dokter'),
    path('createdatadokter', views.createdatadokter, name='createdatadokter'),
    path('update/<str:id>', views.updatedokter, name='updatedokter'),
    path('delete/<str:id>', views.deletedokter, name='deletedokter'),
    path('pendaftaran', views.pendaftaran, name='pendaftaran'),
    path('createdatapendaftaran', views.createdatapendaftaran, name='createdatapendaftaran'),
]