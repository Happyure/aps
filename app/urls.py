from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('components', views.comp, name='components'),

    path('pasien', views.pasien, name='pasien'),
    path('createdatapasien', views.createdatapasien, name='createdatapasien'),
    path('updatepasien/<str:id>', views.updatepasien, name='updatepasien'),
    path('deletepasien/<str:id>', views.deletepasien, name='deletepasien'),

    path('dokter', views.dokter, name='dokter'),
    path('createdatadokter', views.createdatadokter, name='createdatadokter'),
    path('updatedokter/<str:id>', views.updatedokter, name='updatedokter'),
    path('deletedokter/<str:id>', views.deletedokter, name='deletedokter'),
    
    path('pendaftaran', views.pendaftaran, name='pendaftaran'),
    path('deletependaftaran/<str:id>', views.deletependaftaran, name='deletependaftaran'),
    
    path('pelayanan', views.pelayanan, name='pelayanan'),
    path('deletepelayanan/<str:id>', views.deletepelayanan, name='deletepelayanan'),

    path('detailpelayanan', views.detailpelayanan, name='detailpelayanan'),
    path('deletedetailpelayanan/<str:id>', views.deletedetailpelayanan, name='deletedetailpelayanan'),

    path('pasienx', views.pasien, name='pasienx'),
    path('updatepasien/<str:id>', views.updatepasien, name='updatepasienx'),
    path('createdatapasienx', views.createdatapasien, name='createdatapasienx'),

    path('dokterx', views.dokter, name='dokterx'),
    path('createdatadokterx', views.createdatadokter, name='createdatadokterx'),
    path('updatedokter/<str:id>', views.updatedokter, name='updatedokterx'),

    path('pelayananx', views.pelayanan, name='pelayananx'),
    path('createdatapelayananx', views.createdatapelayanan, name='createdatapelayananx'),
    path('updatepelayanan/<str:id>', views.updatepelayanan, name='updatepelayananx'),
    
    path('pendaftaranx', views.pendaftaran, name='pendaftaranx'),
    path('createdatapendaftaranx', views.createdatapendaftaran, name='createdatapendaftaranx'),
    path('updatependaftaran/<str:id>', views.updatependaftaran, name='updatependaftaranx'),

    path('detailpelayananx', views.detailpelayanan, name='detailpelayananx'),
    path('createdatadetailpelayananx', views.createdatadetailpelayanan, name='createdatadetailpelayananx'),
    path('updatedetailpelayanan/<str:id>', views.updatedetailpelayanan, name='updatedetailpelayananx'),

    path('laporan',views.laporan,name='laporan'),
    path('laporanpdf/<str:mulai>/<str:akhir>',views.laporanpdf,name='laporanpdf'),

    path('nota/<str:id>/', views.nota, name='nota'),
    # path('pdf',views.pdfgen),
]