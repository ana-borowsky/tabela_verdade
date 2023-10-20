# p -> q
# ~p or q
 
# p <-> q 
# p -> q and q -> ~q
# (~p or q )and (~p or q)

entrada = "p <-> q"
entradaUsuario = entrada.split(" ")
    
def imprimeTabela(entradaUsuario):
    t = [["V", "V", "F", "F"],
         ["V", "F", "F", "V"], 
         ["F", "V", "V", "F"],
         ["F", "F", "V", "V"]]
        
    tabela = [[f"|  {entradaUsuario[0]} ", f"|  {entradaUsuario[2]} ", f"|  ~{entradaUsuario[0]} ", f"|  ~{entradaUsuario[2]}  |"], \
              [f"|  {t[0][0]} ", f"|  {t[0][1]} ", f"|  {t[0][2]}  ", f"|  {t[0][3]}   |"], \
              [f"|  {t[1][0]} ", f"|  {t[1][1]} ", f"|  {t[1][2]}  ", f"|  {t[1][3]}   |"], \
              [f"|  {t[2][0]} ", f"|  {t[2][1]} ", f"|  {t[2][2]}  ", f"|  {t[2][3]}   |"], \
              [f"|  {t[3][0]} ", f"|  {t[3][1]} ", f"|  {t[3][2]}  ", f"|  {t[3][3]}   |"]]
    return tabela

def implicacao(tabela, entrada):
    implicacao = [f"  {entrada}  |", "    V     |","    F     |","    V     |","    V     |"]

    return implicacao

def bi_implicacao(tabela, entrada):
    biimplicacao = [f"{entrada}    |", "      V      |","      F      |","      F      |","      V      |"]

    return implicacao

def abc(tabela, entrada):
    tabc = [f" {entrada}  |", "   V    |","   F    |","   F    |","   F    |"]

    return tabc

def ghi(tabela, entrada):
    tghi = [f" {entrada}  |", "   V    |","   V    |","   V    |","   F    |"]
 
    return tghi

tabela = imprimeTabela(entradaUsuario)

implicacao = implicacao(tabela, entrada)

tabc = abc(tabela, entrada)

tghi = abc(tabela, entrada)

biImplicacao = bi_implicacao(tabela, entrada)

for i in range(0,5):
    print( tabela[i][0],tabela[i][1], tabela[i][2], tabela[i][3], biImplicacao[i]) 












