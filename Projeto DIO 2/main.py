# Olá, seja bem-vindo(a) ao meu segundo Projeto DIO.

import time

# Informações do criador do script
print("Script feito por Luis!")
time.sleep(1)

# Função "script", é usada para o usuário calcular seu saldo de Rankeadas.
def script():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    # Apresentações para o usuário.
    print(
        "Olá bravo(a) guerreiro(a)! Seja bem-vindo(a) novamente ao nosso QG de heróis de Farland City!",
        "Aqui você fará um relatório de Rankeadas, apresentando seu nome, quantidade de vitórias e derrotas."
          )
    
    # Variável pedindo o nome do herói.
    nomeHeroi = input("\nBom. Para iniciarmos, por favor, digite o seu NOME:\n>>>\t")

    # Variáveis que pedem a quantia de VITÓRIAS e DERROTAS do herói.
    vitoriasHeroi = int(input("Agora diga a quantidade de VITÓRIAS que você teve:\n>>>\t"))
    derrotasHeroi = int(input("E para calcularmos o seu relatório, diga a quantidade de DERROTAS que você teve:\n>>>\t"))
    
    
    
    
    # Função que faz todo o cálculo de rankeadas e afins
    def rankeadasH(vitoriasHeroi,derrotasHeroi):
        # Variável que guarda o NÍVEL do herói.
        nivelH = None
        rankeadasH = vitoriasHeroi - derrotasHeroi
        
        # Estrutura de decisão para decidir o NÍVEL do herói.
        if rankeadasH < 10:
            nivelH = "Ferro"
        elif rankeadasH >= 11 and rankeadasH <= 20:
            nivelH = "Bronze"
        elif rankeadasH >= 21 and rankeadasH <= 50:
            nivelH = "Prata"
        elif rankeadasH >= 51 and rankeadasH <= 80:
            nivelH = "Ouro"
        elif rankeadasH >= 81 and rankeadasH <= 90:
            nivelH = "Diamante"
        elif rankeadasH >= 91 and rankeadasH <= 100:
            nivelH = "Lendário"
        else:
            nivelH = "Imortal"
        
        return nivelH, rankeadasH

    nivelHeroi, rankeadasHeroi = rankeadasH(vitoriasHeroi, derrotasHeroi)
        
    print("Calculando relatório de Herói...")
    time.sleep(0.125)
    print("25%")
    time.sleep(0.5)
    print("50%")
    time.sleep(0.5)
    print("75%")
    time.sleep(0.5)
    print("99%")
    time.sleep(1)
    print("100%")
    time.sleep(0.125)
    
    
    # Saída dos dados
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-------------------- RELATÓRIO DE HERÓI --------------------"
        f"\nNome: {nomeHeroi}"
        f"\nNível do Herói: {nivelHeroi}"
        f"\nRankeadas do Herói: {rankeadasHeroi} ( VITÓRIAS = {vitoriasHeroi} | DERROTAS = {derrotasHeroi} )"
        "\nUse esse relatório com suas INFORMAÇÕES para conseguir trabalhos de acordo com seu nível."
        "\n-------------------- RELATÓRIO DE HERÓI --------------------"
    )
    
script()