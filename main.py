from tkinter import *
from turtle import back, heading
import sqlite3


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
        self.cpf = self.cpf_entry.get()
        self.nome = self.nome_entry.get()
        self.senha = self.senha_entry.get()
        self.endereco = self.endereco_entry.get()
        self.tel = self.tel_entry.get()

        self.cursor.execute(
            """ INSERT INTO cliente (cpf, nome_cliente, senha, endereco, telefone)
            VALUES (?, ?, ?, ?, ?)""",
            (self.cpf, self.nome, self.senha, self.endereco, self.tel))


class Tela_login(Funcs_bd):
    def __init__(self):
        self.root = Tk()
        self.config_tela()
        self.widgets_login()
        self.cria_bd()
        self.root.mainloop()

    def config_tela(self):
        #configuração e preparo para tela
        self.root.title("Tela de login")
        self.root.configure(background='#1e3743')
        self.root.geometry("450x350")
        self.root.minsize(width=500, height=400)
        #frame que vai os widgets
        self.frame_login = Frame(self.root,
                                 bd=4,
                                 bg='#dfe3ee',
                                 highlightbackground='#759fe6',
                                 highlightthickness=3)
        self.frame_login.place(relx=0.02,
                               rely=0.02,
                               relwidth=0.96,
                               relheight=0.96)

    def widgets_login(self):
        #cpf
        self.cpf_lb = Label(self.frame_login,
                            text="CPF",
                            bg='#dfe3ee',
                            fg='#107db2')
        self.cpf_lb.place(relx=0.26, rely=0.15)

        self.cpf_entry = Entry(self.frame_login)
        self.cpf_entry.place(relx=0.35,
                             rely=0.15,
                             relwidth=0.24,
                             relheight=0.05)

        #usuario
        #senha
        self.senha_lb = Label(self.frame_login,
                              text="SENHA",
                              bg='#dfe3ee',
                              fg='#107db2')
        self.senha_lb.place(relx=0.24, rely=0.25)

        self.senha_entry = Entry(self.frame_login)
        self.senha_entry.place(relx=0.35,
                               rely=0.25,
                               relwidth=0.24,
                               relheight=0.05)

        #entrar
        self.entrar_bt = Button(self.frame_login,
                                text="ENTRAR",
                                bd=2,
                                bg='#107db2',
                                fg='white',
                                font=('verdana', 8, 'bold'))

        self.entrar_bt.place(relx=0.35, rely=0.34)
        #cadastrar novo usuario
        self.cadastro_bt = Button(self.frame_login,
                                  text="NOVO USUARIO",
                                  bd=2,
                                  bg='#107db2',
                                  fg='white',
                                  font=('verdana', 8, 'bold'),
                                  command=self.janela_cadastro)

        self.cadastro_bt.place(relx=0.35, rely=0.44)
        #esqueceu a senha
        self.lembrar_senha_bt = Button(self.frame_login,
                                       text="ESQUECI MINHA SENHA",
                                       bd=2,
                                       bg='#107db2',
                                       fg='white',
                                       font=('verdana', 8, 'bold'))

        self.lembrar_senha_bt.place(relx=0.35, rely=0.54)

    def janela_cadastro(self):
        #janela de cadastro
        self.root_cd = Toplevel()
        self.root_cd.title('cadastro')
        self.root_cd.configure(background='lightblue')
        #self.root_cd.resizable(False, False)
        #afirmando da onde vem
        self.root_cd.transient(self.root)
        #travando na janela de cadastro
        self.root_cd.focus_force()
        self.root_cd.grab_set()
        self.frame_cdd()
        self.widgets_cd()

    def frame_cdd(self):
        #colocando o frame dentro da janelda de cadastro
        self.root_cd.geometry("450x350")
        self.root_cd.minsize(width=500, height=400)
        self.frame_cd = Frame(self.root_cd,
                              bd=4,
                              bg='#dfe3ee',
                              highlightbackground='#759fe6',
                              highlightthickness=3)
        self.frame_cd.place(relx=0.02,
                            rely=0.02,
                            relwidth=0.96,
                            relheight=0.96)

    def widgets_cd(self):
        #widgets dentro do frame do cadastro
        #nome completo
        self.nome_lb = Label(self.frame_cd,
                             text="NOME COMPLETO",
                             bg='#dfe3ee',
                             fg='#107db2')
        self.nome_lb.place(relx=0.05, rely=0.15)

        self.nome_entry = Entry(self.frame_cd)
        self.nome_entry.place(relx=0.32,
                              rely=0.15,
                              relwidth=0.44,
                              relheight=0.05)
        #cpf
        self.cpf_lb = Label(self.frame_cd,
                            text="CPF",
                            bg='#dfe3ee',
                            fg='#107db2')
        self.cpf_lb.place(relx=0.05, rely=0.25)

        self.cpfcd_entry = Entry(self.frame_cd)
        self.cpfcd_entry.place(relx=0.12,
                               rely=0.25,
                               relwidth=0.3,
                               relheight=0.05)

        #telefone
        self.tel_lb = Label(self.frame_cd,
                            text="TELEFONE",
                            bg='#dfe3ee',
                            fg='#107db2')
        self.tel_lb.place(relx=0.43, rely=0.25)

        self.tel_entry = Entry(self.frame_cd)
        self.tel_entry.place(relx=0.6, rely=0.25, relwidth=0.3, relheight=0.05)

        #endereço
        self.endereco_lb = Label(self.frame_cd,
                                 text="ENDEREÇO COMPLETO",
                                 bg='#dfe3ee',
                                 fg='#107db2')
        self.endereco_lb.place(relx=0.05, rely=0.35)

        self.endereco_entry = Entry(self.frame_cd)
        self.endereco_entry.place(relx=0.4,
                                  rely=0.35,
                                  relwidth=0.5,
                                  relheight=0.05)

        #senha
        self.senha_lb = Label(self.frame_cd,
                              text="SENHA",
                              bg='#dfe3ee',
                              fg='#107db2')
        self.senha_lb.place(relx=0.05, rely=0.45)

        self.senha_entry = Entry(self.frame_cd)
        self.senha_entry.place(relx=0.2,
                               rely=0.45,
                               relwidth=0.5,
                               relheight=0.05)

        #botao para cadastrar novo usuario
        self.cadastro_bt = Button(self.frame_cd,
                                  text="CADASTRAR",
                                  bd=2,
                                  bg='#107db2',
                                  fg='white',
                                  font=('verdana', 8, 'bold'),
                                  command=self.add_cliente)

        self.cadastro_bt.place(relx=0.3, rely=0.54)


Tela_login()