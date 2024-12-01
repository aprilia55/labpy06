# Daftar untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambah data mahasiswa
def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    nilai = input("Masukkan nilai mahasiswa: ")
    mahasiswa = {"NIM": nim, "Nama": nama, "Nilai": nilai}
    data_mahasiswa.append(mahasiswa)
    print("Data berhasil ditambahkan!")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_data():
    if len(data_mahasiswa) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        print("\nData Mahasiswa:")
        print("{:<15} {:<20} {:<10}".format("NIM", "Nama", "Nilai"))
        print("-" * 50)
        for mahasiswa in data_mahasiswa:
            print("{:<15} {:<20} {:<10}".format(mahasiswa["NIM"], mahasiswa["Nama"], mahasiswa["Nilai"]))

# Fungsi untuk mengubah data mahasiswa
def ubah_data():
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
    ditemukan = False
    for mahasiswa in data_mahasiswa:
        if mahasiswa["NIM"] == nim:
            ditemukan = True
            print("Data ditemukan!")
            mahasiswa["Nama"] = input("Masukkan nama baru: ")
            mahasiswa["Nilai"] = input("Masukkan nilai baru: ")
            print("Data berhasil diubah!")
            break
    if not ditemukan:
        print("Data tidak ditemukan!")

# Fungsi untuk menghapus data mahasiswa
def hapus_data():
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    ditemukan = False
    for mahasiswa in data_mahasiswa:
        if mahasiswa["NIM"] == nim:
            ditemukan = True
            data_mahasiswa.remove(mahasiswa)
            print("Data berhasil dihapus!")
            break
    if not ditemukan:
        print("Data tidak ditemukan!")

# Menu utama
def menu():
    while True:
        print("\nMenu:")
        print("T. Tambah Data")
        print("M. Menampilkan Data")
        print("U. Ubah Data")
        print("H. Hapus Data")
        print("S. Selesai")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program
menu()
