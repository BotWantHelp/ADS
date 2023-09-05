Jogadores = [
    {'nomes': 'Rapha', 'partidas': 3, 'gols': [1, 0, 1]},
    {'nomes': 'Tiago', 'partidas': 5, 'gols': [5, 8, 7, 4, 9]},
    {'nomes': 'Ronald', 'partidas': 2, 'gols': [23, 103]}
]

for jogador in Jogadores:
    nomes = jogador['nomes']
    partidas = jogador['partidas']
    gols = jogador['gols']

    saldo_gol = sum(gols)

    print(f'Jogador: {nomes}, jogou: {partidas}, marcou: {gols}, saldo de gols: {saldo_gol}')
