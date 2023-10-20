n = '0'
total = 0
tampung = 0
while (n != ''):
     n = str(input('masukkan nilai: '))
     tampung += 1
     if(n == ''):
         break;
     elif (n == 'A'):
         print('nilai= 4')
         total += 4 
     elif (n == 'A-'):
         print('nilai = 3.75')
         total +3.75 
     elif (n == 'B+'):
         print('nilai = 3.50')
         total +3.50
     elif (n == 'B'):
         print('nilai = 3.00')
         total +3.00
     elif (n == 'B-'):
         print('nilai = 2.75')
         total +2.75
     elif (n == 'C+'):
         print('nilai = 2.50')
         total +2.50
     elif (n == 'C'):
         print('nilai = 2.00')
         total +2.00
     elif (n == 'C-'):
         print('nilai = 1.75')
         total +1.75
     elif (n == 'D'):
         print('nilai = 1.50')
         total +1.50
     elif (n == 'E'):
         print('nilai = 1.25')
         total +1.25
     else:
          tampung -= 1 
          print("masukkan nilai yang benar")
if(tampung== 1): 
    print("rata-rata nya adalah: 0")
else:
    rerata = total/tampung-1
    print("rata-rata nya adalah :",rerata)