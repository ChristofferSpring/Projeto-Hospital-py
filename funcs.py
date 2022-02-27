from modulos import *


class Funcs_bd():
    def conecta_bd(self):
        self.conn = sqlite3.connect("cliente.bd")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def cria_bd(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                cpf INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                senha CHAR(20) NOT NULL,
                endereco CHAR(40),
                telefone INTEGER(20)
            );""")
        self.conn.commit()
        self.desconecta_bd()

    def add_cliente(self):
        self.cpf = self.cpfcd_entry.get()
        self.nome = self.nome_entry.get()
        self.senha = self.senha_entry.get()
        self.endereco = self.endereco_entry.get()
        self.tel = self.tel_entry.get()
        self.conecta_bd()
        self.cursor.execute(
            """ INSERT OR REPLACE INTO cliente (cpf, nome_cliente, senha, endereco, telefone)
            VALUES (?, ?, ?, ?, ?)""",
            (self.cpf, self.nome, self.senha, self.endereco, self.tel))

        self.conn.commit()
        self.desconecta_bd()
