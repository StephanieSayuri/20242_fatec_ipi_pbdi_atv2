def menu():
    texto="0-fechar\n1-login\n2-logoff"
    usuario = None
    op= int (input(texto))
    while op != 0:
        if op == 1:
            login = input ("Digite seu login \n")
            senha = input ("Digite sua senha \n ")
            usuario = Usuario(login, senha)
            print ("Usuário OK!" if existe (usuario) else "Usuário NOK!")
        elif op == 2:
            usuario = None
            print ("Logoff realizado com sucesso")
        elif op == 3:
            #permitir o cadastro de um novo usuário
            pass
        op = int (input(texto))
    else:
        print('Até mais')