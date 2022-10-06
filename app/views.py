from datetime import datetime
from pyexpat import model
from django.shortcuts import redirect, render
from . import models

# Home
def home(request):
    allpasienobj = models.pasien.objects.all()
    alldokterobj = models.dokter.objects.all()
    allpendaftaranobj = models.pendaftaran.objects.all()
    allpelayananobj = models.pelayanan.objects.all()
    alldetailpelayananobj = models.detailpelayanan.objects.all()

    return render(request, 'home.html',{
        'allpasienobj':allpasienobj,
        'alldokterobj':alldokterobj,
        'allpendaftaranobj':allpendaftaranobj,
        'allpelayananobj':allpelayananobj,
        'alldetailpelayananobj':alldetailpelayananobj
    })

# Pasien
def pasien(request) :
    allpasienobj = models.pasien.objects.all()
    filterpasienobj = models.pasien.objects.filter(jeniskelaminpasien = 'Laki-Laki')

    return render(request, 'pasien.html',{
        'allpasienobj' : allpasienobj,
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

def deletepasien(request,id):
    pasienobj=models.pasien.objects.get(idpasien=id)
    pasienobj.delete()
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

# Pendaftaran
def pendaftaran(request):
    allpendaftaranobj = models.pendaftaran.objects.all()
    alldokterobj=models.dokter.objects.all()
    allpasienobj=models.pasien.objects.all()

    return render(request, 'pendaftaran.html',{
        'allpendaftaranobj' : allpendaftaranobj,
        'alldokterobj' : alldokterobj,
        'allpasienobj' : allpasienobj,
    })

def createdatapendaftaran(request):
    alldokterobj=models.dokter.objects.all()
    allpasienobj=models.pasien.objects.all()
    if request.method == 'GET' :
        return render(request, 'createdatapendaftaran.html',{
        'alldokterobj' : alldokterobj,
        'allpasienobj':allpasienobj
        })

    else :
        iddokter = request.POST['iddokter']
        getiddokter = models.dokter.objects.get(iddokter=iddokter)
        idpasien = request.POST['idpasien']
        getidpasien = models.pasien.objects.get(idpasien=idpasien)
        tanggalpendaftaran = request.POST['tanggalpendaftaran']

        newpendaftaran = models.pendaftaran(
            iddokter = getiddokter,
            idpasien = getidpasien,
            tanggalpendaftaran=tanggalpendaftaran
        ).save()
        return redirect('pendaftaran')

def updatependaftaran(request,id):
    pendaftaranobj = models.pendaftaran.objects.get(idpendaftaran=id)
    dokterall = models.dokter.objects.all()
    pasienall = models.pasien.objects.all()
    tanggal=datetime.strftime(pendaftaranobj.tanggalpendaftaran, '%Y-%m-%d')
    if request.method=='GET':
        return render(request,'updatependaftaran.html',{
            'pendaftaranobj':pendaftaranobj,
            'dokterall':dokterall,
            'pasienall':pasienall,
            'tanggal':tanggal
        })
    else:
        pendaftaranobj.dokter=request.POST['iddokter']
        dokterbaru=models.dokter.objects.get(iddokter=request.POST['iddokter'])
        pendaftaranobj.iddokter=dokterbaru
        pendaftaranobj.pasien=request.POST['idpasien']
        pasienbaru=models.pasien.objects.get(idpasien=request.POST['idpasien'])
        pendaftaranobj.idpasien=pasienbaru
        pendaftaranobj.tanggalpendaftaran=request.POST['tanggalpendaftaran']
        pendaftaranobj.save()
        return redirect('pendaftaran')

def deletependaftaran(request,id):
    pendaftaranobj=models.pendaftaran.objects.get(idpendaftaran=id)
    pendaftaranobj.delete()
    return redirect('pendaftaran')

# Pelayanan
def pelayanan(request):
    allpelayananobj = models.pelayanan.objects.all()
    filterpelayananobj = models.pelayanan.objects.filter(jenispelayanan = 'Penambalan Gigi')

    return render(request, 'pelayanan.html',{
        'allpelayananobj' : allpelayananobj,
        'filterpelayananobj': filterpelayananobj
    })

def createdatapelayanan(request):
    if request.method == 'GET' :
        return render(request, 'createdatapelayanan.html')
    else :
        jenispelayanan = request.POST['jenispelayanan']
        hargapelayanan = request.POST['hargapelayanan']

        newpelayanan = models.pelayanan(
            jenispelayanan = jenispelayanan,
            hargapelayanan = hargapelayanan
        ).save()
        return redirect('pelayanan')

def updatepelayanan(request,id):
    pelayananobj=models.pelayanan.objects.get(idpelayanan=id)
    if request.method=='GET':
        return render(request,'updatepelayanan.html',{
            'pelayanan':pelayananobj,
        })
    else:
        pelayananobj.jenispelayanan = request.POST['jenispelayanan']
        pelayananobj.hargapelayanan = request.POST['hargapelayanan']
        pelayananobj.save()
        return redirect('pelayanan')

def deletepelayanan(request,id):
    pelayananobj=models.pelayanan.objects.get(idpelayanan=id)
    pelayananobj.delete()
    return redirect('pelayanan')

# Detail Pelayanan
def detailpelayanan(request):
    alldetailpelayananobj = models.detailpelayanan.objects.all()
    allpelayananobj = models.pelayanan.objects.all()
    allpendaftaranobj = models.pendaftaran.objects.all()


    return render(request, 'detailpelayanan.html',{
        'alldetailpelayananobj' : alldetailpelayananobj,
        'allpelayananobj' : allpelayananobj,
        'allpendaftaranobj' : allpendaftaranobj,
    })

def createdatadetailpelayanan(request):
    allpelayananobj = models.pelayanan.objects.all()
    allpendaftaranobj = models.pendaftaran.objects.all()
    if request.method == 'GET' :
        return render(request, 'createdatadetailpelayanan.html',{
        'allpelayananobj' : allpelayananobj,
        'allpendaftaranobj' : allpendaftaranobj
        })
    else :
        idpelayanan = request.POST['idpelayanan']
        getidpelayanan = models.pelayanan.objects.get(idpelayanan=idpelayanan)
        idpendaftaran = request.POST['idpendaftaran']
        getidpendaftaran = models.pendaftaran.objects.get(idpendaftaran=idpendaftaran)
        jumlahjenispelayanan = request.POST['jumlahjenispelayanan']
        
        newdetailpelayanan = models.detailpelayanan(
            idpelayanan = getidpelayanan,
            idpendaftaran = getidpendaftaran,
            jumlahjenispelayanan = jumlahjenispelayanan
        ).save()
        return redirect('detailpelayanan')
    
def updatedetailpelayanan(request,id):
    detailpelayananobj = models.detailpelayanan.objects.get(iddetailpelayanan=id)
    pendaftaranall = models.pendaftaran.objects.all()
    pelayananall = models.pelayanan.objects.all()
    if request.method=='GET':
        return render(request,'updatedetailpelayanan.html',{
            'detailpelayananobj':detailpelayananobj,
            'pendaftaranall': pendaftaranall,
            'pelayananall':pelayananall,
        })
    else:
        detailpelayananobj.pendaftaran=request.POST['idpendafatran']
        pendaftaranbaru=models.pendaftaran.objects.get(idpendaftaran=request.POST['idpelayanan'])
        detailpelayananobj.idpendaftaran=pendaftaranbaru
        detailpelayananobj.pelayanan=request.POST['idpelayanan']
        pelayananbaru=models.pelayanan.objects.get(idpelayanan=request.POST['idpelayanan'])
        detailpelayananobj.idpelayanan=pelayananbaru
        detailpelayananobj.jumlahjenispelayanan = request.POST['jumlahjenispelayanan']
        detailpelayananobj.save()
        return redirect('detailpelayanan')

def deletedetailpelayanan(request,id):
    detailpelayananobj=models.detailpelayanan.objects.get(iddetailpelayanan=id)
    detailpelayananobj.delete()
    return redirect('detailpelayanan')