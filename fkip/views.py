from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judul = ["S1 Pendidikan Matematika", "S1 Pendidikan Kimia", "S1 Pendidikan Fisika", "S1 Pendidikan Luar Sekolah", "S1 Pendidikan Guru Sekolah Dasar", "S1 Pendidikan Anak Usia Dini", "S1 Pendidikan Bahasa Indonesia", "S1 Pendidikan Bahasa Inggris", "S1 Pendidikan Bimbingan dan Konseling", "S1 Pendidikan Biologi", "S1 Pendidikan Luar Biasa", "S1 Pendidikan Sendratasik", "S1 Pendidikan Kewarganegaraan", "S1 Pendidikan Sejarah", "S1 Pendidikan Sosiologi", "S1 Pendidikan IPA", "S1 Pendidikan Teknik Elektro", "S1 Pendidikan Teknik Mesin"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fkip.html', konteks)