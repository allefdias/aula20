import pymysql.cursors
from tkinter import *

def criarConexao():
    try:
        conexao = pymysql.connect(user='root',
                                  password= '',
                                  host='localhost',
                                  database='escola')
        return conexao
    except Exception as error:
        print(f'ERRO AO CONECTAR!{error}')


def cadastrarAluno():
    try:
        nome = txtNome.get()
        nota = float (txtNota.get())
        turma_id= int(txtTurma.get())
        sql = "INSERT INTO aluno (nome, nota, turma_id) values (%s,%s,%s)"
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(sql, (nome, nota, turma_id))
        conexao.commit()
        print('Dados cadastros com sucesso!')

        txtNota.delete(0,END)
        txtTurma.delete(0,END)
        txtNome.delete(0,END)

    except Exception as error:
        print(f'erro ao cadastrar! Erro: {error}')




























janela =  Tk()

janela.title('Cadastro de alunos')
label_matricula = Label(janela, text = 'Matricula:', font = 'Tahoma 16')
label_matricula.grid(row = 0, column =0)

txtMatricula = Entry(janela, font= 'Tahoma 16')
txtMatricula.grid(row = 0, column =1)

label_nome = Label(janela, text = ' Nome:', font = 'Tahoma 16')
label_nome.grid(row =1, column=0)

txtNome = Entry(janela, font='Tahoma 16')
txtNome.grid(row =1, column=1)

label_turma = Label(janela, text = ' Turma:', font = 'Tahoma 16')
label_turma.grid(row =2, column=0)
txtTurma = Entry(janela, font='Tahoma 16')
txtTurma.grid(row =2, column=1)


label_nota = Label(janela, text = 'nota:', font = 'Tahoma 16')
label_nota.grid(row =3, column=0)

txtNota = Entry(janela, font='Tahoma 16')
txtNota.grid(row =3, column=1)

btn_cadastrar = Button(janela, text = 'Cadastrar', font= 'Tahoma 16',fg = 'blue', bg = '#14964c',
                       command = cadastrarAluno)
btn_cadastrar.grid(row = 4, column=0)













janela.mainloop()