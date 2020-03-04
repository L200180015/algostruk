def formatRupiah(n):
    x = str(n)
    if len(x) <= 3 :
        return 'Rp ' + x
    else:
        p = x[-3:]
        q = x[:-3]
        return (formatRupiah(q) + '.' + p)
        print ('Rp' + (formatRupiah(q)) + '.' + p)
