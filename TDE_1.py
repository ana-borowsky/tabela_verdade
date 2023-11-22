# Aluna Ana Paula Borowsky de Borba
# Exemplos de entradas aceitas: "p ^ q", "a V ~b", "p -> ~q", "~a <-> b"
# O programa funciona de uma maneira diferente da pedida pelo professor no trabalho, o que pode diminuir a nota, porém deixaria o trabalho 
# mais interessante de ser feito e melhoraria a compreensão da matéria.
# O programa lê a entrada do usuário e verifica qual foi o conectivo utilizado.
# Então o programa irá calcular os valores lógicos conforme o conectivo e se a letra está sendo negada ou não.
# O programa então gera a tabela verdade formatada de acordo com a entrada do usuário.

print("\nBoas vindas!\n\nVocê pode usar os seguintes conectivos: ^, v, -> e <->, \
       \ne pode usar o símbolo de negação. Não use parênteses! \
       \nUse espaço entre as letras e o conectivo. \
       \nEste programa aceita apenas um conectivo. ")
entrada = input("\nDigite sua expressão lógica: ")
print("\n")
entradaRecortada = entrada.split(" ")
tabelaVerdade = [["V", "V", "F", "F"],
                 ["V", "F", "F", "V"], 
                 ["F", "V", "V", "F"],
                 ["F", "F", "V", "V"]]

# Verifica quais são as letras que o usuário digitou para poder usar na impressão das tabelas formatadas.
def pegaLetras(entradaRecortada):
    primeiraLetra = None
    segundaLetra = None

    if len(entradaRecortada[0]) != 1:
        primeiraLetra = entradaRecortada[0][1]

    else:
        primeiraLetra = entradaRecortada[0]

    if len(entradaRecortada[2]) != 1:
        segundaLetra = entradaRecortada[2][1]

    else:
        segundaLetra = entradaRecortada[2]

    return(primeiraLetra, segundaLetra)

# Escolhe se os valores lógicos a serem pegos serão da coluna 'p' ou '~p' por exemplo.
def escolheColuna(entradaRecortada):
    colunaPrimeiraLetra = 0
    colunaSegundaLetra = 0

    if '~' in entradaRecortada[0]: 
        colunaPrimeiraLetra = 2
    else:
        colunaPrimeiraLetra = 0

    if '~' in entradaRecortada[2]: 
        colunaSegundaLetra = 3
    else:
        colunaSegundaLetra = 1 
    
    return(colunaPrimeiraLetra, colunaSegundaLetra)

# Formata a matriz tabela verdade para poder imprimir de forma mais bonitinha na tela. 
# Também faz o cabeçalho de acordo com a entrada do usuário.
def formataTabelaVerdade(tabelaVerdade, entradaRecortada):    
    t = tabelaVerdade   
    primeiraLetra = pegaLetras(entradaRecortada)[0]
    segundaLetra = pegaLetras(entradaRecortada)[1]

    tabelaVerdadeFormatada = [[f"  {primeiraLetra} ", f"|  {segundaLetra} ", f"|  ~{primeiraLetra} ", f"|  ~{segundaLetra}  |"], \
                              [f"  {t[0][0]} ", f"|  {t[0][1]} ", f"|  {t[0][2]}  ", f"|  {t[0][3]}   |"], \
                              [f"  {t[1][0]} ", f"|  {t[1][1]} ", f"|  {t[1][2]}  ", f"|  {t[1][3]}   |"], \
                              [f"  {t[2][0]} ", f"|  {t[2][1]} ", f"|  {t[2][2]}  ", f"|  {t[2][3]}   |"], \
                              [f"  {t[3][0]} ", f"|  {t[3][1]} ", f"|  {t[3][2]}  ", f"|  {t[3][3]}   |"]]

    return tabelaVerdadeFormatada

# É a função do E
def funcaoE(tabelaVerdade, entrada, entradaRecortada):
    valoresLogicos = [None]*4
    t = tabelaVerdade

    colunaPrimeiraLetra = escolheColuna(entradaRecortada)[0]
    colunaSegundaLetra = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaPrimeiraLetra] == "V" and t[i][colunaSegundaLetra] == "V":
            valoresLogicos[i] = "V"
        else:
            valoresLogicos[i] = "F"  
    
    valoresLogicosFormatada = [f" {entrada}", \
                               f"   {valoresLogicos[0]}", \
                               f"   {valoresLogicos[1]}", \
                               f"   {valoresLogicos[2]}", \
                               f"   {valoresLogicos[3]}"]

    return valoresLogicosFormatada

# É a função do OU
def funcaoOu(tabelaVerdade, entrada, entradaRecortada):
    t = tabelaVerdade
    valoresLogicos = [None]*4
    colunaPrimeiraLetra = escolheColuna(entradaRecortada)[0]
    colunaSegundaLetra = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaPrimeiraLetra] == "V" or t[i][colunaSegundaLetra] == "V":
            valoresLogicos[i] = "V"
        else:
            valoresLogicos[i] = "F"  
 
    valoresLogicosFormatada = [f" {entrada}", \
                               f"   {valoresLogicos[0]}", \
                               f"   {valoresLogicos[1]}", \
                               f"   {valoresLogicos[2]}", \
                               f"   {valoresLogicos[3]}"]

    return valoresLogicosFormatada

# É a função da IMPLICAÇÃO
def funcaoImplicacao(tabelaVerdade, entrada, entradaRecortada):
    t = tabelaVerdade
    valoresLogicos = [None]*4
    colunaPrimeiraLetra = escolheColuna(entradaRecortada)[0]
    colunaSegundaLetra = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaPrimeiraLetra] == "V" and t[i][colunaSegundaLetra] == "F":
            valoresLogicos[i] = "F"
        else:
            valoresLogicos[i] = "V"  

    valoresLogicosFormatada = [f" {entrada}", \
                               f"   {valoresLogicos[0]}", \
                               f"   {valoresLogicos[1]}", \
                               f"   {valoresLogicos[2]}", \
                               f"   {valoresLogicos[3]}"]

    return valoresLogicosFormatada

# É a função da BI-IMPLICAÇÃO
def funcaoBiImplicacao(tabelaVerdade, entrada, entradaRecortada):
    t = tabelaVerdade
    valoresLogicos = [None]*4
    colunaPrimeiraLetra = escolheColuna(entradaRecortada)[0]
    colunaSegundaLetra = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaPrimeiraLetra] != t[i][colunaSegundaLetra]:
            valoresLogicos[i] = "F"
        else:
            valoresLogicos[i] = "V"  

    valoresLogicosFormatada = [f" {entrada}", \
                               f"    {valoresLogicos[0]}", \
                               f"    {valoresLogicos[1]}", \
                               f"    {valoresLogicos[2]}", \
                               f"    {valoresLogicos[3]}"]

    return valoresLogicosFormatada

print("Aqui está o resultado!\n")

tabelaVerdadeFormatada = formataTabelaVerdade(tabelaVerdade, entradaRecortada)

# Detecta o conectivo e chama a função de acordo.
if entradaRecortada[1] == "^":
    tabelaVerdadeDoUsuario = funcaoE(tabelaVerdade, entrada, entradaRecortada)

if entradaRecortada[1] == "V" or entradaRecortada[1] == "v":
    tabelaVerdadeDoUsuario = funcaoOu(tabelaVerdade, entrada, entradaRecortada)

if entradaRecortada[1] == "->":
    tabelaVerdadeDoUsuario = funcaoImplicacao(tabelaVerdade, entrada, entradaRecortada)

if entradaRecortada[1] == "<->":
    tabelaVerdadeDoUsuario = funcaoBiImplicacao(tabelaVerdade, entrada, entradaRecortada)

# Imprime a tabela final formatada.
for i in range(0,5):
    print( tabelaVerdadeFormatada[i][0],tabelaVerdadeFormatada[i][1], tabelaVerdadeFormatada[i][2], tabelaVerdadeFormatada[i][3], tabelaVerdadeDoUsuario[i]) 