from django.urls import path
from.import views

urlpatterns = [
    path('pasien', views.pasien, name='pasien'),
    path('createdatapasien', views.createdatapasien, name='createdatapasien'),
    path('updatepasien/<str:id>', views.updatepasien, name='updatepasien'),

    path('dokter', views.dokter, name='dokter'),
    path('createdatadokter', views.createdatadokter, name='createdatadokter'),
    path('updatedokter/<str:id>', views.updatedokter, name='updatedokter'),
    path('deletedokter/<str:id>', views.deletedokter, name='deletedokter'),
    
    path('pendaftaran', views.pendaftaran, name='pendaftaran'),
    path('createdatapendaftaran', views.createdatapendaftaran, name='createdatapendaftaran'),
    
    path('pelayanan', views.pelayanan, name='pelayanan'),
    path('createdatapelayanan', views.createdatapelayanan, name='createdatapelayanan'),
    path('updatepelayanan/<str:id>', views.updatepelayanan, name='updatepelayanan'),
    path('deletepelayanan/<str:id>', views.deletepelayanan, name='deletepelayanan'),
]