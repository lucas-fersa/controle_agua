# Controle de nível de água em um reservatório
# Autor: Lucas Fersa (Revisado pelo Professor)

# Bibliotecas
from colorama import Fore, Style, init

# Inicializa o colorama para compatibilidade entre sistemas
init()

# Função responsável por definir a mensagem e a cor conforme o nível informado
def obter_alerta_nivel(nivel):
    if nivel == 1:
        return Fore.RED + f"Nível de água {nivel}: Muito baixo (crítico)"
    elif nivel == 2:
        return Fore.YELLOW + f"Nível de água {nivel}: Baixo"
    elif nivel == 3:
        return Fore.GREEN + f"Nível de água {nivel}: Médio"
    elif nivel == 4:
        return Fore.CYAN + f"Nível de água {nivel}: Alto"
    elif nivel == 5:
        return Fore.BLUE + f"Nível de água {nivel}: Muito alto (alerta)"
    else:
        return "Nível desconhecido"

# Lista com os níveis do reservatório
niveis_reservatorio = [1, 2, 3, 4, 5]

print("--- Iniciando Monitoramento do Reservatório ---")

# Simulação do monitoramento percorrendo a lista
for nivel in niveis_reservatorio:
    # Chama a função que define a cor e exibe o resultado
    print(obter_alerta_nivel(nivel))

# Restaura o estilo padrão do terminal ao finalizar
print(Style.RESET_ALL + "\nControle de nível de água concluído.")