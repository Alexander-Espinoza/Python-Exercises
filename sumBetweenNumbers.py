def get_sum(a,b):
    if a<b:
        minor = a
        mayor = b
    else:
        minor = b
        mayor = a
        if a==b :
            equals=True
    suma = 0 
    while minor <= mayor:
        
        suma += minor
        minor += 1

    return suma

suma=get_sum(1,1)
print(suma)
        
        