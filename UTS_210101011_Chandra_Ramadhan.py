"""
Nama    : Chandra Ramadhan
NIM     : 210101011
Kelas   : SI 21 A1
"""
print('Program Pasien Sederhana\n'
      '========================')
kpasien = input    ('Masukan Kode Pasien   : ')
kkamar  = int(input('Masukan Kode Kamar    : '))
hari    = int(input('Berapa Hari Menginap  : '))
kdokter = input    ('Masukan Kode Dokter   : ')
print('=======================')
if kpasien == 'RS001':
    status = 'Pasien Baru'
    bdaftar = 400000
elif kpasien == 'RS002':
    status = 'Pasien Lama'
    bdaftar = 300000
elif kpasien == 'RS003':
    status = 'Pasien BPJS'
    bdaftar = 200000
elif kpasien == 'RS004':
    status = 'Pasien Akses'
    bdaftar = 100000
else:
    status = 'Kode Pasien Tidak Ada'
    bdaftar = 0

if kkamar == 1111:
    nkamar = 'Kamar Anggrek'
    bkamar = 1000000
elif kkamar == 2222:
    nkamar = 'Kamar Melati'
    bkamar = 2000000
elif kkamar == 3333:
    nkamar = 'Kamar Mawar'
    bkamar = 3000000
elif kkamar == 4444:
    nkamar = 'Kamar Tulip'
    bkamar = 4000000
elif kkamar == 5555:
    nkamar = 'Kamar Tulip'
    bkamar = 5000000
else:
    nkamar = 'Kode Kamar Tidak Ada'
    bkamar = 0

if kdokter == 'DK001':
    ndokter = 'Dr.Budi'
    bperiksa = 500000
elif kdokter == 'DK002':
    ndokter = 'Dr.Ari'
    bperiksa = 500000
elif kdokter == 'DK003':
    ndokter = 'Dr.Andi'
    bperiksa = 500000
elif kdokter == 'DK004':
    ndokter = 'Dr.Rudi'
    bperiksa = 600000
elif kdokter == 'DK005':
    ndokter = 'Dr.Agus'
    bperiksa = 700000
else:
    ndokter = 'Kode Dokter Tidak Ada'
    bperiksa = 0

if hari > 15:
    bkamarbaru = bkamar*hari
    diskonkamar = bkamarbaru*0.5
    pdis   = '50%'
elif hari > 10 and hari <= 15:
    bkamarbaru = bkamar*hari
    diskonkamar = bkamarbaru*0.4
    pdis   = '40%'
elif hari > 6 and hari <= 10:
    bkamarbaru = bkamar*hari
    diskonkamar = bkamarbaru*0.3
    pdis   = '30%'
elif hari > 3 and hari <= 6:
    bkamarbaru = bkamar*hari
    diskonkamar = bkamarbaru*0.2
    pdis   = '20%'
elif hari > 1 and hari <= 3:
    bkamarbaru = bkamar*hari
    diskonkamar = bkamarbaru*0.1
    pdis   = '10%'
totalb = bdaftar+bkamarbaru+bperiksa-diskonkamar

print(f'Status Pasien       : {status}')
print(f'Biaya Daftar Pasien : Rp.{bdaftar}')
print(f'Nama Kamar          : {nkamar}')
print(f'Biaya Kamar         : {hari} Hari x Rp.{bkamar} = Rp.{bkamarbaru}')
print(f'Nama Dokter         : {ndokter}')
print(f'Biaya Pemeriksaan   : Rp.{bperiksa}')
print(f'Diskon Biaya Kamar  : {diskonkamar} / {pdis}')
print(f'Total Pembayaran    : Rp.{totalb}')