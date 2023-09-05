#Praticando if, elif, else------------------------------------------------

login = input("Digite o seu login:")
senha = input("Digite sua senha: ")

if login == "userpy01" and senha == "teste01":
    print("Bem-vindo userpy01")
elif login == "userpy02" and senha == "teste02":
    print("Bem-vindo userpy02")
elif login == "userpy03" and senha == "teste03":
    print("Bem-vindo userpy03")
elif login == "userpy04" and senha == "teste04":
    print("Bem-vindo userpy04")
else:
    print("Login falhou!")