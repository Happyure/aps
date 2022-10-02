from datetime import datetime
from django.shortcuts import redirect, render
from . import models

# Pasien
def pasien(request) :
    allpasienobj = models.pasien.objects.all()
    getpasienobj = models.pasien.objects.get(idpasien = 1)
    filterpasienobj = models.pasien.objects.filter(jeniskelaminpasien = 'Laki-Laki')

    return render(request, 'pasien.html',{
        'allpasienobj' : allpasienobj,
        'getpasienobj' : getpasienobj,
        'filterpasienobj' : filterpasienobj
    })

def createdatapasien(request):
    if request.method == 'GET' :
        return render(request, 'createdatapasien.html')
    else :
        namapasien = request.POST['namapasien']
        tanggallahir = request.POST['tanggallahir']
        jeniskelaminpasien = request.POST['jeniskelaminpasien']
        nohppasien = request.POST['nohppasien']

        newpasien = models.pasien(
            namapasien = namapasien,
            tanggallahir = tanggallahir,
            jeniskelaminpasien = jeniskelaminpasien,
            nohppasien = nohppasien
        ).save()
        return redirect('pasien')

def updatepasien(request,id):
    pasienobj=models.pasien.objects.get(idpasien=id)
    tanggal=datetime.strftime(pasienobj.tanggallahir, '%Y-%m-%d')
    if request.method=='GET':
        return render(request,'updatepasien.html',{
            'pasien':pasienobj,
            'tanggallahir':tanggal
        })
    else:
        pasienobj.namapasien = request.POST['namapasien']
        pasienobj.tanggallahir = request.POST['tanggallahir']
        pasienobj.jeniskelaminpasien = request.POST['jeniskelaminpasien']
        pasienobj.nohppasien = request.POST['nohppasien']
        pasienobj.save()
        return redirect('pasien')

# Dokter
def dokter(request):
    alldokterobj = models.dokter.objects.all()

    return render(request, 'dokter.html',{
        'alldokterobj' : alldokterobj,
    })

def createdatadokter(request):
    if request.method == 'GET' :
        return render(request, 'createdatadokter.html')
    else :
        namadokter = request.POST['namadokter']
        nohpdokter = request.POST['nohpdokter']

        newdokter = models.dokter(
            namadokter = namadokter,
            nohpdokter = nohpdokter
        ).save()
        return redirect('dokter')

def updatedokter(request,id):
    dokterobj=models.dokter.objects.get(iddokter=id)
    if request.method=='GET':
        return render(request,'updatedokter.html',{
            'dokter':dokterobj,
        })
    else:
        dokterobj.namadokter = request.POST['namadokter']
        dokterobj.nohpdokter = request.POST['nohpdokter']
        dokterobj.save()
        return redirect('dokter')

def deletedokter(request,id):
    dokterobj=models.dokter.objects.get(iddokter=id)
    dokterobj.delete()
    return redirect('dokter')

# Pendaftaran Sik error
def pendaftaran(request):
    allpendaftaranobj = models.dokter.objects.all()

    return render(request, 'pendaftaran.html',{
        'allpendaftaranobj' : allpendaftaranobj,
    })

def createdatapendaftaran(request):
    if request.method == 'GET' :
        return render(request, 'createdatapendaftaran.html')
    else :
        tanggalpendaftaran = request.POST['tanggalpendaftaran']

        newpendaftaran = models.pendaftaran(
            tanggalpendaftaran=tanggalpendaftaran,
        ).save()
        return redirect('pendaftaran')

# Pelayanan
