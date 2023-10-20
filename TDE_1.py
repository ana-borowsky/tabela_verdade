# p -> q
# ~p or q
 
# p <-> q 
# p -> q and q -> ~q
# (~p or q )and (~p or q)


t = [[True, True, False, False],
     [True, False, False, True], 
     [False, True, True, False],
     [False, False, True, True]]

entradaUsuario = "p^q"
    
def imprimeTabela(t,entradaUsuario):
    line = "+--------+--------+--------+--------+"
    cabecalho = 

    tabela = ( f"|  {t[0][0]}  |  {t[0][1]}  | {t[0][2]}  | {t[0][3]}  | \n" \
               f"|  {t[1][0]}  | {t[1][1]}  | {t[1][2]}  |  {t[1][3]}  | \n" \
               f"| {t[2][0]}  |  {t[2][1]}  |  {t[2][2]}  | {t[2][3]}  | \n" \
               f"| {t[3][0]}  | {t[3][1]}  |  {t[3][2]}  |  {t[3][3]}  |" )

    print(f"{line} \n" \
          \
          f"{line} \n" \
          f"{tabela} \n"
          f"{line} \n" \
          )

imprimeTabela(entradaUsuario)

