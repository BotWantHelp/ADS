#Praticando if, elif, else------------------------------------------------

login = input("Digite o seu login:")
senha = input("Digite sua senha: ")

if login == "rapha" and senha == "rapha":  # SE atender essa condição irá exibir Bem-vindo Rapha
    print("Bem-vindo Rapha")
elif login == "naty" and senha == "naty":  # OU SE atender essa condição irá exibir Bem-vinda Naty
    print("Bem-vinda Naty")
else:                                      # SE NAO atender nenhuma vai exibir Login Falhou
    print("Login falhou!")
    
