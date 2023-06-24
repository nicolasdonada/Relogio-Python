from tkinter import *
from time import strftime
import os

janela = Tk()
janela.title("Relógio")
janela.geometry("600x400")
janela.config(bg="black")
janela.resizable(width=False, height=False)

dark = PhotoImage(file="images/dark.png")
brightness = PhotoImage(file="images/brightness.png")

def bg_mode():
    user = os.getlogin()

    def dark_mode():
        janela["bg"] = "black"
        label_horas["bg"] = "black"
        botao_mode["bg"] = "black"
        botao_mode["image"] = dark

        label_user["bg"] = "black"
        label_user["fg"] = "black"

        bg_mode()
      
    
    def brightness_mode():
        janela["bg"] = "white"
        label_horas["bg"] = "white"
        botao_mode["bg"] = "white"
        botao_mode["image"] = brightness

        label_user["bg"] = "white"
        label_user["fg"] = "white"

        bg_mode()

    if label_horas["bg"] == "black":
        botao_mode = Button(janela, image=dark, bg="black", relief="flat", command=brightness_mode)
        botao_mode.place(x=280, y=50)

        label_user = Label(janela, text=f"Olá, {user}", bg="black", fg="white", font="Arial 20")
        label_user.place(x=180, y=120)

    if label_horas["bg"] == "white":
        botao_mode = Button(janela, image=brightness, bg="white", relief="flat", command=dark_mode)
        botao_mode.place(x=280, y=50)

        label_user = Label(janela, text=f"Olá, {user}", bg="white", fg="black", font="Arial 20")
        label_user.place(x=180, y=120)
        
def iniciar():
    label_horas["text"] = strftime("%H:%M:%S")
    label_horas.after(1000, iniciar)


botao_mode = Button(janela, image=dark, bg="black", relief="flat")
botao_mode.place(x=280, y=50)

label_horas = Label(janela, fg="#5E04B5", bg="black", text="", font="Numerial 60 bold")
label_horas.pack(pady=150, anchor="center") 

bg_mode()
iniciar()

janela.mainloop()