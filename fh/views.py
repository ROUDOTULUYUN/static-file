from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judul = ['Ilmu Hukum']

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fh.html', konteks)

