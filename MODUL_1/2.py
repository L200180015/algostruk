def gambarlahPersegiEmpat(p, q):
    for i in range (p):
        if i==0 or i==p-1:
            print("@"*q)
        else:
            print("@"+" "*(q-2)+"@")
