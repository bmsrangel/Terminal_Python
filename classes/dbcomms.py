import mysql.connector

# conn = mysql.connector.connect(host="localhost",
#                                database="shopping",
#                                user="root",
#                                password="12345678")
# c = conn.cursor()


def list_items(tabela):
    conn = mysql.connector.connect(host="localhost",
                                   database="shopping",
                                   user="root",
                                   password="12345678")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {tabela}")
    for i in c.fetchall():
        print(f'Código: %s\nProduto: %s\nPreço: R$%.2f' % (i[0], i[1], i[2]))
        print()
    conn.close()


def busca_pdv(cod, tabela):
    conn = mysql.connector.connect(host="localhost",
                                   database="shopping",
                                   user="root",
                                   password="12345678")
    c = conn.cursor()
    c.execute(f"SELECT produto, preco FROM {tabela} WHERE id={cod}")
    res = c.fetchone()
    conn.close()
    return res


def saldo_cliente(cpf):
    conn = mysql.connector.connect(host="localhost",
                                   database="shopping",
                                   user="root",
                                   password="12345678")
    c = conn.cursor()
    c.execute(f"SELECT nome, saldo FROM clientes WHERE cpf={cpf}")
    res = c.fetchone()
    conn.close()
    return res


def atualizar_saldo(cpf, saldo):
    conn = mysql.connector.connect(host="localhost",
                                   database="shopping",
                                   user="root",
                                   password="12345678")
    c = conn.cursor()
    try:
        c.execute("""UPDATE clientes SET saldo=%s WHERE cpf=%s""" % (saldo, cpf))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        c.close()
        conn.close()


# list_items('bobs')
# list_items('burgerking')
# print(busca_pdv(10, 'bobs'))
# print(saldo_cliente('123456'))
# print(nome)
# print(saldo)
# atualizar_saldo('12345', 2000)
