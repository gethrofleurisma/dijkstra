def resumo():
    mensagem = "Edsger Wybe Dijkstra (1930–2002) foi um renomado cientista da computação holandês, amplamente reconhecido por suas contribuições fundamentais para a ciência da computação teórica e prática."
    return mensagem

def resumo():
    mensagem = "Edsger Wybe Dijkstra (1930–2002) foi um renomado cientista da computação holandês, amplamente reconhecido por suas contribuições fundamentais para a ciência da computação teórica e prática."
    return mensagem

def doutorado():
    mensagem = "Dijkstra obteve seu doutorado na Universidade de Leiden em 1959, com uma tese sobre a solução numérica de equações diferenciais, antes de se dedicar à computação, que na época era um campo emergente."
    return mensagem

def contribuicoes():
    mensagem = "Dijkstra produziu um vasto número de escritos, muitos em forma de notas manuscritas conhecidas como EWDs. Ele frequentemente defendia abordagens matemáticas rigorosas e criticava práticas que não seguiam princípios sólidos de engenharia."
    return mensagem

def artigos():
    mensagem = "Seus artigos e textos tiveram um impacto profundo em áreas como algoritmos, linguagens de programação e fundamentos teóricos da computação. "
    return mensagem

def citacoes():
    mensagem = "A simplicidade é pré-requisito para a confiabilidade; A ciência da computação não trata de computadores, assim como a astronomia não trata de telescópios"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
