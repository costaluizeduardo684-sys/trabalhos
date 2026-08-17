n=0
k=0
for i in range(9):
    m=int(input('fala uma das notas: '))
    n=n+m
    if m == -1:
        k=(n+1)/i
        print (f'{k} esta é sua média')
        if k>7:
            print('Tá aprovado')
        elif k>5:
            print('Tá de recuperação')
        else :
            print('Tá reprovado')
            break
        print(f'a quantidade de notas digitadas foi {i-1}')