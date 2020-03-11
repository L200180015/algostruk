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


p1 = Manusia('Andi')
p1.ucapSalam()
