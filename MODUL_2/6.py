# lat23 + Soal 6
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
        return n * 2


# 6
class SiswaSMA(Manusia):

    def __init__(self, nama, Nisn, kelas, alamat):
        self.nama = nama
        self.no = Nisn
        self.kelas = kelas
        self.alamat = alamat

    def __str__(self):
        a = "Nama : " + self.nama + '\n' + \
            "No Induk : " + str(self.no) + '\n' + \
            "Kelas : " + str(self.kelas) + '\n' + \
            "Tinggal di : " + self.alamat + '\n'
        print(a)

    def ambilNama(self):
        print(self.nama)

    def ambilNisn(self):
        print(self.no)

    def ambilKelas(self):
        print(self.kelas)

    def ambilAlamat(self):
        print(self.alamat)
