#membuat list sebanyak 5 element
list = [10,20,25,30,50]
#tampilkan element ke 3
print ('element ke 3 :',list[2])
#ambil nilai element ke 2 sampai ke 4
print('element ke 2 sampe ke 4:',list[1:4])
#ambil element terakhir
print('element ke terakhir :',list[4])

#mengubah element ke 4
list[3]= 100
print('mengubah element ke 4 dari 30 menjadi :',list[3])
#mengubah element ke 4 sampai sampai dengan yang terakhir
list[3:4]= [90,99]
print('mengubah element ke 4 sampai terakhir:',list[3:5])

#menambah element list

a = [1,2,3,4]
#mengambil 2 bagian dari list a
b = a[1:3]
print(b)

#menambah list b dengan nilai string
b.append('mobil')
print(b)

#tambah list b dengan 3 nilai
b.extend([100,200,300])
print(b)

#gabungkan list b dengan list a
c = a + b
print(c)