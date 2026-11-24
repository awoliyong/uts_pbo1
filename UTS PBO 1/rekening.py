class Rekening:
    # constructor berparameter dengan 3 atribut private
    def __init__(self, no_rekening, nama_pemilik, saldo):
        self.__no_rekening = no_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    # getter dan setter
    def get_no_rekening(self):
        return self.__no_rekening

    def get_nama_pemilik(self):
        return self.__nama_pemilik

    def set_nama_pemilik(self, nama_pemilik):
        self.__nama_pemilik = nama_pemilik

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    # method tambahan 1: menambah saldo
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    # method tambahan 2: mengurangi saldo
    def tarik(self, jumlah):
        if jumlah > 0 and self.__saldo >= jumlah:
            self.__saldo -= jumlah
            return True
        return False

    # method untuk menampilkan ringkasan data
    def get_info_rekening(self):
        return f"No Rek: {self.__no_rekening} | Pemilik: {self.__nama_pemilik} | Saldo: Rp{self.__saldo:,.0f}"