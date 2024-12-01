NAMA : Alfarizki Aprilia Putri

NIM : 312410455

Mata Kuliah : Bahasa Pemrograman

# Praktikum 6 - Pengelolaan Data Mahasiswa

Program ini memungkinkan untuk mengelola data nilai mahasiswa dengan fitur-fitur sebagai berikut:

Menambah data mahasiswa baru.

Menampilkan daftar data mahasiswa.

Mengubah data mahasiswa berdasarkan NIM.

Menghapus data mahasiswa berdasarkan NIM.

Keluar dari program.

`Tambah Data`: Menambahkan mahasiswa baru dengan informasi NIM, Nama, dan Nilai.

`Tampilkan Data`: Menampilkan semua data mahasiswa dalam bentuk tabel.

`Ubah Data`: Mengubah informasi mahasiswa seperti nama dan nilai berdasarkan NIM.

`Hapus Data`: Menghapus data mahasiswa berdasarkan NIM.

`Selesai`: Mengakhiri program.

# Cara Menjalankan 

`Pastikan` Python telah terinstal di perangkat Anda.

`Salin kode` program ini ke file Python (misalnya pengelolaan_data_nilai.py).

`Jalankan` file menggunakan terminal atau command prompt dengan perintah:

```python
python pengelolaan_data_nilai.py
```

Pilih menu sesuai kebutuhan dan ikuti instruksi yang muncul.

# Contoh Penggunaan 

**`Menambahkan data`**

``` python
Masukkan nama mahasiswa: Andi
Masukkan NIM mahasiswa: 12345
Masukkan nilai mahasiswa: A
```
**`menampilkan data`**

```python
Data Mahasiswa:
NIM             Nama                Nilai     
-----------------------------------------------
12345           Andi                A         
```

# Penjelasan kode 

1. **Daftar Data Mahasiswa**
   
 ```python
   data_mahasiswa = []
   ```

`data_mahasiswa` adalah list kosong yang digunakan untuk menyimpan data mahasiswa.

`Data mahasiswa` disimpan dalam bentuk `dictionary`, dengan kunci `NIM`, `Nama`, dan `Nilai`.

2. **Fungsi `tambah data()`**

```python
def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    nilai = input("Masukkan nilai mahasiswa: ")
    mahasiswa = {"NIM": nim, "Nama": nama, "Nilai": nilai}
    data_mahasiswa.append(mahasiswa)
    print("Data berhasil ditambahkan!")
```
Fungsi ini digunakan untuk menambahkan data mahasiswa.

Menggunakan fungsi `input()` untuk meminta input dari pengguna mengenai nama, NIM, dan nilai.

Data yang dimasukkan kemudian dimasukkan ke dalam dictionary dengan key `NIM`, `Nama`, dan `Nilai`.

Dictionary tersebut ditambahkan ke dalam list `data_mahasiswa`.

3. **Fungsi `Tampilkan data`**
   
```python
def tampilkan_data():
    if len(data_mahasiswa) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        print("\nData Mahasiswa:")
        print("{:<15} {:<20} {:<10}".format("NIM", "Nama", "Nilai"))
        print("-" * 50)
        for mahasiswa in data_mahasiswa:
            print("{:<15} {:<20} {:<10}".format(mahasiswa["NIM"], mahasiswa["Nama"], mahasiswa["Nilai"]))
```
Fungsi ini digunakan untuk menampilkan seluruh data mahasiswa.

Pertama, program mengecek apakah ada data yang tersimpan menggunakan `len(data_mahasiswa)`. Jika tidak ada data, akan ditampilkan pesan bahwa tidak ada data mahasiswa.

Jika ada data, program akan menampilkan data dalam bentuk tabel menggunakan format string `("{:<15} {:<20} {:<10}")`.

Setiap mahasiswa ditampilkan dengan `NIM`, `Nama`, dan `Nilai` pada baris terpisah.

4. **Fungsi `Ubah data`**

```python
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
```
Fungsi ini digunakan untuk mengubah data mahasiswa berdasarkan NIM.

Program akan meminta input NIM yang ingin diubah.

Fungsi mencari mahasiswa yang NIM-nya cocok menggunakan perulangan `(for)`.

Jika ditemukan, data nama dan nilai mahasiswa dapat diubah.

Jika NIM tidak ditemukan, maka program akan memberi tahu pengguna bahwa data tidak ditemukan.

5. **Fungsi`hapus data`**
   
```python
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
```
Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan NIM.

Program akan meminta input NIM yang ingin dihapus.

Fungsi mencari mahasiswa dengan NIM yang sesuai dan menghapusnya dari list data_mahasiswa.

Jika `data mahasiswa` ditemukan, maka data akan dihapus, dan jika tidak, program akan memberi tahu bahwa data tidak ditemukan.

6. **Fungsi `Menu()`**
   ```python
   def menu():
    while True:
        print("\nMenu:")
        print("T. Tambah Data")
        print("M. Menampilkan Data")
        print("U. Ubah Data")
        print("H. Hapus Data")
        print("S. Selesai")
        pilihan = input("Pilih menu yang di butuhkan : ")

        if pilihan == "T":
            tambah_data()
        elif pilihan == "M":
            tampilkan_data()
        elif pilihan == "U":
            ubah_data()
        elif pilihan == "H":
            hapus_data()
        elif pilihan == "S":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
   ```
   
Fungsi `menu()` adalah menu utama yang memungkinkan pengguna untuk memilih tindakan yang ingin dilakukan.

Program terus berjalan dalam loop `while True` hingga pengguna memilih opsi untuk keluar (pilihan S).

Berdasarkan pilihan yang dimasukkan pengguna, fungsi yang sesuai akan dipanggil.

Jika input tidak valid, program akan meminta pengguna untuk memilih menu lagi.

7. **Menjalankan `program`**
   
   ```python
   menu()
   ```
   Menjalankan fungsi `menu()` yang memulai seluruh alur program dan menampilkan menu kepada pengguna.

# Hasil Interaksi Program 
![foto](https://github.com/aprilia55/labpy06/blob/fae788891b21fb4d49ab00b8cbf015125b31ef47/Screen%20Shot%202024-12-01%20at%2012.59.08.png)

# Flow Chart alur penggunaan program
![foto]()


   






