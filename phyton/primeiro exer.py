positivos=0
for i in range(1,6):
    m=int(input('fale um número: '))
    if m<0:
        print('é negativo')
    elif m==0:
        print('É zero rapaz')
    elif m>0:
        print('é positivo')
        positivos = positivos + 1

print(f'Você digitou {positivos} números positivos!')
        
