print("Login")

usuario = input("Digite seu usuário: ")
    
if usuario != "admin":
    print("Usuário não encontrado")
    exit()

senha = input("Digite sua senha: ")

if senha != "python123":
    print("Senha incorreta")

else:
    print("Acesso liberado. Bem-vindo, admin!")

