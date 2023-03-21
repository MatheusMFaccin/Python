
import re


# dicionário que irá conter as posições das variáveis 
variaveis_posicoes = {}

# lista que irá conter os coeficientes do sistema
coeficientes = []

# lista que irá conter os resultados do sistema (lado direito)
resultados = []


# funcao para printar um sistema passado pelo parâmetro matriz, junto ao seu resultado
def print_sistema(matriz, resultado):
    
    # inicializa uma string sistema vazia, onde toda a string do sistema será montada
    sistema = ""
    
    # itera por todos os índices da matriz, onde i é o índice (0, 1, 2, ...)
    for i in range(len(matriz)):
        
        # inicializa uma string linha vazia, onde a string de cada linha do sistema será montada
        linha = ""
        
        # itera por todos os índices de cada índice da matriz, onde j é o índice (0, 1, 2, ...)
        for j in range(len(matriz[i])):
            
            # pega o coeficiente atual
            coef = matriz[i][j]
            
            # se esse coeficiente não for 0
            if coef != 0:
                
                # se esse coeficiente é maior do que 0 e o tamanho da linha também (não é o primeiro índice)
                if coef > 0 and len(linha) > 0:
                    
                    # adiciona "+ " à string linha
                    linha += "+ "
                
                # se esse coeficiente é menor do que 0
                elif coef < 0:
                    
                    # adiciona "- " à string linha
                    linha += "- "
                
                # se o módulo do coeficiente for diferente de 1 
                if abs(coef) != 1:
                    
                    # adiciona a string do coeficiente na linha
                    linha += str(coef) + " "
                
                # adiciona o "nome" da variável na linha
                linha += variaveis_posicoes[j] + " "
                
        # ao fim do loop, adiciona o valor do resultado da linha atual do sistema
        linha += "= " + str(resultado[i])

        # adiciona uma quebra de linha à string sistema
        sistema += linha + "\n"
    
    # printa a string sistema
    print(sistema)    
                 
                  
# função para extrair de uma string (passada pelo parâmetro expressao) os coeficientes de um sistema
def get_coefs(expressao):
    
    # transforma o dict ({0:"x1", 1:"x2", ...}) em uma lista dos valores do dict (["x1", "x2", ...])
    vars = list(variaveis_posicoes.values())

    # transforma a lista em uma string formatada da seguinte maneira: "x1|x2|x3..."
    onde_splitar = "|".join(vars)  
    
    # splita a expressão nas variáveis do sistema. Ex.: "2x1+3x2-x3" -> ["2", "+3", "-", ""]
    coefs = re.split(onde_splitar,expressao)
    
    # tira a última posição da lista coefs pois será uma string vazia
    coefs = coefs[:-1]

    print(coefs)

    # lista temporária que irá conter os valores dos coeficientes
    valores_coefs = []
    
    # pra cada coef na var coefs
    for coef in coefs:
        
        # se o tamanho da string for menor q 2 (ela é "", "+" ou "-")
        if len(coef) < 2:
            
            # adiciona "1" na string coef (ficando "1", "+1" ou "-1")
            if not coef.isdigit():
                coef += "1"
        
        # transforma em float o coef (ficando 1.0, 1.0 ou -1.0)
        valores_coefs.append(float(coef))
    
    # pra cada variavel do sistema
    for var in vars:
        
        # se a variavel não ta na expressao
        if var not in expressao:
            
            # pega a posição da variável na lista vars
            index = vars.index(var)
            
            # insere 0.0 na posição da variável
            valores_coefs.insert(index, 0.0)
    
    # appenda a lista para a variável coeficientes
    coeficientes.append(valores_coefs)


# função para extrair de uma string (passada pelo parâmetro expressao) as variáveis de um sistema
def get_vars(expressao):
    
    # transforma a string da expressão em uma list com cada caractere individual
    elementos = list(expressao)

    # variável que irá definir se o programa está lendo uma variável ou não
    pegando_var = False
    
    # índice da string expressão
    index = 0
    
    # lista que irá conter cada variável da EXPRESSÃO (linha do txt)
    vars = []
    
    # string que será o nome da variável
    var = ''
    
    # loop que passará por cada char da lista elementos
    for char in elementos:
        
        # se for o primeiro char
        if index == 0:
            
            # se o char não for "-"
            if not char == '-':
                
                # se o char não for um dígito (é letra)
                if not char.isdigit():   
                    
                    # adiciona o char à string var
                    var += char
                    
                    # sinaliza que está lendo uma variável
                    pegando_var = True
                    
        # se nao for o primeiro char
        else:
            
            # se não ta lendo variável
            if not pegando_var:
                
                # se o char for número ou "+" ou "-"
                if char.isdigit() or char == "+" or char == "-":
                    
                    # volta do começo do loop (ignora o char atual)
                    continue
                
                # se não for digito, nem "+" nem "-"
                else: 
                    
                    # adiciona o char à string var
                    var += char
                    
                    # sinaliza que está lendo uma variável
                    pegando_var = True
                    
            # se ta pegando variável
            else:
                
                # se o char for um "+" ou um "-"
                if char == "+" or char == "-":
                    
                    # guarda a variável salva até agora na lista vars
                    vars.append(var)
                    
                    # limpa a string var
                    var = ''
                    
                    # sinaliza que parou de ler uma variável (estará lendo um número)
                    pegando_var = False
                    
                # se for qualquer digito tirando "+" ou "-"
                else:
                    
                    # adiciona o char na string var
                    var += char
                    
        
        # aumenta o index da lista a cada iteração do loop    
        index += 1    

    # a última variável da linha não é inserida durante o for, então é feito um append quando o loop termina
    vars.append(var)   
    
    # chama a função check_vars para determinar se a variáveis da expressão já estão em suas devidas posições
    check_vars(vars)
    
    
# checa se as variáveis na lista vars (passada por parâmetro) estão na posição correta no dict variaveis_posicoes
def check_vars(vars):
    
    # itera por cada var na lista vars (passada por parâmetro)
    for var in vars:
        
        # encontra o index da variável RELATIVO À LISTA VARS
        indice = vars.index(var)
        
        # se o índice da variável da lista não está no dicionário das variáveis
        if indice not in variaveis_posicoes:
            
            # insere a variável na POSIÇÃO DO ÍNDICE DA LISTA VARS
            variaveis_posicoes[indice] = var
            
        # se o índice está na lista
        else:
            
            # pega a variável que está no mesmo índice no dicionário
            v = variaveis_posicoes[indice]
            
            # se não for a mesma variável
            if v != var:
                
                # e se a variável do dicionário está na lista vars
                if v in vars:
                    
                    # e se, na lista vars, o index da variável do dict for maior do que o índice da variável atual
                    if vars.index(v) > indice:
                        
                        # insere no dict a variável atual na posição do índice dela
                        variaveis_posicoes[indice] = var
  

# abre o arquivo passado pelo parâmetro 'caminho' e lê os sistemas desse arquivo
def abrir_arquivo(caminho):
    
    # abre o arquivo no modo leitura
    dados = open(caminho, 'r')
    
    # inicializa uma lista que conterá os lados esquerdos
    lados_esq = []
    
    # itera por cada linha do arquivo
    for linha in dados:
        
        # limpa a direita de cada linha do arquivo (remove os \n)
        linha = linha.rstrip()
        
        # splita a linha no símbolo "="
        elementos = linha.split("=")
    
        # pega o lado esquerdo da expressão
        lado_esq = elementos[0]
        
        # pega o lado direito da expressão
        lado_dir = elementos[1]
        
        # printa a linha, o lado esquerdo e o lado direito da expressão respectivamente
        print("Expressão: {}".format(linha))
        print("Lado esquerdo: {}".format(lado_esq))
        print("Lado direito: {}".format(lado_dir))
        
        # appenda o lado direito da expressão na lista resultados
        resultados.append(float(lado_dir))
        
        # appenda o lado esquerdo da espressão na lista lados_esq
        lados_esq.append(lado_esq)

        # chama a função get_vars para o lado esquerdo da expressão
        get_vars(lado_esq)
        print()

    # para cada lado esquerdo na lista lados_esq
    for lado_esq in lados_esq:
        
        # chama a funcção get_coefs para o lado_esq
        get_coefs(lado_esq)
        
    print()
    
    # printa as posições das variáveis
    print(variaveis_posicoes)
    print()
    
    # para cada lista de coeficientes na lista coeficientes
    for coef in coeficientes:
        
        # printa a lista de coeficientes
        print(coef)
        
    print()  
    

print()
def printMatriz(matriz):
    for linha in range(len(matriz)):
        print("\n")
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna])



def escalonamento(matriz):
    #os dois for para ler a matriz
    for linha in range(len(matriz)):    
        for coluna in range(len(matriz[linha])):
            # para encontrar os valores da diagonal principal em suas posiçoes no caso [0.0] [1.1] [2.2] [3.3] [4.4] ... [m.n] 
            if linha == coluna: # se for a diagonal principal
                lst = matriz[linha][coluna] #pega o valor da posição e verifica se é diferente de 1
                if lst != 1: #se for diferente de 1 ele divide o valor por ele mesmo para ficar igual a 1
                    matriz[linha][coluna] = matriz[linha][coluna]/lst
                    print("resultado: ",str(matriz[linha][coluna]))
                    
    printMatriz(matriz)


# chama a função abrir arquivo
abrir_arquivo("equacoes.txt")
print("matriz antes da função: \n")
printMatriz(coeficientes)
escalonamento(coeficientes)
# chama a função print_sistema
print("matriz depois da função: \n")
printMatriz(coeficientes)
print_sistema(coeficientes,resultados)