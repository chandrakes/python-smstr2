print('Program Menghitung Nilai\n'
      '==========================')
nama= input('Input Nama Mahasiswa   : ')
nim = input('Input NIM Mahasiswa    : ')
tg  = int(input('Input Nilai Tugas      : '))
uts = int(input('Input Nilai UTS        : '))
uas = int(input('Input Nilai UAS        : '))
nt  = (tg*0.2)+(uts*0.4)+(uas*0.4)
print('==========================\n'
      f'Nama Mahasiswa   : {nama}\n'
      f'NIM Mahasiswa    : {nim}\n'
      f'Nilai Total Anda : {nt:.1f}')
if nt > 80:
    print('Grade Anda       : A\n' 
          'Keterangan       : Lulus')
elif (nt <= 80) and (nt > 70):
    print('Grade Anda       : B\n' 
          'Keterangan       : Lulus')
elif (nt <= 70) and (nt > 40):
    print('Grade Anda       : C\n' 
          'Keterangan       : Lulus')
elif nt <= 40:
    print('Grade Anda       : D\n' 
          'Keterangan       : Tidak Lulus')