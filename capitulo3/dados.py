import csv
import os


def carregar_acessos():
    X = []
    Y = []

    cwd = os.path.dirname(__file__)  # get current location of script
    arquivo = open(cwd + '/acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    
    next(leitor)

    for home, como_funciona, contato, comprou in leitor:

        dado = [int(home), int(como_funciona), int(contato)]
        X.append(dado)
        Y.append(int(comprou))

    return X, Y


def carregar_buscas():

    X = []
    Y = []

    cwd = os.path.dirname(__file__)  # get current location of script
    arquivo = open(cwd + '/buscas.csv', 'r')
    leitor = csv.reader(arquivo)

    next(leitor)

    for home, busca, logado, comprou in leitor:

        dado = ([int(home), busca, int(logado)])
        X.append(dado)
        Y.append(int(comprou))

    return X, Y
