import random

def inimigos_vivos(inimigos):
   
    return [inimigo for inimigo in inimigos if inimigo["vida"] > 0]

def mostrar_menu():
    print()
    print("========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")


def atacar(jogador, inimigos):
# devolve 1 se derrotou o inimig 0 caso contrário
    vivos = inimigos_vivos(inimigos)
    if len(vivos) == 0:
        print("Não existem inimigos vivos.")
        return 0

    print("Inimigos vivos:")
    for i in range(len(vivos)):
        print(f"{i + 1} - {vivos[i]['nome']} | Vida: {vivos[i]['vida']} | Ataque: {vivos[i]['ataque']}")


    validos = [str(n) for n in range(1, len(vivos) + 1)]
    escolha = input("Escolha o inimigo: ")

    if escolha not in validos:
        print(f"Escolha inválida! Introduza um número entre 1 e {len(vivos)}.")
        return 0

    alvo = vivos[int(escolha) - 1]

    # ataque jogador
    dano = random.randint(10, 20)
    alvo["vida"] -= dano
    if alvo["vida"] < 0:
        alvo["vida"] = 0
    print(f"Causaste {dano} de dano ao {alvo['nome']}.")