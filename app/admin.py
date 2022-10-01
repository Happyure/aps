from django.contrib import admin
from.import models
# Register your models here.

admin.site.register(models.dokter)
admin.site.register(models.pasien)
admin.site.register(models.pendaftaran)
admin.site.register(models.pelayanan)
admin.site.register(models.detailpelayanan)