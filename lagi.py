#membuat tabel data base
pelanggan=[]
alamat=[]

def masukPelanggan():
    pelangganBaru= input("masukkan nama pelanggan=")
    pelanggan.append(pelangganBaru)
    alamatBaru= input("masukkan alamat pelanggan = ")
    alamat.append(alamatBaru)

#sub program tampilkan data dibuat oleh siha
def tampilkanData():
    print("data base pelanggan adalah :")
    for i in range (0, len(pelanggan)):
        print('no pelanggan', i, "nama pelanggan", pelanggan[i],"alamat:",alamat[i])


#program utama dibuat oleh karin
jawaban = input ("apakah anda ingin memasukkan data pelanggan ? (ya/tidak)")
while jawaban == "ya":
    masukPelanggan()
    jawaban = input ("apakah anda ingin memasukkan data pelanggan ? (ya/tidak)")

masukPelanggan()
tampilkanData()
