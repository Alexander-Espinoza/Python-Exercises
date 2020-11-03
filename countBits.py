def count_bits(n):
    if n>=0:
        D = n
        d = 2
        q = D//d
        
        num = []
        while d <= q :
            
            q = D//d
            r = D%d
            num.append(r)
            D = q
            print(r)
        num.append(q)
        binario = num[::-1]
    else:
        pass

    cantidad = list(filter(lambda x: x==1, binario))
    return len(cantidad)

count_bits(21)