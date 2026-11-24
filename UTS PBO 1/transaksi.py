from rekening_tabungan import RekeningTabungan
from rekening_giro import RekeningGiro


class Transaksi:
    # constructor dengan atribut private dan relasi asosiasi ke satu Rekening
    def __init__(self, id_transaksi, jenis_transaksi, nominal, rekening):
        self.__id_transaksi = id_transaksi
        self.__jenis_transaksi = jenis_transaksi
        self.__nominal = nominal
        self.__rekening = rekening

    # getter
    def get_id_transaksi(self):
        return self.__id_transaksi

    def get_jenis_transaksi(self):
        return self.__jenis_transaksi

    def get_nominal(self):
        return self.__nominal

    def get_rekening(self):
        return self.__rekening

    # method tambahan 1: jalankan transaksi pada rekening terkait
    def proses_transaksi(self):
        if self.__rekening is None or self.__nominal <= 0:
            return False

        if self.__jenis_transaksi.lower() == "setor":
            self.__rekening.setor(self.__nominal)
            return True

        elif self.__jenis_transaksi.lower() == "tarik":
            # cek aturan sesuai jenis subclass rekening
            if isinstance(self.__rekening, RekeningTabungan):
                if not self.__rekening.cek_limit_tarik(self.__nominal):
                    return False
                return self.__rekening.tarik(self.__nominal)

            elif isinstance(self.__rekening, RekeningGiro):
                if self.__rekening.cek_bisa_overdraft(self.__nominal):
                    saldo_baru = self.__rekening.get_saldo() - self.__nominal
                    self.__rekening.set_saldo(saldo_baru)
                    return True
                return False

            return self.__rekening.tarik(self.__nominal)

        return False

    # method tambahan 2: format riwayat transaksi
    def get_detail_transaksi(self):
        return (
            f"ID: {self.__id_transaksi} | Jenis: {self.__jenis_transaksi} "
            f"| Nominal: Rp{self.__nominal:,.0f} | Rek Tujuan: "
            f"{self.__rekening.get_no_rekening()} ({self.__rekening.get_nama_pemilik()})"
        )