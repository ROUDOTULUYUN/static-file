from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = ["Ilmu Pemerintahan", "Administrasi Publik", "Ilmu Komunikasi"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fisip.html', konteks)