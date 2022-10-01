from django.shortcuts import render

# Create your views here.
def index(request) :
    allpasienobj = models.pasien.objects.all()
    getpasienobj = models.pasien.get(idpasien = 1)
    filterpasienobj = models.pasien.objects.filter(jeniskelamin = 'Laki-Laki')

    return render(request, 'pasien.html',{
        'allpasienobj' : allpasienobj,
        'getpasienobj' : getpasienobj,
        'filterpasienobj' : filterpasienobj
    })

def createdata(request):
    if request.method == 'GET' :
        return render(request, 'createdata.html')
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
        return redirect('index')