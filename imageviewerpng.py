import tkinter as tki
from tkinter import *
from tkinter import filedialog
import os

nome = "" 

def abrir():
    global nome
    nome=tki.filedialog.askopenfilename()
    photo["file"]=nome
    print(nome)

def sair():
    win.destroy()

win= tki.Tk()
win.geometry("500x500+150+150")
win["bg"]="white"

win.title("Visualizador de imagem")

menu_bar = tki.Menu(win)
menu_arquivo = tki.Menu(win)

menu_arquivo.add_command(label="Novo")
menu_arquivo.add_command(label="Abrir...",command=abrir)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair",command=sair)

menu_bar.add_cascade(label="Arquivo",menu=menu_arquivo)

win.config(menu=menu_bar)

photo=tki.PhotoImage(file=nome)

label=tki.Label(win,image=photo)
label.pack()


win.mainloop()
