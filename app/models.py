from django.db import models

# Create your models here.
class dokter(models.Model):
    iddokter = models.AutoField(primary_key=True)
    namadokter = models.CharField(max_length=50)
    nohpdokter = models.IntegerField()

    def __str__(self):
        return str(self.iddokter)

class pasien(models.Model):
    idpasien = models.AutoField(primary_key=True)
    namapasien = models.CharField(max_length=50)
    jeniskelaminpasien = models.CharField(max_length=15)
    tanggallahir = models.DateField()
    nohppasien = models.IntegerField()

    def __str__(self):
        return str(self.idpasien)

class pendaftaran(models.Model):
    idpendaftaran = models.AutoField(primary_key=True)
    iddokter = models.ForeignKey(dokter,on_delete=models.CASCADE)
    idpasien = models.ForeignKey(pasien,on_delete=models.CASCADE)
    tanggalpendaftaran = models.DateField()

    def __str__(self):
        return str(self.idpendaftaran)

class pelayanan(models.Model):
    idpelayanan = models.AutoField(primary_key=True)
    jenispelayanan = models.CharField(max_length=50)
    hargapelayanan = models.IntegerField()

    def __str__(self):
        return str(self.idpelayanan)

class detailpelayanan(models.Model):
    iddetailpelayanan = models.AutoField(primary_key=True)
    idpendaftaran = models.ForeignKey(pendaftaran,on_delete=models.CASCADE)
    idpelayanan = models.ForeignKey(pelayanan,on_delete=models.CASCADE)
    jumlahjenispelayanan = models.IntegerField()

    def __str__(self):
        return str(self.iddetailpelayanan)

