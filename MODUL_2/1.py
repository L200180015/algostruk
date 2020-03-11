class Pesan(object):
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

    # 1a
    def apakahTerkandung(self, kata):
        return kata in self.teks

    # 1b
    def jumlahHurufKonsonan(self):
        vokal = 'aiueo'
        kata = self.teks.lower()
        jmlK = 0
        pjgKata = len(kata)
        for huruf in kata:
            if huruf not in vokal:
                jmlK += 1
        return jmlK
    # 1c
    def jumlahHurufVokal(self):
        vokal = 'aiueo'
        kata = self.teks.lower()
        jmlV = 0
        pjgKata = len(kata)
        for huruf in kata:
            if huruf in vokal:
                jmlV += 1
        return jmlV
