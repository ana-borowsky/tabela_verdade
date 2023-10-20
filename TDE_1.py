# p -> q
# ~p or q
 
# p <-> q 
# p -> q and q -> ~q
# (~p or q )and (~p or q)


t = [["V", "V", "F", "F"],
     ["V", "F", "F", "V"], 
     ["F", "V", "V", "F"],
     ["F", "F", "V", "V"]]

entradaUsuario = "p^q"
    
def imprimeTabela(t, entradaUsuario):

    tabela = ( " +-----+-----+------+------+ \n" \
               f" |  {entradaUsuario[0]}  |  {entradaUsuario[2]}  |  ~{entradaUsuario[0]}  |  ~{entradaUsuario[2]}  |\n" \
               " +-----+-----+------+------+ \n " \
               f"|  {t[0][0]}  |  {t[0][1]}  |   {t[0][2]}  |   {t[0][3]}  | \n" \
               f" |  {t[1][0]}  |  {t[1][1]}  |   {t[1][2]}  |   {t[1][3]}  | \n" \
               f" |  {t[2][0]}  |  {t[2][1]}  |   {t[2][2]}  |   {t[2][3]}  | \n" \
               f" |  {t[3][0]}  |  {t[3][1]}  |   {t[3][2]}  |   {t[3][3]}  | \n" \
               " +-----+-----+------+------+")

    print(tabela)

imprimeTabela(t, entradaUsuario)


