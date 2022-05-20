num = int(input('Masukan Bilangan : '))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,'Bukan bilangan prima')
            print(i,'Kali',num//i,'=',num)
            break
    else:
        print(num,'Adalah bilangan prima')
else:
    print(num,'Bukan Bilangan prima')