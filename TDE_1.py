# p -> q
# ~p or q
 
# p <-> q 
# p -> q and q -> ~q
# (~p or q ) and (~p or q)

entrada = "~p <-> q"
entradaUsuario = entrada.split(" ")
tabelaVerdade = [["V", "V", "F", "F"],
                 ["V", "F", "F", "V"], 
                 ["F", "V", "V", "F"],
                 ["F", "F", "V", "V"]]
primeiraLetra = None
segundaLetra = None

def pegaLetras(entradaUsuario):
    if len(entradaUsuario[0]) != 1:
        primeiraLetra = entradaUsuario[0][1]

    else:
        primeiraLetra = entradaUsuario[0]

    if len(entradaUsuario[2]) != 1:
        segundaLetra = entradaUsuario[2][1]

    else:
        segundaLetra = entradaUsuario[2]

    return(primeiraLetra, segundaLetra)

def escolheColuna(entradaUsuario):
    colunaP = 0
    colunaQ = 0

    if '~' in entradaUsuario[0]: 
        colunaP = 2
    else:
        colunaP = 0

    if '~' in entradaUsuario[2]: 
        colunaQ = 3
    else:
        colunaQ = 1 
    
    return(colunaP, colunaQ)
    
def formataTabelaVerdade(tabelaVerdade, entradaUsuario):    
    t = tabelaVerdade   
    primeiraLetra = pegaLetras(entradaUsuario)[0]
    segundaLetra = pegaLetras(entradaUsuario)[1]

    tabelaVerdadeFormatada = [[f"|  {primeiraLetra} ", f"|  {segundaLetra} ", f"|  ~{primeiraLetra} ", f"|  ~{segundaLetra}  |"], \
                              [f"|  {t[0][0]} ", f"|  {t[0][1]} ", f"|  {t[0][2]}  ", f"|  {t[0][3]}   |"], \
                              [f"|  {t[1][0]} ", f"|  {t[1][1]} ", f"|  {t[1][2]}  ", f"|  {t[1][3]}   |"], \
                              [f"|  {t[2][0]} ", f"|  {t[2][1]} ", f"|  {t[2][2]}  ", f"|  {t[2][3]}   |"], \
                              [f"|  {t[3][0]} ", f"|  {t[3][1]} ", f"|  {t[3][2]}  ", f"|  {t[3][3]}   |"]]

    return tabelaVerdadeFormatada

def funcao_e(tabelaVerdade, entradaUsuario):
    #tabc = [f" {entrada}  |", "   V    |","   F    |","   F    |","   F    |"]
    t = tabelaVerdade
    valores_logicos = [None]*4

    colunaP = escolheColuna(entradaUsuario)[0]
    colunaQ = escolheColuna(entradaUsuario)[1]

    for i in range(0,4):
        if t[i][colunaP] == "V" and t[i][colunaQ] == "V":
            valores_logicos[i] = "V"
        else:
            valores_logicos[i] = "F"  

    return valores_logicos

def funcao_ou(tabelaVerdade, entrada):
    # tghi = [f" {entrada}  |", "   V    |","   V    |","   V    |","   F    |"]
    t = tabelaVerdade
    valores_logicos = [None]*4
    colunaP = escolheColuna(entradaUsuario)[0]
    colunaQ = escolheColuna(entradaUsuario)[1]

    for i in range(0,4):
        if t[i][colunaP] == "V" or t[i][colunaQ] == "V":
            valores_logicos[i] = "V"
        else:
            valores_logicos[i] = "F"  
 
    return valores_logicos

def funcao_implicacao(tabelaVerdade, entrada):
    #implicacao = [f"  {entrada}  |", "    V     |","    F     |","    V     |","    V     |"]
    t = tabelaVerdade
    valores_logicos = [None]*4
    colunaP = escolheColuna(entradaUsuario)[0]
    colunaQ = escolheColuna(entradaUsuario)[1]

    for i in range(0,4):
        if t[i][colunaP] == "V" and t[i][colunaQ] == "F":
            valores_logicos[i] = "F"
        else:
            valores_logicos[i] = "V"  

    return valores_logicos

def funcao_bi_implicacao(tabelaVerdade, entrada):
    #biimplicacao = [f"{entrada}    |", "      V      |","      F      |","      F      |","      V      |"]
    t = tabelaVerdade
    valores_logicos = [None]*4
    colunaP = escolheColuna(entradaUsuario)[0]
    colunaQ = escolheColuna(entradaUsuario)[1]

    for i in range(0,4):
        if t[i][colunaP] != t[i][colunaQ]:
            valores_logicos[i] = "F"
        else:
            valores_logicos[i] = "V"  

    return valores_logicos



# tabela = imprimeTabela(entradaUsuario)

# implicacao = implicacao(tabela, entrada)

# tabc = abc(tabela, entrada)

# tghi = abc(tabela, entrada)
tabela = formataTabelaVerdade(tabelaVerdade, entradaUsuario)
biImplicacao = funcao_bi_implicacao(tabelaVerdade, entrada)

for i in range(0,5):
    print( tabela[i][0],tabela[i][1], tabela[i][2], tabela[i][3]) 

#print(tabela)



















