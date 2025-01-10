###### TO-DO LIST #########
from tkinter import *

window = Tk()
window.geometry("300x500")

#######################################

def mostrarItem():
    limparTela1()
    def limparTelaMostrar():
        voltar.pack_forget()
        itens.pack_forget()
        gerarTela()

    itens.pack()

    voltar = Button(window, text="Voltar", command=limparTelaMostrar)
    voltar.pack()

######################################
def adicionarItem():
    limparTela1()
    def enviarItem():
        item = descricao.get()
        itens.insert(itens.size(), item)
        itens.config(height=itens.size())
        limparTelaAdicionar()

    def limparTelaAdicionar():
        title.pack_forget()
        descricao.pack_forget()
        btnEnviar.pack_forget()
        voltar.pack_forget()
        gerarTela()

    title = Label(window, text="Insira o objetivo (máx 100 caractere)")
    title.pack()
    descricao = Entry(window)
    descricao.pack()
    btnEnviar = Button(window, text="Enviar", command= enviarItem)
    btnEnviar.pack()
    voltar = Button(window, text="Voltar", command=limparTelaAdicionar)
    voltar.pack()

#######################################
def removerItem():
    limparTela1()
    def limparTelaRemover():
        itens.pack_forget()
        deletar.pack_forget()
        voltar.pack_forget()
        gerarTela()
    
    def deletarItem():
        itens.delete(itens.curselection(), itens.curselection())
        itens.config(height=itens.size())
        
    itens.pack()
    deletar = Button(window, text="Deletar", command=deletarItem)
    deletar.pack()
    voltar = Button(window,text="Voltar", command=limparTelaRemover)
    voltar.pack()
#######################################
def limparTela1():
    btnMostrar.pack_forget()
    btnAdicionar.pack_forget()
    btnRemover.pack_forget()

def gerarTela():
    btnMostrar.pack()
    btnAdicionar.pack()
    btnRemover.pack()
#######################################
pendente = 0
itens = Listbox(window)
#######################################

btnMostrar = Button(window, text= "Mostrar itens",width = 15, command=mostrarItem)
btnMostrar.pack()

btnAdicionar = Button(window, text= "Adicionar item",width = 15, command=adicionarItem)
btnAdicionar.pack()

btnRemover = Button(window, text="Remover item",width = 15, command=removerItem)
btnRemover.pack()


window.mainloop()
