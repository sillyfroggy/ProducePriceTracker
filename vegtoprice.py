from parseresult import parseresult

def vegtoprice(veggie):
    with open("veggies.txt", "r") as veg:
        i = False
        j = False
        for ln in veg.readlines():
            if i:
                j = True
                i = False
                continue
            if j:
                print(parseresult(ln), '\n')
                j = False
                continue
            if veggie in ln:
                print(parseresult(ln))
                i = True
                continue