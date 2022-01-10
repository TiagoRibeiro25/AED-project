from tkinter import *
from tkinter import messagebox
import time
from PIL import ImageTk,Image
import start_menu

def main_menu(usernumber):
    main_window = Tk()
    main_window.geometry('1024x600')
    main_window.title("Online Courses Manager")
    main_window.resizable(0,0)
    main_window.configure(background='#b9b9b9')
    main_window.iconbitmap("hat.ico")

    def addinfo():
        global Dados
        f = open("data/utilizadores.txt", 'r', encoding='UTF-8')
        linha = f.readlines()
        #Variável user number é do tipo string
        info = linha[int(usernumber)]               #   Dados[0] = User Number |  Dados[3] = Password
        f.close()                                   #   Dados[1] = Name        |  Dados[4] = Admin/User
        Dados = info.split(';')                     #   Dados[2] = Email       |  Dados[5] = Register Date
    addinfo()

    painel_preto_cima = PanedWindow(main_window, width = 1024, height= 50, background='black')
    painel_preto_cima.place(x = 0, y = 0)

    #Relógio
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

    menu_abrir = PhotoImage(file = 'menu_abrir.png')
    menu_fechar = PhotoImage(file = 'menu_fechar.png')

    def sub_menu():
        #fechar sub-menu
        def fechar_menu():
            sub_menu.destroy()
            btn_menu()

        def log_out():
            global Dados
            Dados = []
            main_window.destroy()
            start_menu.start_window()

        #Painel-botoes do sub-menu
        sub_menu = PanedWindow(main_window, width = 300, height= 600, background='black')
        sub_menu.place(x = 0, y = 0)
        btn_menu_fechar = Button(sub_menu, image = menu_fechar, font = ('Arial', 10), fg = 'black', relief='flat', background = '#b9b9b9', width=39, height=28, command=fechar_menu)
        btn_menu_fechar.place (x = 5,y = 7)

        btn_log_out = Button(sub_menu, text = 'Log out', font = ('Arial', 18), fg = 'black', relief='groove', background = 'white', width=15, command=log_out)
        btn_log_out.place (x = 35,y = 530)


    def btn_menu():
        #Botão hamburguer (sub-menu)
        def abrir_menu():
            btn_menu_abrir.destroy()
            sub_menu()

        btn_menu_abrir = Button(painel_preto_cima, image = menu_abrir, font = ('Arial', 10), fg = 'black', relief='flat', background = '#b9b9b9', width=39, height=28, command=abrir_menu)
        btn_menu_abrir.place (x = 5,y = 7)

    btn_menu()


    main_window.mainloop() 