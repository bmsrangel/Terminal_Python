# Faça um programa de vendas em um shopping, neste programa terá lojas de: roupas,
# atacados, comida, óculos, sorveteria, açaí, carros, eletrónicos. Dentro de um desses tipos terá as
# lojas, exemplo, nas roupas terá a loja do Paraíba; na de eletronico terá a magazineluiza, tem que ser
# no mínimo 3 lojas. Aí nas lojas terá os produtos, no mínimo 15 produtos. Continuando...
# Nessas lojas terão os vendedores que, claro, venderão o produto. A pessoa escolherá  o produto, vários
# produtos até a pessoa dizer que não quer mais produtos e aí pedirá pra passar no caixa, e o vendedor deverá
# passar no caixa(No caixa terá que ter aleatórias pessoas na frente, 5 por exemplo, no máximo 10) aí quando
# passar os produtos perguntará se quer comprar mais produtos(Não poderá ter os produtos que foram comprados
# logo pelo usuário) Aí se ele sair da loja Deverá voltar shopping(menu, no programa).
# O usuário começará com R$2.000. Para aumentar o dinheiro, haverá dois bancos.

import classes.banco as b
import classes.lojas as l

categorias = l.categorias


def cats():
    c = 2
    aux = ['financeiro']
    print('[ 1 ] Financeiro')
    for k, v in categorias.items():
        print(f'[ {c} ] {k.title()}')
        aux.append(k)
        c += 1
    while True:
        try:
            cat = int(input('\nInforme sua categoria: '))
            break
        except ValueError:
            print('Por favor, informe uma opção válida')
    cat = aux[cat-1]

    return cat


while True:
    print('-' * 30)
    print(f'{"Shopping Tchururu":^30}')
    print('-' * 30, '\n')
    c = cats()
    if c == 'financeiro':
        loja = b.BancoBmsr()
        loja.menu()
    else:
        loja = l.Lojas(c)
        loja.storeList()
