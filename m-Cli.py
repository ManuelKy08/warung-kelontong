import os
import datetime

daftar_produk = {
    1: {"nama": "Indomie Goreng", "harga": 3000, "stok": 50, "kategori": "Makanan"},
    2: {"nama": "Air Mineral Aqua 600ml", "harga": 1500, "stok": 100, "kategori": "Minuman"},
    3: {"nama": "Roti'O", "harga": 12000, "stok": 30, "kategori": "Makanan"},
    4: {"nama": "Cokelat Silverqueen", "harga": 15000, "stok": 40, "kategori": "Makanan"},
    5: {"nama": "Teh Pucuk Harum", "harga": 3500, "stok": 60, "kategori": "Minuman"},
    6: {"nama": "Deterjen Rinso", "harga": 18000, "stok": 20, "kategori": "Perlengkapan Rumah Tangga"},
    7: {"nama": "Shampo Sunsilk", "harga": 16000, "stok": 25, "kategori": "Perlengkapan Rumah Tangga"},
    8: {"nama": "Sabun Mandi Lifebuoy", "harga": 4000, "stok": 35, "kategori": "Perlengkapan Rumah Tangga"},
    9: {"nama": "Beras Premium 5kg", "harga": 60000, "stok": 15, "kategori": "Makanan"},
    10: {"nama": "Minyak Goreng 1L", "harga": 15000, "stok": 10, "kategori": "Makanan"},
    11: {"nama": "Susu Kental Manis", "harga": 10000, "stok": 45, "kategori": "Makanan"},
    12: {"nama": "Kopi Instan", "harga": 5000, "stok": 70, "kategori": "Minuman"},
    13: {"nama": "Biskuit Marie", "harga": 8000, "stok": 55, "kategori": "Makanan"},
    14: {"nama": "Mie Sedap Goreng", "harga": 2800, "stok": 80, "kategori": "Makanan"},
    15: {"nama": "Fanta Merah", "harga": 6000, "stok": 90, "kategori": "Minuman"},
    16: {"nama": "Sprite", "harga": 6000, "stok": 95, "kategori": "Minuman"},
    17: {"nama": "Coca-Cola", "harga": 6500, "stok": 85, "kategori": "Minuman"},
    18: {"nama": "Flashdisk ", "harga": 7000, "stok": 20, "kategori": "Lain-lain", "gambar": "fd.jpg"},
    19: {"nama": "Kabel Data ", "harga": 7500, "stok": 22, "kategori": "Lain-lain", "gambar": "kabel.jpg"},
    20: {"nama": "Headset  ", "harga": 8000, "stok": 28, "kategori": "Lain-lain", "gambar": "headset.jpg"},
    21: {"nama": "Saus Sambal", "harga": 9000, "stok": 65, "kategori": "Makanan"},
    22: {"nama": "Kecap Manis", "harga": 9500, "stok": 60, "kategori": "Makanan"},
    23: {"nama": "Gula Pasir 1kg", "harga": 12000, "stok": 30, "kategori": "Makanan"},
    24: {"nama": "Garam Dapur", "harga": 2000, "stok": 75, "kategori": "Makanan"},
    25: {"nama": "Tepung Terigu 1kg", "harga": 10000, "stok": 40, "kategori": "Makanan"},
    26: {"nama": "Telur Ayam 1kg", "harga": 25000, "stok": 18, "kategori": "Makanan"},
    27: {"nama": "Tahu Putih", "harga": 3000, "stok": 50, "kategori": "Makanan"},
    28: {"nama": "Tempe", "harga": 2500, "stok": 55, "kategori": "Makanan"},
    29: {"nama": "Kerupuk Udang", "harga": 7000, "stok": 30, "kategori": "Makanan"},
    30: {"nama": "Bawang Merah", "harga": 8000, "stok": 25, "kategori": "Makanan"},
    31: {"nama": "Teh Botol Sosro", "harga": 4000, "stok": 70, "kategori": "Minuman"},
    32: {"nama": "Nu Green Tea", "harga": 4500, "stok": 65, "kategori": "Minuman"},
    33: {"nama": "Sari Roti Coklat", "harga": 6000, "stok": 45, "kategori": "Makanan"},
    34: {"nama": "Wafer Tango", "harga": 10000, "stok": 50, "kategori": "Makanan"},
    35: {"nama": "Beng-Beng", "harga": 4000, "stok": 60, "kategori": "Makanan"},
    36: {"nama": "Oreo", "harga": 9000, "stok": 55, "kategori": "Makanan"},
    37: {"nama": "Yakult", "harga": 8000, "stok": 80, "kategori": "Minuman"},
    38: {"nama": "Floridina Orange", "harga": 3000, "stok": 75, "kategori": "Minuman"},
    39: {"nama": "Pocari Sweat", "harga": 7000, "stok": 70, "kategori": "Minuman"},
    40: {"nama": "Indomie Ayam Bawang", "harga": 3000, "stok": 65, "kategori": "Makanan"},
    41: {"nama": "Super Bubur", "harga": 6000, "stok": 40, "kategori": "Makanan"},
    42: {"nama": "Energen Coklat", "harga": 2500, "stok": 50, "kategori": "Minuman"},
    43: {"nama": "Milo Kotak", "harga": 5000, "stok": 60, "kategori": "Minuman"},
    44: {"nama": "Susu Ultra Milk Coklat", "harga": 5500, "stok": 55, "kategori": "Minuman"},
    45: {"nama": "Tissue Paseo", "harga": 12000, "stok": 30, "kategori": "Perlengkapan Rumah Tangga"},
    46: {"nama": "Pasta Gigi Pepsodent", "harga": 10000, "stok": 35, "kategori": "Perlengkapan Rumah Tangga"},
    47: {"nama": "Sikat Gigi Formula", "harga": 7000, "stok": 40, "kategori": "Perlengkapan Rumah Tangga"},
    48: {"nama": "Royco Ayam", "harga": 1500, "stok": 80, "kategori": "Makanan"},
    49: {"nama": "Masako Sapi", "harga": 1500, "stok": 75, "kategori": "Makanan"},
    50: {"nama": " sunlight ", "harga": 11000, "stok": 25, "kategori": "Perlengkapan Rumah Tangga"},
    51: {"nama": " Baygon ", "harga": 20000, "stok": 15, "kategori": "Perlengkapan Rumah Tangga"},
    52: {"nama": " So Klin Pewangi ", "harga": 9000, "stok": 20, "kategori": "Perlengkapan Rumah Tangga"},
    53: {"nama": " Molto Pelembut ", "harga": 13000, "stok": 18, "kategori": "Perlengkapan Rumah Tangga"},
}

keranjang = {}
riwayat_transaksi = []
poin_pelanggan = 0
DISKON_PEMBELIAN_BESAR = 0.05 

def clear_screen():
    """Membersihkan tampilan terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_banner():
    """Menampilkan banner aplikasi."""
    print("""

 /$$$$$$$$        /$$                         /$$   /$$           /$$                 /$$      
|__  $$__/       | $$                        | $$  /$$/          | $$                | $$                           
   | $$  /$$$$$$ | $$   /$$  /$$$$$$         | $$ /$$/   /$$$$$$ | $$   /$$  /$$$$$$ | $$   /$$
   | $$ /$$__  $$| $$  /$$/ /$$__  $$ /$$$$$$| $$$$$/   /$$__  $$| $$  /$$/ /$$__  $$| $$  /$$/
   | $$| $$  \ $$| $$$$$$/ | $$  \ $$|______/| $$  $$  | $$  \ $$| $$$$$$/ | $$  \ $$| $$$$$$/ 
   | $$| $$  | $$| $$_  $$ | $$  | $$        | $$\  $$ | $$  | $$| $$_  $$ | $$  | $$| $$_  $$ 
   | $$|  $$$$$$/| $$ \  $$|  $$$$$$/        | $$ \  $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$ \  $$
   |__/ \______/ |__/  \__/ \______/         |__/  \__/ \______/ |__/  \__/ \______/ |__/  \__/
====================================================================
**                  Customer Puas                                 **
**                  Kami Sangat Bahagia dan Senang                **
**              Struk Tidak Diberikan Semua Belanjaan Gratis      **
====================================================================
    """)

def tampilkan_menu():
    """Menampilkan menu utama."""
    print("\nPilih fitur (1-9):")
    print("==================")
    print("1. Lihat Daftar Produk")
    print("2. Tambah ke Keranjang")
    print("3. Edit Jumlah di Keranjang")
    print("4. Lihat Keranjang")
    print("5. Hapus dari Keranjang")
    print("6. Cari Produk")
    print("7. Lihat Produk Berdasarkan Kategori")
    print("8. Hitung Total Belanja dan Bayar")
    print("9. Lihat Riwayat Transaksi")

def tampilkan_daftar_produk():
    """Menampilkan daftar produk beserta harga dan stok."""
    print("\nDaftar Produk Alfamart:")
    print("----------------------")
    for kode, produk in daftar_produk.items():
        print(f"{kode}. {produk['nama']} - Rp {produk['harga']:,} (Stok: {produk['stok']})")

def tambah_ke_keranjang():
    """Menambahkan produk ke keranjang belanja dengan nomor atau nama."""
    tampilkan_banner()
    tampilkan_daftar_produk()
    while True:
        input_produk = input("\nMasukkan nomor atau nama produk yang ingin dibeli: ").strip()
        produk_ditemukan = None
        kode_produk = None

    
        if input_produk.isdigit():
            kode_produk = int(input_produk)
            if kode_produk in daftar_produk:
                produk_ditemukan = daftar_produk[kode_produk]
            else:
                print("Nomor produk tidak valid.")
                continue
    
        else:
            for kode, produk in daftar_produk.items():
                if produk['nama'].lower() == input_produk.lower():
                    produk_ditemukan = produk
                    kode_produk = kode
                    break
            if not produk_ditemukan:
                print("Nama produk tidak ditemukan.")
                continue

        try:
            jumlah = int(input(f"Masukkan jumlah {produk_ditemukan['nama']} yang ingin dibeli: "))
            if jumlah > 0:
                if jumlah > produk_ditemukan['stok']:
                    print(f"Maaf, stok {produk_ditemukan['nama']} tidak mencukupi. Stok tersedia: {produk_ditemukan['stok']}")
                    continue
                if kode_produk in keranjang:
                    keranjang[kode_produk] += jumlah
                else:
                    keranjang[kode_produk] = jumlah
                print(f"{jumlah} {produk_ditemukan['nama']} berhasil ditambahkan ke keranjang.")
                break
            else:
                print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Masukkan jumlah dengan angka.")

def edit_jumlah_keranjang():
    """Mengedit jumlah produk yang sudah ada di keranjang."""
    tampilkan_banner()
    if not keranjang:
        print("\nKeranjang belanja Anda kosong.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    lihat_keranjang()
    while True:
        input_edit = input("\nMasukkan nomor atau nama produk yang ingin diubah jumlahnya: ").strip()
        kode_produk_edit = None

        if input_edit.isdigit():
            kode_produk_edit = int(input_edit)
            if kode_produk_edit not in keranjang:
                print("Nomor produk tidak ada di keranjang.")
                continue
        else:
            for kode in keranjang.keys():
                if daftar_produk[kode]['nama'].lower() == input_edit.lower():
                    kode_produk_edit = kode
                    break
            if kode_produk_edit is None:
                print("Nama produk tidak ada di keranjang.")
                continue

        try:
            jumlah_baru = int(input(f"Masukkan jumlah baru untuk {daftar_produk[kode_produk_edit]['nama']}: "))
            if jumlah_baru > 0:
                if jumlah_baru > daftar_produk[kode_produk_edit]['stok']:
                    print(f"Maaf, stok tidak mencukupi. Stok tersedia: {daftar_produk[kode_produk_edit]['stok']}")
                    continue
                keranjang[kode_produk_edit] = jumlah_baru
                print(f"Jumlah {daftar_produk[kode_produk_edit]['nama']} berhasil diubah menjadi {jumlah_baru}.")
                break
            else:
                print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Masukkan jumlah dengan angka.")

def lihat_keranjang():
    """Menampilkan isi keranjang belanja."""
    tampilkan_banner()
    if keranjang:
        print("\nIsi Keranjang Belanja Anda:")
        print("--------------------------")
        for kode, jumlah in keranjang.items():
            nama_produk = daftar_produk[kode]['nama']
            harga_satuan = daftar_produk[kode]['harga']
            total_harga = harga_satuan * jumlah
            print(f"{nama_produk} x {jumlah} = Rp {total_harga:,}")
    else:
        print("\nKeranjang belanja Anda masih kosong.")
    input("\nTekan Enter untuk kembali ke menu...")

def hapus_dari_keranjang():
    """Menghapus produk dari keranjang belanja."""
    tampilkan_banner()
    if not keranjang:
        print("\nKeranjang belanja Anda kosong.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    lihat_keranjang()
    while True:
        input_hapus = input("\nMasukkan nomor atau nama produk yang ingin dihapus dari keranjang: ").strip()
        kode_produk_hapus = None

        if input_hapus.isdigit():
            kode_produk_hapus = int(input_hapus)
            if kode_produk_hapus not in keranjang:
                print("Nomor produk tidak ada di keranjang.")
                continue
        else:
            for kode in keranjang.keys():
                if daftar_produk[kode]['nama'].lower() == input_hapus.lower():
                    kode_produk_hapus = kode
                    break
            if kode_produk_hapus is None:
                print("Nama produk tidak ada di keranjang.")
                continue
        break

    try:
        jumlah_hapus = int(input(f"Masukkan jumlah {daftar_produk[kode_produk_hapus]['nama']} yang ingin dihapus: "))
        if jumlah_hapus > 0:
            if jumlah_hapus >= keranjang[kode_produk_hapus]:
                del keranjang[kode_produk_hapus]
                print(f"Semua {daftar_produk[kode_produk_hapus]['nama']} berhasil dihapus dari keranjang.")
            else:
                keranjang[kode_produk_hapus] -= jumlah_hapus
                print(f"{jumlah_hapus} {daftar_produk[kode_produk_hapus]['nama']} berhasil dihapus dari keranjang.")
        else:
            print("Jumlah yang dihapus harus lebih dari 0.")
    except ValueError:
        print("Masukkan jumlah dengan angka.")

def cari_produk():
    """Mencari produk berdasarkan nama."""
    tampilkan_banner()
    kata_kunci = input("Masukkan nama produk yang ingin dicari: ").strip().lower()
    hasil_pencarian = {}
    for kode, produk in daftar_produk.items():
        if kata_kunci in produk['nama'].lower():
            hasil_pencarian[kode] = produk

    if hasil_pencarian:
        print("\nHasil Pencarian:")
        print("---------------")
        for kode, produk in hasil_pencarian.items():
            print(f"{kode}. {produk['nama']} - Rp {produk['harga']:,} (Stok: {produk['stok']})")
    else:
        print(f"Tidak ada produk yang cocok dengan kata kunci '{kata_kunci}'.")
    input("\nTekan Enter untuk kembali ke menu...")

def lihat_produk_berdasarkan_kategori():
    """Melihat produk berdasarkan kategori."""
    tampilkan_banner()
    kategori_unik = sorted(list(set(produk['kategori'] for produk in daftar_produk.values())))
    print("\nPilih Kategori:")
    print("---------------")
    for i, kategori in enumerate(kategori_unik):
        print(f"{i+1}. {kategori}")

    while True:
        try:
            pilihan_kategori = int(input("Masukkan nomor kategori: "))
            if 1 <= pilihan_kategori <= len(kategori_unik):
                kategori_dipilih = kategori_unik[pilihan_kategori - 1]
                print(f"\nProduk Kategori {kategori_dipilih}:")
                print("---------------------------")
                for kode, produk in daftar_produk.items():
                    if produk['kategori'] == kategori_dipilih:
                        print(f"{kode}. {produk['nama']} - Rp {produk['harga']:,} (Stok: {produk['stok']})")
                break
            else:
                print("Nomor kategori tidak valid.")
        except ValueError:
            print("Masukkan nomor dengan angka.")
    input("\nTekan Enter untuk kembali ke menu...")

def hitung_total_belanja_dan_bayar():
    """Menghitung total belanja, menerapkan diskon, dan menerima pembayaran."""
    tampilkan_banner()
    global poin_pelanggan
    if keranjang:
        total_belanja = 0
        print("\nDetail Belanja Anda:")
        print("------------------")
        for kode, jumlah in keranjang.items():
            nama_produk = daftar_produk[kode]['nama']
            harga_satuan = daftar_produk[kode]['harga']
            total_harga_item = harga_satuan * jumlah
            total_belanja += total_harga_item
            print(f"{nama_produk} x {jumlah} = Rp {total_harga_item:,}")

        diskon = 0
        if total_belanja > 100000:
            diskon = total_belanja * DISKON_PEMBELIAN_BESAR
            print(f"Diskon Pembelian Besar (5%): Rp {diskon:,}")

        total_bayar = total_belanja - diskon
        print(f"\nSubtotal: Rp {total_belanja:,}")
        print(f"Total Diskon: Rp {diskon:,}")
        print(f"Total Bayar: Rp {total_bayar:,}")

        while True:
            try:
                uang_diterima = int(input("Masukkan jumlah uang yang diterima: Rp "))
                if uang_diterima >= total_bayar:
                    kembalian = uang_diterima - total_bayar
                    print(f"Kembalian Anda: Rp {kembalian:,}")
                    
                    transaksi = {
                        "waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "produk": {daftar_produk[kode]['nama']: jumlah for kode, jumlah in keranjang.items()},
                        "total_belanja": total_belanja,
                        "diskon": diskon,
                        "total_bayar": total_bayar,
                        "uang_diterima": uang_diterima,
                        "kembalian": kembalian,
                    }
                    riwayat_transaksi.append(transaksi)
                    poin_pelanggan += int(total_bayar // 10000) 
                    print(f"Poin Anda saat ini: {poin_pelanggan}")
                    for kode, jumlah in keranjang.items():
                        daftar_produk[kode]['stok'] -= jumlah 
                    keranjang.clear() 
                    input("\nTekan Enter untuk melanjutkan...")
                    break
                else:
                    print("Uang yang Anda berikan kurang. Silakan masukkan lagi.")
            except ValueError:
                print("Masukkan jumlah uang dengan angka.")
    else:
        print("\nKeranjang belanja Anda kosong, tidak ada yang perlu dihitung.")
        input("\nTekan Enter untuk kembali ke menu...")

def lihat_riwayat_transaksi():
    """Menampilkan riwayat transaksi."""
    tampilkan_banner()
    if riwayat_transaksi:
        print("\nRiwayat Transaksi Anda:")
        print("----------------------")
        for i, transaksi in enumerate(riwayat_transaksi):
            print(f"Transaksi #{i+1} - {transaksi['waktu']}")
            for nama_produk, jumlah in transaksi['produk'].items():
                print(f"  - {nama_produk}: {jumlah}")
            print(f"  Total Belanja: Rp {transaksi['total_belanja']:,}")
            print(f"  Diskon: Rp {transaksi['diskon']:,}")
            print(f"  Total Bayar: Rp {transaksi['total_bayar']:,}")
            print(f"  Uang Diterima: Rp {transaksi['uang_diterima']:,}")
            print(f"  Kembalian: Rp {transaksi['kembalian']:,}\n")
    else:
        print("\nBelum ada riwayat transaksi.")
    input("\nTekan Enter untuk kembali ke menu...")

def main():
    """Fungsi utama aplikasi."""
    while True:
        clear_screen()
        tampilkan_banner()
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1-9): ")

        if pilihan == '1':
            clear_screen()
            tampilkan_banner()
            tampilkan_daftar_produk()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '2':
            clear_screen()
            tambah_ke_keranjang()
        elif pilihan == '3':
            clear_screen()
            edit_jumlah_keranjang()
        elif pilihan == '4':
            clear_screen()
            lihat_keranjang()
        elif pilihan == '5':
            clear_screen()
            hapus_dari_keranjang()
        elif pilihan == '6':
            clear_screen()
            cari_produk()
        elif pilihan == '7':
            clear_screen()
            lihat_produk_berdasarkan_kategori()
        elif pilihan == '8':
            clear_screen()
            hitung_total_belanja_dan_bayar()
        elif pilihan == '9':
            clear_screen()
            lihat_riwayat_transaksi()
        elif pilihan == '0':
            print("Terima kasih telah berbelanja di Alfamart CLI!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
