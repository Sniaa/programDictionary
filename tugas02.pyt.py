#semangat ya ingat kamu punya mimpi yang begitu banyak dan ini adalah awalnya

#tugas 01
print("============================")
print("+NAMA : SONIA TARANDARI    +")
print("+NIM  : SI19220032         +")
print("+PRODI: SI(Sistem Informasi+")
print("============================")

list_nilai = [1,2,3,4,5,6,7,8,9,10]

print("==============================================================")
print("+                        TUGAS NO 1                          +")
print("==============================================================")
print("+ list               : ",list_nilai,"     +")
print("+ jumlah index       : ",len(list_nilai),"                                  +")
print("+ jumlah nilai       : ",list_nilai.count(list_nilai),"                                   +")
list_nilai.append(11)
print("+ tambah nilai       : ", list_nilai," +")
list_nilai.insert(4,97)
list_nilai.pop(11)
print("+ insert             : ",list_nilai," +")
list_nilai.pop(4)
list_nilai.pop(2)
list_nilai.append(3)
print("+ perpindahan nilai  : ",list_nilai,"     +")
list_nilai.pop(0)
list_nilai.pop(0)
list_nilai.pop(7)
list_nilai.insert(0,3)
print("+ menghilangkan nilai: ",list_nilai,"           +")
list_nilai.insert(0,1)
list_nilai.insert(1,2)
list_nilai.pop(6)
list_nilai.append(7)
print("+ 7 trakhir          : ",list_nilai,"     +")
print("==============================================================")
print("+                      TUGAS NO 2                            +")
print("+                  BIODATA MAHASISWA                         +")
print("==============================================================")

#tugas dictionary

mhs  = {
    "nama" : "laila linta",
    "alamat":"bogor",
    "gender":"perempuan",
    "n_kalkulus"  :90,
    "n_manajement": 80,
    "jaringan":70,
}
print('nama       : ',mhs.get('nama'))
print('asal       : ',mhs.get('alamat'))
print('gender     : ',mhs.get('gender'))
print('kalkulus   : ',mhs.get('n_kalkulus'))
print('manajement : ',mhs.get('n_manajement'))
print('jaringan   : ',mhs.get('jaringan'))
print("==============================================================")

mhs2  = {
    "nama" : "mutia lalain",
    "alamat":"bogor",
    "gender":"perempuan",
    "n_kalkulus"  :90,
    "n_manajement": 70,
    "jaringan":95,
}
print('nama       : ',mhs2.get('nama'))
print('asal       : ',mhs2.get('alamat'))
print('gender     : ',mhs2.get('gender'))
print('kalkulus   : ',mhs2.get('n_kalkulus'))
print('manajement : ',mhs2.get('n_manajement'))
print('jaringan   : ',mhs2.get('jaringan'))
print("==============================================================")

mhs3  = {
    "nama" : "aldinataro",
    "alamat":"bandung",
    "gender":"laki-laki",
    "n_kalkulus"  :70,
    "n_manajement": 90,
    "jaringan":95,
}
print('nama       : ',mhs3.get('nama'))
print('asal       : ',mhs3.get('alamat'))
print('gender     : ',mhs3.get('gender'))
print('kalkulus   : ',mhs3.get('n_kalkulus'))
print('manajement : ',mhs3.get('n_manajement'))
print('jaringan   : ',mhs3.get('jaringan'))
print("==============================================================")

mhs4  = {
    "nama" : "salsatralala",
    "alamat":"lampung",
    "gender":"perempuan",
    "n_kalkulus"  :80,
    "n_manajement":90,
    "jaringan":85,
}
print('nama       : ',mhs4.get('nama'))
print('asal       : ',mhs4.get('alamat'))
print('gender     : ',mhs4.get('gender'))
print('kalkulus   : ',mhs4.get('n_kalkulus'))
print('manajement : ',mhs4.get('n_manajement'))
print('jaringan   : ',mhs4.get('jaringan'))
print("==============================================================")

mhs5  = {
    "nama" : "lintang prabudi",
    "alamat":"lampung",
    "gender":"laki-laki",
    "n_kalkulus"  :95,
    "n_manajement":75,
    "jaringan":95,
}
print('nama       : ',mhs5.get('nama'))
print('asal       : ',mhs5.get('alamat'))
print('gender     : ',mhs5.get('gender'))
print('kalkulus   : ',mhs5.get('n_kalkulus'))
print('manajement : ',mhs5.get('n_manajement'))
print('jaringan   : ',mhs5.get('jaringan'))
print("==============================================================")
print("+                        Terimakasih                         +")
print("==============================================================")




