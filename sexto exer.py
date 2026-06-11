s = 1000.00
for i in iter(int, 1):
    print("--- CAIXA ELETRÔNICO ---")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    o = int(input("Escolha uma opção: "))
    if o == 1:
        print(f"Seu saldo atual é: R$ {s:.2f}")
    elif o == 2:
        vd= float(input("Digite o valor para depósito: R$ "))
        if vd > 0:
            s += vd
            print(f"Depósito de R$ {vd:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    elif o == 3:
        vs = float(input("Digite o valor para saque: R$ ")) 
        if vs <= 0:
            print("Valor inválido")
        elif vs > saldo:
            print("Saldo insuficiente")
        else:
            s -= vs
            print(f"Saque de R$ {vs:.2f} realizado com sucesso!")
    elif o == 4:
        print("Obrigado por usar o nosso caixa eletrônico. Até logo!")
        print(r'''______________________________
                    /                              \
                   /            BANK                \
                  /__________________________________\
                  ||________________________________||
                  ||  __    __    __    __    __    ||
                  || |  |  |  |  |  |  |  |  |  |   ||
                  || |  |  |  |  |  |  |  |  |  |   ||
                  || |  |  |  |  |  |  |  |  |  |   ||
                  || |__|  |__|  |__|  |__|  |__|   ||
                  ||  ||    ||    ||    ||    ||    ||
                  ||  ||    ||  _/\_    ||    ||    ||
                  ||  ||    || | || |   ||    ||    ||
                  ||  ||    || | || |   ||    ||    ||
                  ||__||____||_|_||_|___||____||____||
                 /                                    \
                /______________________________________\
               /________________________________________\
              /__________________________________________\''')
        break  
    else:
        print("Opção inválida! Tente novamente.")
