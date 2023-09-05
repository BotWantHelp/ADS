#Estruturas condicionais: if, elif, else------------------------------------------------

codigo_compra = 0000

if   codigo_compra == 5222:               # SE atender ao codigo_compra Igual a 5222
    print("Compra a vista.")
elif codigo_compra == 5333:               # OU SE for Igual a 5333
    print("Compra a prazo no boleto.")
elif codigo_compra == 5444:               # OU SE for Igual a 5444 
    print("Compra a prazo no cartão.")
else:                                     # Se não atender merda nenhuma
    print("Codigo não cadastrado")
