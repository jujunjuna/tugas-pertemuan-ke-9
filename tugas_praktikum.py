print("tugas pertemuan ke 9")
print("Nama\t: Jujun Junaedi \nNIM\t: 312110568 \nKelas\t: TI21C5")
data ={}
while True:
    c = input("tambahkan data? y/t :  ")
    if (c.lower() == 'y'):
        print("tambah data mahasiswa baru")
        nama = input('masukan nama : ')
        nim = input('masukan nim : ')
        nilai_tugas = int(input('masukan nilai tugas : '))
        nilai_uts = int(input('masukan nilai uts : '))
        nilai_uas = int(input('masukan nilai uas : '))
        nilai_akhir = (0.30 * nilai_tugas) + (0.30 * nilai_uts) + (0.30 * nilai_uas)
        data[nama]= nim, nilai_tugas, nilai_uts,nilai_uas,nilai_akhir
        print("\ndata berhasil ditambahkan")
    elif (c.lower() == 't'):                                                                    
        if data.items():                                                                     
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")
