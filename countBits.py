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

        num.append(q)
        binario = num[::-1]
    else:
        pass

    return binario.count(1)

a=count_bits(21)
print(a)