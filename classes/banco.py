import classes.dbcomms as dbcomms
import os


class BancoBmsr():
    def __init__(self):
        pass

    def menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{"Bem vindo ao banco BMSR":^30}')
        while True:
            cpf = str(input('Informe seu CPF [0 para sair]: '))
            if cpf != '0' and dbcomms.saldo_cliente(cpf) is None:
                print('CPF inválido ou não encontrado!')
            else:
                break
        if cpf != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            nome, saldo = dbcomms.saldo_cliente(cpf)
            print(f'Bem-vindo, {nome}!\nSeu saldo atual é {saldo}.'
                  f'\nO que você gostaria de fazer?')
            while True:
                print('[ 1 ] Sacar')
                print('[ 2 ] Depositar')
                print('[ 0 ] Encerrar')
                menu = int(input('Informe sua operação: '))
                if menu == 1:
                    self.saque(cpf, saldo)
                elif menu == 2:
                    self.deposito(cpf, saldo)
                elif menu == 0:
                    print('Obrigado por usar nossos caixas eletrônicos!!')
                    break
                else:
                    print('Opção inválida!')

    def saque(self, cpf, saldo):
        saque = int(input('Informe o valor a ser sacado: '))
        if saque <= saldo:
            saldo -= saque
            dbcomms.atualizar_saldo(cpf, saldo)
            print(f'Saldo atual: {saldo}')
        else:
            print('Saldo insuficiente para saque!')

    def deposito(self, cpf, saldo):
        deposito = int(input('Valor a ser depositado: '))
        saldo += deposito
        dbcomms.atualizar_saldo(cpf, saldo)
        print(f'Saldo atual: {saldo}')
