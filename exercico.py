usuario = str(input('digite o seu nome de usuário: ')).strip()
senha = str(input('digite sua senha: ')).strip() 
if senha == usuario:
    print('sua senha não pode ser igual ao seu nome de usuario')
