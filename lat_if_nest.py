print('Menu Sederhana')
print('1.Minuman')
print('2.Makanan')
u = input('Mau Pilih Menu Apa : ')
if u == '1':
    print('1.Es Teh\n''2.Teh Anget')
    im = input('Silahkan Pilih Minuman : ')
    if im == '1':
        print('Pilihan Anda Es Teh')
    elif im == '2':
        print('Pilihan Anda Teh Anget')
    else:
        print('Menu Tidak Ada')
elif u == '2':
    print('1.Sate\n''2.Bakso')
    imk = input('Silahkan Pilih Makanan : ')
    if imk == '1':
        print('Pilihan Anda Sate')
    elif imk == '2':
        print('Pilihan Anda Bakso')
    else:
        print('Menu Tidak Ada')
else:
    print('Menu Tidak Ada')