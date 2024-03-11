
# Manajemen Tugas
import os
os.system('cls')

# Node
class Tugas:
    def __init__(self, noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status):
        self.noTugas = noTugas
        self.mataKuliah = mataKuliah
        self.materi = materi
        self.tenggatWaktu = tenggatWaktu
        self.jenisTugas = jenisTugas
        self.status = status
        self.next = None

# Linked List
class ManajemenTugas(Tugas):
    def __init__(self):
        self.head = None

    def noTugas(self):
        count = 1
        nodeSekarang = self.head
        while nodeSekarang:
            count += 1
            nodeSekarang = nodeSekarang.next
        
        return count

    def tambahkanTugasDariAwal(self, noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status):
        if self.head == None:
            self.head = Tugas(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)
        else:
            nodeBaru = Tugas(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)
            nodeBaru.next = self.head
            self.head = nodeBaru

    def tambahkanTugasDiantara(self, noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status, posisi):
        if self.head == None or noTugas == 1:
            self.tambahkanTugasDariAwal(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)

        count = 0
        nodeSekarang = self.head
        while nodeSekarang != None:
            if count == posisi - 1:
                nodeBaru = Tugas(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)
                nodeBaru.next = nodeSekarang.next
                nodeSekarang.next = nodeBaru
                return
                
            nodeSekarang = nodeSekarang.next
            count += 1    

    def tambahkanTugasDariBelakang(self, noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status):
        if self.head == None:
            self.head = Tugas(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)
            
        else:   
            nodeSekarang = self.head
            while nodeSekarang.next:
                nodeSekarang = nodeSekarang.next
            nodeSekarang.next = Tugas(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)

    def tambahkanTugas(self):
        try:
            print("="*30)
            print("Tambahkan tugas dari urutan:")
            print("1. Awal")
            print("2. Posisi Tertentu")
            print("3. Akhir")
            ("="*30)
            opt = int(input("Masukkan operasi menggunakan angka = "))
            if opt==1:
                noTugas = self.noTugas()
                mataKuliah = input("Masukkan Mata Kuliah Tugas = ")
                materi = input("Materi dari Tugas tersebut = ")
                tenggatWaktu = input("Tenggat Waktu Tugas = ")
                jenisTugas = input("Apa Jenis Tugasnya? (Kelompok/Individu/Praktikum) = ")
                status = "Belum Selesai"
                self.tambahkanTugasDariAwal(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)
            elif opt==2:
                noTugas = self.noTugas()
                mataKuliah = input("Masukkan Mata Kuliah Tugas = ")
                materi = input("Materi dari Tugas Tersebut = ")
                tenggatWaktu = input("Tenggat Waktu Tugas = ")
                jenisTugas = input("Apa Jenis Tugasnya? (Kelompok/Individu/Praktikum) = ")
                status = "Belum Selesai"
                posisi = int(input("Ingin dimasukkan ke posisi berapa? = "))
                self.tambahkanTugasDiantara(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status, posisi)
            elif opt==3:
                noTugas = self.noTugas()
                mataKuliah = input("Masukkan Mata Kuliah Tugas = ")
                materi = input("Materi dari Tugas tersebut = ")
                tenggatWaktu = input("Tenggat Waktu Tugas = ")
                jenisTugas = input("Apa Jenis Tugasnya? (Kelompok/Individu/Praktikum) = ")
                status = "Belum Selesai"
                ("="*30)
                self.tambahkanTugasDariBelakang(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)
            else:
                main()
        except ValueError:
            os.system('cls')
            print("Masukkan Angka")
        
    def hapusTugasDariAwal(self):
        if self.head == None:
            print("Belum ada tugas")
            return

        self.head = self.head.next
            
    def hapusTugasDiantara(self, posisi):
        if self.head == None:
            print("Belum ada tugas")
            return
        
        count = 0
        nodeSekarang = self.head
        while nodeSekarang != None:
            if count == posisi - 1:
                nodeSekarang.next = nodeSekarang.next.next
                break
            
            count += 1
            nodeSekarang.next

    def hapusTugasDariBelakang(self):
        if self.head == None:
            print("Belum ada tugas")
            return

        if self.head.next == None:
            self.head = None
            return

        nodeSekarang = self.head
        while nodeSekarang.next.next != None:
            nodeSekarang = nodeSekarang.next
        nodeSekarang.next = None

    def hapusTugas(self):
        try:    
            print("Menghapus Daftar Tugas")
            print("1. Hapus Daftar Tugas di Awal")
            print("2. Hapus Daftar Tugas di Posisi Tertentu")
            print("3. Hapus Daftar Tugas di Akhir")
            opt = int(input("Masukkan Operasi Menggunakan Angka = "))
            if opt==1:
                self.hapusTugasDariAwal()
            elif opt==2:
                posisi = int(input("Ingin Hapus Tugas No Berapa? = "))
                self.hapusTugasDiantara(posisi)
            elif opt==3:
                self.hapusTugasDariBelakang()
            else:
                main()
        except ValueError:
            os.system('cls')
            print("Masukkan Angka")
            print("="*30)

    def lihatTugas(self):
        os.system('cls')
        print("Daftar Tugas:")
        if self.head == None:
            print("="*30)
            print("Belum ada tugas")
            return
        nodeSekarang = self.head
        while nodeSekarang != None:
            print("="*30)
            print(f"No Tugas = {nodeSekarang.noTugas}")
            print(f"Mata Kuliah = {nodeSekarang.mataKuliah}")
            print(f"Materi = {nodeSekarang.materi}")
            print(f"Tenggat Waktu = {nodeSekarang.tenggatWaktu}")
            print(f"Jenis Tugas = {nodeSekarang.jenisTugas}")
            print(f"Status Tugas = {nodeSekarang.status}")
            nodeSekarang = nodeSekarang.next
        skip = input("\nENTER untuk melanjutkan")
        
    def perbaruiTugas(self, noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status):
        nodeSekarang = self.head
        while nodeSekarang != None:
            if nodeSekarang.noTugas == noTugas:
                nodeSekarang.mataKuliah = mataKuliah
                nodeSekarang.materi = materi
                nodeSekarang.tenggatWaktu = tenggatWaktu
                nodeSekarang.jenisTugas = jenisTugas
                nodeSekarang.status = status
                return True
        return False
    
    def lihatSortedTugas(self, tugas):
            print("="*30)
            print(f"No Tugas = {tugas.noTugas}")
            print(f"Mata Kuliah = {tugas.mataKuliah}")
            print(f"Materi = {tugas.materi}")
            print(f"Tenggat Waktu = {tugas.tenggatWaktu}")
            print(f"Jenis Tugas = {tugas.jenisTugas}")
            print(f"Status Tugas = {tugas.status}")

    def quickSort(self, list, key, ascending=True):
        if len(list) <= 1:
            return list

        pivot = list[0]
        kiri = [x for x in list[1:] if (x.__getattribute__(key) < pivot.__getattribute__(key)) == ascending]
        kanan = [x for x in list[1:] if (x.__getattribute__(key) >= pivot.__getattribute__(key)) == ascending]

        sorted = self.quickSort(kiri, key, ascending) + [pivot] + self.quickSort(kanan, key, ascending)

        return sorted
        
    def temporaryList(self, key, ascending=True):
        list = []
        nodeSekarang = self.head
        while nodeSekarang:
            list.append(nodeSekarang)
            nodeSekarang = nodeSekarang.next

        sorted = self.quickSort(list, key, ascending)
        for tugas in sorted:
            self.lihatSortedTugas(tugas)
        skip = input("\nENTER untuk melanjutkan")
        

    def quickSortMenu(self):
        try:
            print("Mengurutkan Tugas")
            print("Urutkan Tugas dengan:")
            print("1. No Tugas (Ascending)")
            print("2. No Tugas (Descending)")
            print("3. Mata Kuliah (Ascending)")
            print("4. Mata Kuliah (Descending)")
            opt = int(input("Masukkan Operasi dengan Angka = "))    
            if opt==1:
                self.temporaryList("noTugas")
            elif opt==2:
                self.temporaryList("noTugas", False)
            elif opt==3:
                self.temporaryList("mataKuliah")
            elif opt==4:
                self.temporaryList("mataKuliah", False)
        except ValueError:
            print("Masukkan Angka")


def main():
        os.system("cls")
        print("Selamat Datang!")
        print("Di Program Notion, Manajemen Tugas Kuliah")

        tugasKu = ManajemenTugas()
        while True:
            try:
                print("="*30)
                print("Manajemen Tugas Kuliah")
                print("Menu Program")
                print("1. Tambahkan Tugas Baru")
                print("2. Lihat Daftar Tugas")
                print("3. Hapus Daftar Tugas")
                print("4. Perbarui Daftar Tugas")
                print("5. Mengurutkan Tugas")
                print("6. Keluar Program")
                print("="*30)
                operator = int(input("Pilih Menu Menggunakan Angka = "))
                os.system("cls")
                if operator==1:
                    tugasKu.tambahkanTugas()
                elif operator==2:
                    os.system('cls')
                    tugasKu.lihatTugas()
                elif operator==3:
                    os.system('cls')
                    tugasKu.lihatTugas()
                    tugasKu.hapusTugas()
                elif operator==4:
                    tugasKu.lihatTugas()
                    print("Memperbarui Tugas")
                    noTugas = int(input("Masukkan Nomor Tugas yang Ingin Diperbarui = "))
                    mataKuliah = input("Masukkan Mata Kuliah Tugas = ")
                    materi = input("Materi dari Tugas tersebut = ")
                    tenggatWaktu = input("Tenggat Waktu Tugas = ")
                    jenisTugas = input("Apa Jenis Tugasnya? (Kelompok/Individu/Praktikum) = ")
                    status = "Belum Selesai"
                    ("="*30)
                    tugasKu.perbaruiTugas(noTugas, mataKuliah, materi, tenggatWaktu, jenisTugas, status)
                elif operator ==5 :
                    tugasKu.quickSortMenu()
                else:
                    print("Anda Keluar Dari Program")
                    break
            except ValueError:
                os.system('cls')   
                print("Masukkan Angka")
main()
