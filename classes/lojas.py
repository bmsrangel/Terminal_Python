# atacados, carros
import classes.dbcomms as dbcomms
import os

categorias = {'alimentação': ["bobs", 'burger king', 'subway'], 'vestuário': ['riachuelo', 'renner', 'myplace'],
              'guloseimas': ['point do açaí', 'sol & neve'], 'eletrônicos': ['ponto frio', 'americanas'],
              'acessórios': ['chilli beans'], 'carros': ['land rover', 'porsche'], 'atacados': ['saara', 'casa & cia']}


class Lojas:
    def __init__(self, cat):
        self.cat = cat

    def operacoes(self, loja):
        while True:
            print('[ 1 ] Consulta de preço')
            print('[ 2 ] Acessar PDV')
            print('[ 0 ] Sair')
            menu = int(input('Escolha sua opção: '))

            if menu == 1:
                dbcomms.list_items(loja)
            elif menu == 2:
                self.pdv(loja)
            elif menu == 0:
                break
            else:
                print('Opção inválida')

    def storeList(self):
        if self.cat.isnumeric():
            pass
        else:
            c = 1
            print('Lojas da categoria')
            for i in categorias[self.cat]:
                print(f'[ {c} ] {i.title()}')
                c += 1
            print(f'[ 0 ] Sair')
            while True:
                try:
                    menu = int(input('Selecione uma das lojas acima: '))
                    break
                except ValueError:
                    print('Opção inválida!')
            if menu > 0:
                self.operacoes(categorias[self.cat][menu - 1])
            elif menu == 0:
                return 0
            else:
                print('Opção inválida!')

    def pdv(self, loja):
        venda = list()
        total = 0
        while True:
            cod = int(input('Informe o código do produto (-1 para encerrar): '))
            if cod > 0:
                if dbcomms.busca_pdv(cod, loja) is not None:
                    venda.append(dbcomms.busca_pdv(cod, loja))
                else:
                    print('Código inválido!')
            elif cod == -1:
                print('Encerrando venda...')
                break
            else:
                print('Opção inválida!')
        print('Carrinho:')
        print(f'{"Produto":^30}{"Preço":^10}')
        for i in venda:
            print(f'{i[0]:<30}{i[1]:7.2f}')
            total += i[1]
        print(f'Total da compra: R${total:.2f}')
        self.pagamento(total)

    def pagamento(self, total):
        cpf = str(input('Informe o CPF do cliente: '))
        nome, saldo = dbcomms.saldo_cliente(cpf)
        confirma = str(input('Confirma o pagamento [S/N]? '))
        if confirma in 'sS':
            saldo -= total
            dbcomms.atualizar_saldo(cpf, saldo)


