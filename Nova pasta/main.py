nomesVariaveis = {} #dicionario com o nome das variaveis
def insereVariavel(variavel1):
    if variavel1 not in nomesVariaveis:
        nomesVariaveis[variavel1]="sim"

def separaCoef_var(termo):
    tamanho = len(termo)
    coef = ""
    indice = 0
    variavel = ''
    for letra in termo:
        if(letra.isdigit()):
            coef = coef+letra
            indice+=1
        else:
            if indice == 0: #a primeira letra não eh numero
                coef='1'
            variavel = termo[indice:]
            break
    return coef,variavel

def dividirLE(le):
    #iremos quebrar o lado esquerdo pelos simbolos + e -
    if le.find('+')>0: #busco o sinal de + no codigo
        variaveis = le.split('+')
        print('variaveis (+)', variaveis[0],'|',variaveis[1])
        c,v = separaCoef_var(variaveis[0])
        insereVariavel(v)
        c,v = separaCoef_var(variaveis[1])
        insereVariavel(v)
    if le.find('-')>=0:#busco o sinal de - no le
        variaveisN = le.split('-')
        #print('num de -:',len(variaveisN))
        if len(variaveisN)==2:
            print('Variaveis (-)->',variaveisN[0],'|',variaveisN[1])
            c,v = separaCoef_var(variaveis[0])
            insereVariavel(v)
            c,v = separaCoef_var(variaveis[1])
            insereVariavel(v)
        elif len(variaveisN)==3:
            print('Variaveis (-)->',variaveisN[1],'|',variaveisN[2])
    
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
print(nomesVariaveis.keys)
