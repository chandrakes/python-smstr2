print('Penghitung Harga Barang\n'
      '=======================')
tb = int(input('Masukan Jumlah Barang   : '))
hb = int(input('Masukan Harga Barang    : '))
th = 0
for i in range(tb):
    if i+1 == 3:
        th += hb*0.5
        print(f'Harga Barang ke {i+1} Diskon 50%  : {hb*0.5}')
        print(f'Harga Barang ke {i+1} Total Harga : {th}')
    else:
        th += hb
        print(f'Harga Barang ke {i+1} Total Harga : {th}')