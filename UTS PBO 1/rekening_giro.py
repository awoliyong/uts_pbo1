from rekening import Rekening


class RekeningGiro(Rekening):
    # constructor berparameter dengan 3 atribut private tambahan
    def __init__(self, no_rekening, nama_pemilik, saldo, limit_overdraft, biaya_admin, nama_perusahaan):
        super().__init__(no_rekening, nama_pemilik, saldo)
        self.__limit_overdraft = limit_overdraft
        self.__biaya_admin = biaya_admin
        self.__nama_perusahaan = nama_perusahaan

    # getter dan setter
    def get_limit_overdraft(self):
        return self.__limit_overdraft

    def set_limit_overdraft(self, limit_overdraft):
        self.__limit_overdraft = limit_overdraft

    def get_biaya_admin(self):
        return self.__biaya_admin

    def get_nama_perusahaan(self):
        return self.__nama_perusahaan

    def set_nama_perusahaan(self, nama_perusahaan):
        self.__nama_perusahaan = nama_perusahaan

    # method tambahan 1: cek apakah penarikan masih masuk limit overdraft
    def cek_bisa_overdraft(self, jumlah_tarik):
        return (self.get_saldo() + self.__limit_overdraft) >= jumlah_tarik

    # method tambahan 2: potong saldo untuk biaya admin
    def potong_biaya_admin(self):
        self.set_saldo(self.get_saldo() - self.__biaya_admin)

    # override method dari superclass
    def get_info_rekening(self):
        return (
            f"[Giro - {self.__nama_perusahaan}] {super().get_info_rekening()} "
            f"| Limit Overdraft: Rp{self.__limit_overdraft:,.0f} | Admin: Rp{self.__biaya_admin:,.0f}"
        )