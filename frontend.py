# frontend.py

import tkinter as tk
from tkinter import messagebox

# Lista de contatos
contatos = []

# Função para adicionar contato
def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if nome == "" or telefone == "" or email == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    contato = f"Nome: {nome} | Telefone: {telefone} | Email: {email}"

    contatos.append(contato)

    lista_contatos.insert(tk.END, contato)

    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Função para remover contato
def remover_contato():
    selecionado = lista_contatos.curselection()

    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um contato!")
        return

    indice = selecionado[0]

    lista_contatos.delete(indice)

    contatos.pop(indice)

# Janela principal
janela = tk.Tk()
janela.title("Agenda de Contatos")
janela.geometry("500x400")

# Título
titulo = tk.Label(
    janela,
    text="Agenda de Contatos",
    font=("Arial", 18)
)

titulo.pack(pady=10)

# Campo Nome
label_nome = tk.Label(janela, text="Nome")
label_nome.pack()

entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

# Campo Telefone
label_telefone = tk.Label(janela, text="Telefone")
label_telefone.pack()

entry_telefone = tk.Entry(janela, width=40)
entry_telefone.pack(pady=5)

# Campo Email
label_email = tk.Label(janela, text="Email")
label_email.pack()

entry_email = tk.Entry(janela, width=40)
entry_email.pack(pady=5)

# Botão adicionar
btn_adicionar = tk.Button(
    janela,
    text="Adicionar Contato",
    command=adicionar_contato,
    bg="green",
    fg="white",
    width=20
)

btn_adicionar.pack(pady=10)

# Lista de contatos
lista_contatos = tk.Listbox(
    janela,
    width=70,
    height=10
)

lista_contatos.pack(pady=10)

# Botão remover
btn_remover = tk.Button(
    janela,
    text="Remover Contato",
    command=remover_contato,
    bg="red",
    fg="white",
    width=20
)

btn_remover.pack(pady=5)

# Executar interface
janela.mainloop()