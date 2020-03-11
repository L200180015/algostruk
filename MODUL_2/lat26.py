# lat26 melanjutkan lat24

class Manusia(object):
    """
        Class Manusia dgn inisiasi 'nama'
    """
    keadaan = 'lapar'
    def __init__(self, nama):
        self.nama = nama
    def ucapSalam(self):
        print('Salam, namaku', self.nama)
    def makan(self, s):
        print('saya baru aja maem', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('saya abis olahraga', k)
        self.keadaan = 'lapar'
    def mengaliDgnDua(self, n):
        return n*2

class Mahasiswa(Manusia):
    """Class Mahasiswa yg dibangun dari class Manusia"""
    keadaan = 'lapar'
    def __init__(self, nama, nim, kota, us):
        """ Metode ini menutupi inisiasi dari class Manusia """
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.nim) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' perharinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """ Method ini menutupi method di Manusia """
        print('Saya baru aje maem', s, 'Sambil nugass')
        self.keadaan = 'kenyang'


m1 = Mahasiswa('Andi', 14, 'Sono', 4500000)
m2 = Mahasiswa('Amin Richman', 999, 'Asgard', 9999999)
m3 = Mahasiswa('Plankton', 307, 'Bikini Bottom', 10000)
daftar = [m1, m2, m3]
for i in daftar:
    print(i.nim)
for i in daftar:
    print(i)
