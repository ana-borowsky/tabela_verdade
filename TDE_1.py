print("\nBoas vindas!\n")
entrada = input("Digite sua expressão lógica: ")
print("\n")
entradaRecortada = entrada.split(" ")
tabelaVerdade = [["V", "V", "F", "F"],
                 ["V", "F", "F", "V"], 
                 ["F", "V", "V", "F"],
                 ["F", "F", "V", "V"]]

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

def escolheColuna(entradaRecortada):
    colunaP = 0
    colunaQ = 0

    if '~' in entradaRecortada[0]: 
        colunaP = 2
    else:
        colunaP = 0

    if '~' in entradaRecortada[2]: 
        colunaQ = 3
    else:
        colunaQ = 1 
    
    return(colunaP, colunaQ)
    
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

def funcaoE(tabelaVerdade, entrada, entradaRecortada):
    valoresLogicos = [None]*4
    t = tabelaVerdade

    colunaP = escolheColuna(entradaRecortada)[0]
    colunaQ = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaP] == "V" and t[i][colunaQ] == "V":
            valoresLogicos[i] = "V"
        else:
            valoresLogicos[i] = "F"  
    
    valoresLogicosFormatada = [f" {entrada}", \
                               f"   {valoresLogicos[0]}", \
                               f"   {valoresLogicos[1]}", \
                               f"   {valoresLogicos[2]}", \
                               f"   {valoresLogicos[3]}"]

    return valoresLogicosFormatada

def funcaoOu(tabelaVerdade, entrada):
    t = tabelaVerdade
    valoresLogicos = [None]*4
    colunaP = escolheColuna(entradaRecortada)[0]
    colunaQ = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaP] == "V" or t[i][colunaQ] == "V":
            valoresLogicos[i] = "V"
        else:
            valoresLogicos[i] = "F"  
 
    valoresLogicosFormatada = [f" {entrada}", \
                               f"   {valoresLogicos[0]}", \
                               f"   {valoresLogicos[1]}", \
                               f"   {valoresLogicos[2]}", \
                               f"   {valoresLogicos[3]}"]

    return valoresLogicosFormatada

def funcaoImplicacao(tabelaVerdade, entrada):
    t = tabelaVerdade
    valoresLogicos = [None]*4
    colunaP = escolheColuna(entradaRecortada)[0]
    colunaQ = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaP] == "V" and t[i][colunaQ] == "F":
            valoresLogicos[i] = "F"
        else:
            valoresLogicos[i] = "V"  

    valoresLogicosFormatada = [f" {entrada}", \
                               f"   {valoresLogicos[0]}", \
                               f"   {valoresLogicos[1]}", \
                               f"   {valoresLogicos[2]}", \
                               f"   {valoresLogicos[3]}"]

    return valoresLogicosFormatada

def funcaoBiImplicacao(tabelaVerdade, entrada):
    t = tabelaVerdade
    valoresLogicos = [None]*4
    colunaP = escolheColuna(entradaRecortada)[0]
    colunaQ = escolheColuna(entradaRecortada)[1]

    for i in range(0,4):
        if t[i][colunaP] != t[i][colunaQ]:
            valoresLogicos[i] = "F"
        else:
            valoresLogicos[i] = "V"  

    valoresLogicosFormatada = [f" {entrada}", \
                               f"   {valoresLogicos[0]}", \
                               f"   {valoresLogicos[1]}", \
                               f"   {valoresLogicos[2]}", \
                               f"   {valoresLogicos[3]}"]

    return valoresLogicosFormatada

tabela = formataTabelaVerdade(tabelaVerdade, entradaRecortada)
teste = funcaoE(tabelaVerdade, entrada, entradaRecortada)

for i in range(0,5):
    print( tabela[i][0],tabela[i][1], tabela[i][2], tabela[i][3], teste[i]) 

#print(tabela)



















