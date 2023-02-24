
#função para dividir o lado esquerdo no sinal de + ou -
def dividirLE(le):
    #iremos quebrar o lado esquerdo pelos simbolos + e -
    if le.find('+')>0: #busco o sinal de + no codigo
        variaveis = le.split('+')
        print('variaveis (+)', variaveis[0],'-',variaveis[1])
    if le.find('-')>=0:
        variaveisN  = le.split('-')
        if len((variaveisN)==2):
            print('variaveis (-)', variaveis[0],'-',variaveis[1])
        if len((variaveisN)==3):
            print('variaveis (-)', variaveis[1],'-',variaveis[2])
#função para dividir a linha no igual       
def dividirLinha(linha):
    elementos = linha.split('=')
    elementos = linha.split('=')#quebra a linha no igual
    le = elementos[0]
    ld = elementos[1]        
    print('LE:',le,"LD:", ld)
    dividirLE(le)
    
def abre_arquivo(nomeArquivo):
    dados = open(nomeArquivo)
    for linha in dados: #percorre linha a linha do arquivo
        print(linha)
        dividirLinha(linha)
        

nomeArquivo = "equacoes.txt"


abre_arquivo(nomeArquivo)




