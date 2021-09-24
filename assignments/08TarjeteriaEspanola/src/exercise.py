
def datos_usuario(pa,pl):
    papel=12*pa
    plumon=35*pl
    if papel<plumon:
        return papel
    elif plumon<papel:
        return plumon
def main():
    #escribe tu código abajo de esta línea
    a=int(input('Dame la cantidad de pliegos de papel albanene: '))
    b=int(input('Dame la cantidad de plumones: '))
    m=datos_usuario(a,b)
    print('El número máximo de tarjetas que se pueden hacer es: '+str(m))

if __name__=='__main__':
    main()
