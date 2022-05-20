print('Penghitung Harga Barang\n'
      '=======================')
tb = int(input('Masukan Jumlah Barang   : '))
hb = int(input('Masukan Harga Barang    : '))
th = 0
for i in range(tb):
    th += hb
    print(f'Harga Barang ke {i+1} Total Harga : {th}')