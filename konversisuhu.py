print('====Konversi Suhu====')
print('A.Celcius')
print('B.Reamur')
print('C.Fahrenheit')
print('D.Kelvin')
print('====================')
s = input('Pilih Suhu Yang ingin Di Konversi : ')
if (s == 'A') or (s == 'a'):
    c = float(input('Input Suhu Celcius : '))
    r = 4/5*c
    f = 9/5*c+32
    k = c+273
    print(c,'Celcius ke Reamur      : ',r)
    print(c,'Celcius ke Fahrenheit  : ',f)
    print(c,'Celcius ke Kelvin      : ',k)
elif (s == 'B') or (s == 'b'):
    r = float(input('Input Suhu Reamur : '))
    c = 5/4*r
    f = 9/4*r+32
    k = 5/4*r+273
    print(r,'Reamur ke Celcius      : ',c)
    print(r,'Reamur ke Fahrenheit   : ',f)
    print(r,'Reamur ke Kelvin       : ',k)
elif (s == 'C') or (s == 'c'):
    f = float(input('Input Suhu Fahrenheit : '))
    c = 5/9*(f-32)
    r = 4/9*(f-32)
    k = c+273
    print(f,'Fahrenheit ke Celcius      : ',c)
    print(f,'Fahrenheit ke Reamur       : ',r)
    print(f,'Fahrenheit ke Kelvin       : ',k)
elif (s == 'D') or (s == 'd'):
    k = float(input('Input Kelvin : '))
    c = k-273
    f = 9/5*c+32
    r = 4/5*(k-273)
    print(k,'Kelvin ke Celcius      : ',c)
    print(k,'Kelvin ke Fahrenheit   : ',f)
    print(k,'Kelvin ke Reamur       : ',r)
else:
    print('Satuan Suhu Tidak Ditemukan!')
