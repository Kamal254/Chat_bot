def dic(a,b):
    c = {}
    for x in a.keys():
        for i in b.keys():
            if x==i:
                c[x]=a[x]+b[i]
    for x in a.keys():
        if x in c.keys():
            continue
        else:
            c[x]=a[x]
    for i in b.keys():
        if i in c.keys():
            continue
        else:
            c[i]=b[i]
    return c