from django.shortcuts import render

# Create your views here.
def prodi3(request):
    judul = ["S1 Managemen" "S1 Akuntansi", "S1 Ilmu Ekonomi Pembangunan", "S1 Ekonomi Syariah", "D3 Akuntansi", "D3 Marketing", "D3 Perpajakan", "D3 Keuangan Perbankan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'feb.html', konteks)

