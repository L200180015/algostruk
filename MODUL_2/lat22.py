class Pesan(object):
    """
        Sebuah class bernama Pesan.
        untuk memahami konsep class dan object
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJmlKar(self):
        print('Kalimat punya', len(self.teks), 'karakter')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
