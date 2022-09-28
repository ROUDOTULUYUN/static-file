from django.shortcuts import render

# Create your views here.
def prodi8(request):
    judul = ["TEKNIK INDUSTRI", "TEKNIK SIPIL", "TEKNIK KIMIA", "TEKNIK MESIN", "TEKNIK ELEKTRO", "TEKNIK METALURGI", "INFORMATIKA"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'ft.html', konteks)


