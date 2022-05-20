bil = int(input('Masukan Jumlah Bilangan : '))
for i in range(bil):
    b = int(input('Input Bilangan : '))
    if b > 0 :
        print(b,' Adalah Nilai Positif')
    elif b == 0:
        print(b,' Adalah Nilai 0')
    elif b < 0 :
        print(b,' Adalah Nilai Negatif') 