from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judul = ["S1 Pendidikan Dokter", "S1 Keperawatan", "S1 Gizi", "S1 Ilmu Keolahragaan", "D3 Keperawatan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fk.html', konteks)