def vendas(qnt_produto, vl_produto, moeda="real", acrescimo=0, desconto=0):
    # conversão de moeda
    if moeda == "euro":
        vl_produto = vl_produto * 5.70
    elif moeda == "dolar":
        vl_produto = vl_produto * 5

    # calculo do valor de vendas
    total_de_vendas = vl_produto * qnt_produto

    # calculo de desconto
    if acrescimo != 0:
        acrescimo_total = (vl_produto * acrescimo/100)
        total_de_vendas = vl_produto + acrescimo_total
        
    elif desconto != 0:
        desconto_total = (vl_produto * desconto/100)
        total_de_vendas = vl_produto - desconto_total

    print("Valor do produto (por unidade):", vl_produto)
    print("Quantidade de produtos vendidos:", qnt_produto)
    print("Valor total de vendas:", total_de_vendas)

    return total_de_vendas

vendas(qnt_produto=1500, vl_produto=10, moeda="dolar") ## Modificando aqui voce altera os valores dos prints