from rekening import Rekening


class RekeningTabungan(Rekening):
    # constructor berparameter dengan 3 atribut private tambahan
    def __init__(self, no_rekening, nama_pemilik, saldo, bunga_tahunan, batas_tarik_harian, jenis_tabungan):
        super().__init__(no_rekening, nama_pemilik, saldo)
        self.__bunga_tahunan = bunga_tahunan
        self.__batas_tarik_harian = batas_tarik_harian
        self.__jenis_tabungan = jenis_tabungan

    # getter dan setter
    def get_bunga_tahunan(self):
        return self.__bunga_tahunan

    def set_bunga_tahunan(self, bunga_tahunan):
        self.__bunga_tahunan = bunga_tahunan

    def get_batas_tarik_harian(self):
        return self.__batas_tarik_harian

    def set_batas_tarik_harian(self, batas_tarik_harian):
        self.__batas_tarik_harian = batas_tarik_harian

    def get_jenis_tabungan(self):
        return self.__jenis_tabungan

    # method tambahan 1: hitung estimasi bunga per tahun
    def hitung_estimasi_bunga(self):
        return self.get_saldo() * (self.__bunga_tahunan / 100)

    # method tambahan 2: cek batas penarikan harian
    def cek_limit_tarik(self, jumlah):
        return jumlah <= self.__batas_tarik_harian

    # override method dari superclass
    def get_info_rekening(self):
        return (
            f"[Tabungan - {self.__jenis_tabungan}] {super().get_info_rekening()} "
            f"| Bunga: {self.__bunga_tahunan}% | Limit Tarik: Rp{self.__batas_tarik_harian:,.0f}"
        )