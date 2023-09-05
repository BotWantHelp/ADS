import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()

nome = input("Digite seu nome: ")
guerra_comecou = input("Estamos em GUERRA? (sim ou nao)\n\n: ")
humano = 'Homem'
orientacao = 'Hetero'

if guerra_comecou == 'sim':
    humano = 'Mulher'
    orientacao = 'Lésbica'
    nome += 'a Raiana'
    print(f"\nOie a todes chamo {nome}")
    print(f"Agora me identifico {humano} e sou {orientacao}\n")
else:
    print(f"\nOlá, me chamo {nome}")
    print(f"Não há guerra, {humano} e sou {orientacao}\n")
    
    