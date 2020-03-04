def jumlahHurufVokal(huruf):
    jumlah = 0
    vokal = ["a","i","u","e","o","A","I","E","O","U"]
    for i in huruf:
        if i in vokal:
            jumlah+=1
    return len(huruf), jumlah

def jumlahHurufKonsonan(huruf):
    jumlah = 0
    konsonan = ["a","i","u","e","o","A","I","E","O","U"]
    for i in huruf:
        if i in konsonan:
            jumlah+=1
    return len(huruf), len(huruf)-jumlah


