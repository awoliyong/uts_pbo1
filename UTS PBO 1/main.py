from rekening_tabungan import RekeningTabungan
from rekening_giro import RekeningGiro
from transaksi import Transaksi

daftar_rekening = []
daftar_transaksi = []


# helper untuk mencari rekening berdasarkan nomor
def cari_rekening_by_no(no_rek):
    for rek in daftar_rekening:
        if rek.get_no_rekening().lower() == no_rek.lower():
            return rek
    return None


# menu 1: tambah rekening atau transaksi
def menu_tambah_data():
    print("\nTambah Data")
    print("1. Rekening Tabungan")
    print("2. Rekening Giro")
    print("3. Transaksi Baru")
    jenis = input("Pilih jenis data: ")

    if jenis == "1":
        no_rek = input("Nomor Rekening: ")
        nama = input("Nama Pemilik: ")
        saldo = float(input("Saldo Awal: "))
        bunga = float(input("Bunga Tahunan (%): "))
        batas = float(input("Batas Tarik Harian: "))
        tipe = input("Jenis Tabungan (Reguler/Pelajar): ")

        rek_baru = RekeningTabungan(no_rek, nama, saldo, bunga, batas, tipe)
        daftar_rekening.append(rek_baru)
        print("Rekening tabungan berhasil ditambahkan.")

    elif jenis == "2":
        no_rek = input("Nomor Rekening: ")
        nama = input("Nama Pemilik: ")
        saldo = float(input("Saldo Awal: "))
        limit = float(input("Limit Overdraft: "))
        admin = float(input("Biaya Admin Bulanan: "))
        perusahaan = input("Nama Perusahaan: ")

        rek_baru = RekeningGiro(no_rek, nama, saldo, limit, admin, perusahaan)
        daftar_rekening.append(rek_baru)
        print("Rekening giro berhasil ditambahkan.")

    elif jenis == "3":
        no_rek = input("Masukkan Nomor Rekening tujuan: ")
        rek = cari_rekening_by_no(no_rek)

        if rek is None:
            print("Rekening tidak ditemukan.")
            return

        id_trx = input("ID Transaksi: ")
        jenis_trx = input("Jenis Transaksi (Setor/Tarik): ")
        nominal = float(input("Nominal: "))

        trx = Transaksi(id_trx, jenis_trx, nominal, rek)
        if trx.proses_transaksi():
            daftar_transaksi.append(trx)
            print(f"Transaksi berhasil diproses. Saldo saat ini: Rp{rek.get_saldo():,.0f}")
        else:
            print("Transaksi gagal. Periksa saldo atau batas penarikan.")
    else:
        print("Pilihan tidak valid.")


# menu 2: tampilkan semua rekening dan transaksi
def menu_tampilkan_data():
    print("\nDaftar Rekening")
    if not daftar_rekening:
        print("Belum ada data rekening.")
    else:
        for rek in daftar_rekening:
            print(rek.get_info_rekening())

    print("\nRiwayat Transaksi")
    if not daftar_transaksi:
        print("Belum ada data transaksi.")
    else:
        for trx in daftar_transaksi:
            print(trx.get_detail_transaksi())


# menu 3: cari rekening berdasarkan nomor rekening
def menu_cari_data():
    no_rek = input("\nMasukkan Nomor Rekening yang dicari: ")
    hasil = cari_rekening_by_no(no_rek)

    if hasil is not None:
        print("Data ditemukan:")
        print(hasil.get_info_rekening())
    else:
        print(f"Rekening dengan nomor {no_rek} tidak ditemukan.")


# menu 4: ubah data rekening
def menu_ubah_data():
    no_rek = input("\nMasukkan Nomor Rekening yang akan diubah: ")
    rek = cari_rekening_by_no(no_rek)

    if rek is None:
        print("Rekening tidak ditemukan.")
        return

    nama_baru = input(f"Nama Pemilik baru (lama: {rek.get_nama_pemilik()}): ")
    if nama_baru.strip() != "":
        rek.set_nama_pemilik(nama_baru)

    if isinstance(rek, RekeningTabungan):
        batas_baru = float(input(f"Batas Tarik Harian baru (lama: {rek.get_batas_tarik_harian():,.0f}): "))
        rek.set_batas_tarik_harian(batas_baru)
    elif isinstance(rek, RekeningGiro):
        limit_baru = float(input(f"Limit Overdraft baru (lama: {rek.get_limit_overdraft():,.0f}): "))
        rek.set_limit_overdraft(limit_baru)

    print("Data rekening berhasil diperbarui.")


# menu 5: cek status saldo dan fitur khusus rekening
def menu_cek_status_data():
    no_rek = input("\nMasukkan Nomor Rekening untuk cek status: ")
    rek = cari_rekening_by_no(no_rek)

    if rek is None:
        print("Rekening tidak ditemukan.")
        return

    print(f"Pemilik: {rek.get_nama_pemilik()}")
    if rek.get_saldo() < 0:
        print(f"Status Saldo: Minus / Menggunakan Overdraft (Rp{rek.get_saldo():,.0f})")
    elif rek.get_saldo() < 100000:
        print(f"Status Saldo: Saldo Minim (Rp{rek.get_saldo():,.0f})")
    else:
        print(f"Status Saldo: Aktif dan Aman (Rp{rek.get_saldo():,.0f})")

    if isinstance(rek, RekeningTabungan):
        print(f"Estimasi Bunga Tahunan: Rp{rek.hitung_estimasi_bunga():,.0f}")
    elif isinstance(rek, RekeningGiro):
        total_dana = rek.get_saldo() + rek.get_limit_overdraft()
        print(f"Total Dana Tersedia (Saldo + Overdraft): Rp{total_dana:,.0f}")


def main():
    # data awal untuk pengujian program
    daftar_rekening.append(RekeningTabungan("1001", "Andika Ramadhan Iskandar", 1500000, 2.5, 5000000, "Reguler"))
    daftar_rekening.append(RekeningGiro("2001", "Amanda Trihandayani", 10000000, 3000000, 25000, "CV Suka Maju"))

    while True:
        print("\nAplikasi Rekening Bank Mini")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Ubah Data")
        print("5. Cek Status Data")
        print("6. Keluar dari Program")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            menu_tambah_data()
        elif pilihan == "2":
            menu_tampilkan_data()
        elif pilihan == "3":
            menu_cari_data()
        elif pilihan == "4":
            menu_ubah_data()
        elif pilihan == "5":
            menu_cek_status_data()
        elif pilihan == "6":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()