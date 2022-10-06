from django.urls import path
from.import views

urlpatterns = [
    path('home', views.home, name='home'),

    path('pasien', views.pasien, name='pasien'),
    path('createdatapasien', views.createdatapasien, name='createdatapasien'),
    path('updatepasien/<str:id>', views.updatepasien, name='updatepasien'),
    path('deletepasien/<str:id>', views.deletepasien, name='deletepasien'),

    path('dokter', views.dokter, name='dokter'),
    path('createdatadokter', views.createdatadokter, name='createdatadokter'),
    path('updatedokter/<str:id>', views.updatedokter, name='updatedokter'),
    path('deletedokter/<str:id>', views.deletedokter, name='deletedokter'),
    
    path('pendaftaran', views.pendaftaran, name='pendaftaran'),
    path('createdatapendaftaran', views.createdatapendaftaran, name='createdatapendaftaran'),
    path('updatependaftaran/<str:id>', views.updatependaftaran, name='updatependaftaran'),
    path('deletependaftaran/<str:id>', views.deletependaftaran, name='deletependaftaran'),
    
    path('pelayanan', views.pelayanan, name='pelayanan'),
    path('createdatapelayanan', views.createdatapelayanan, name='createdatapelayanan'),
    path('updatepelayanan/<str:id>', views.updatepelayanan, name='updatepelayanan'),
    path('deletepelayanan/<str:id>', views.deletepelayanan, name='deletepelayanan'),

    path('detailpelayanan', views.detailpelayanan, name='detailpelayanan'),
    path('createdatadetailpelayanan', views.createdatadetailpelayanan, name='createdatadetailpelayanan'),
    path('updatedetailpelayanan/<str:id>', views.updatedetailpelayanan, name='updatedetailpelayanan'),
    path('deletedetailpelayanan/<str:id>', views.deletedetailpelayanan, name='deletedetailpelayanan'),
]