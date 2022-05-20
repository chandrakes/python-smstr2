a = int(input('Masukan Nilai Awal  : '))
b = int(input('Masukan Nilai Akhir : '))
for i in range (a,b):
    if i%2==0:
        print(i,' Adalah Genap')
    else:
        print(i,'Adalah Ganjil')