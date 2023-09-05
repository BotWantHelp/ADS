# Similar ao Switch case o Python possui o match case, porem ele só retorna similaridades

estacao = "outono"

match estacao:
    
    case "primavera":
        print("Estação das Flores")
    case "verao":
        print("O Verao é quente")
    case "inverno":
        print("Estação das Flores")
    case "outono":
        print("O outono é sempre igual, as floques caem no quintal")
    case _:
        print("Digite uma estação válida")
        
#--------Segue Gambiarra para usar "Switch Case"---------------------------------------

def case_primavera():
    return "Estação das Flores"

def case_outono():
    return "O outono é sempre igual, as floques caem no quintal"

def switch_case_example(argument):
    switcher = {
        1: case_primavera,
        2: case_outono,
    }
    return switcher.get(argument)()

print(switch_case_example(2)) 

        