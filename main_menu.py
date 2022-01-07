from tkinter import *
from tkinter import messagebox
import time
from PIL import ImageTk,Image

def main_menu(usernumber):
    main_window = Tk()
    main_window.geometry('1024x600')
    main_window.title("Online Courses Manager")
    main_window.resizable(0,0)
    main_window.configure(background='navajo white')
    main_window.iconbitmap("code.ico")

    def addinfo():
        global Dados
        f = open("data/utilizadores.txt", 'r', encoding='UTF-8')
        linha = f.readlines()
        #Variável user number é do tipo string
        info = linha[int(usernumber)]               #   Dados[0] = User Number |  Dados[3] = Password
        f.close()                                   #   Dados[1] = Name        |  Dados[4] = Admin/User
        Dados = info.split(';')                     #   Dados[2] = Email       |  Dados[5] = Register Date
        print(Dados)   
    addinfo()

    painel_preto_cima = PanedWindow(main_window, width = 1024, height= 50, background='black')
    painel_preto_cima.place(x = 0, y = 0)

    time1 = ''
    clock = Label(painel_preto_cima, font=('times', 20, 'bold'), fg='white', bg='black')
    clock.place(x = 910,y = 5)
 
    def tick(time1):
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed (delay 200ms)
        clock.after(200, lambda:tick(time1))
    
    tick(time1)


 

    main_window.mainloop() 