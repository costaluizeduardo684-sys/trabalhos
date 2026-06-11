m=int(input('fala um número para tabuada: '))
for i in range (11):
    print(f'{m}x{i}={m*i}')
    if m==0:
        break
    else:
        if m<10:
            print('pequeno')
        elif m>10 and m<50:
            print('médio')
        else:
            print('grande')

    
