# Manajemen Tugas

from prettytable import PrettyTable
import os
os.system('cls')

class Pengguna:
    def __init__(self, nama, umur, semester, programStudi):
        self.nama = nama
        self.umur = umur
        self.semester = semester
        self.programStudi = programStudi

    def tampilkanPengguna(self):
        print("Data Pengguna")
        print("="*30)
        print(f"Nama = {self.nama}")
        print(f"Umur = {self.umur}")
        print(f"Semester = {self.semester}")
        print(f"Program Studi = {self.programStudi}")
        print("=*30")

class Tugas:
    def __init__(self):
        self.mataKuliah = ""
        self.materi = ""
        self.tenggatWaktu = ""
        self.jenisTugas = ""
        self.status = ""
        self.dataTugas = []

    def tambahkanTugas(self, mataKuliah, materi, tenggatWaktu, jenisTugas, status = "Belum Selesai"):
        self.dataTugas.append([len(self.dataTugas) + 1, mataKuliah, materi, tenggatWaktu, jenisTugas, status])
        print("Tugas telah ditambah ke daftar tugas")

    def lihatTugas(self):
        tabel = PrettyTable()
        tabel.field_names = ["No", "Mata Kuliah", "Materi", "Tenggat Waktu", "Jenis Tugas", "Status Tugas"]
        for tugas in self.dataTugas:
            tabel.add_row(tugas)
        print(tabel)

    def hapusTugas(self, nomorTugas):
        if 1 <= nomorTugas <= len(self.dataTugas):
            del self.dataTugas[nomorTugas - 1]
            print("Tugas telah dihapus dari daftar tugas")
        else:
            print("Nomor tugas tidak valid")
    
    def perbaruiTugas(self, nomorTugas, informasi, nilaiBaru):
        infoBaru = ["Mata Kuliah", "Materi", "Tenggat Waktu", "Jenis Tugas", "Status Tugas"]
        if informasi in infoBaru:
            indexInformasi = infoBaru.index(informasi) + 1
            if 1 <= nomorTugas <= len(self.dataTugas):
                self.dataTugas[nomorTugas - 1][indexInformasi] = nilaiBaru
                print(f"Data {informasi} untuk tugas nomor {nomorTugas} telah diperbarui.")
            else:
                print("Nomor Tugas tidak Terdeteksi")
        else:
            print("Data yang dimasukkan Tidak Valid")


def main():
    print("Selamat Datang!")
    print("Di Program Notion, Manajemen Tugas Kuliah")
    print("Silahkan Masukkan Data Diri Anda")
    nama = input("Masukkan Nama Anda = ")
    umur = input("Masukkan Umur Anda = ")
    semester = input("Semester Anda saat ini = ")
    programStudi = input("Masukkan Program Studi Anda = ")
    penggunaBaru = Pengguna(nama, umur, semester, programStudi)
    tugasKu = Tugas()
    while True:
        print("="*30)
        print("Manajemen Tugas Kuliah")
        print("Menu Program")
        print("1. Tambahkan Tugas Baru")
        print("2. Lihat Daftar Tugas")
        print("3. Hapus Daftar Tugas")
        print("4. Perbarui Daftar Tugas")
        print("5. Lihat Detail Pengguna")
        print("6. Keluar Program")
        print("="*30)
        operator = int(input("Pilih Menu Menggunakan Angka = "))
        if operator==1:
            mataKuliah = input("Masukkan Mata Kuliah Tugas = ")
            materi = input("Materi dari Tugas tersebut = ")
            tenggatWaktu = input("Tenggat Waktu Tugas = ")
            jenisTugas = input("Apa Jenis Tugasnya? (Kelompok/Individu/Praktikum) = ")
            tugasKu.tambahkanTugas(mataKuliah, materi, tenggatWaktu, jenisTugas)
        elif operator==2:
            tugasKu.lihatTugas()
        elif operator==3:
            tugasKu.lihatTugas()
            nomorTugas = int(input("Masukkan Nomor Tugas yang Ingin Dihapus = "))
            tugasKu.hapusTugas(nomorTugas)
        elif operator==4:
            tugasKu.lihatTugas()
            nomorTugas = int(input("Masukkan Nomor Tugas yang Ingin Diperbarui = "))
            informasi = input("Data Apa Yang Ingin Diperbarui (Mata Kuliah / Materi / Tenggat Waktu / Jenis Tugas / Status Tugas) = ")
            nilaiBaru = input("Masukkan Data Baru = ")
            tugasKu.perbaruiTugas(nomorTugas, informasi, nilaiBaru)
        elif operator==5:
            penggunaBaru.tampilkanPengguna()
        else:
            print("Anda Keluar Dari Program")
            break
        
main()