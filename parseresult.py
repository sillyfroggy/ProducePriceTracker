def parseresult(res):
    res = list(res)
    price = ""
    for r in res:
        if r == '>':
            res[res.index(r)] = ''
            break
        elif r in "$1234567890.":
            price += r
        else:
            res[res.index(r)] = ''

    res.reverse()
    for r in res:
        if r == '<':
            res[res.index(r)] = ''
            break
        else:
            res[res.index(r)] = ''

    res.reverse()
    return ''.join(res)
