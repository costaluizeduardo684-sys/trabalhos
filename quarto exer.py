s='python123'
for i in range (1,4):
    m=int(input('diga a senha: '))
    if m==s:
        print('Acesso liberado!')
    elif i==3:
        print('!Conta bloqueda!')
        print(r'''  _____
 /     \
| () () |
 \  ^  /
  |||||
  |||||''')
        break
    else :
        print('senha incorreta')
