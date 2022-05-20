menu = 0
while menu != 9:
    print('Menu : \n'
          '1.Makanan\n'
          '2.Minuman')
    dmenu = int(input('Silahkan Pilih Menu : '))
    if dmenu == 1:
        print('Bakso\n'
              'Mie Ayam')
        menu = int(input('Ketik 0 untuk ke home, 9 untuk keluar :'))
    elif dmenu == 2:
        print('es jeruk\n'
              'es teh')
        menu = int(input('Ketik 0 untuk ke home, 9 untuk keluar :'))
    else:
        print('Menu Tidak Ada')
else:
    print('Anda Keluar Dari Menu ')