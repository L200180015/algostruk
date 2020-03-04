def faktorPrima(x):
    bilangan = []
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            bilangan.append(loop)
        else:
            loop +=1
    return bilangan
