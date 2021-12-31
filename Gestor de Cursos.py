from tkinter import *
from PIL import ImageTk,Image

def start_window():

    #Criar janela principal
    start_window = Tk()  
    start_window.geometry('850x400+500+300')
    start_window.resizable(0,0)
    start_window.configure(background='black')
        
    def start():
        start_window.title('Online Courses Manager')

        def Log_In():
            start_window.title('Online Courses Manager - Log In')
            painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='navajo white')
            painel_inicial.place(x = 40, y = 33)

            #container Canvas
            ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='navajo white')
            ctn_canvas.place(x = 0, y = 0)
            ctn_canvas.create_image(240,170, image = img1)

            #Botao voltar
            btn_voltar = Button(painel_inicial, text = 'back', font = ('Helvetica', 10), fg = 'black', relief='raised', background = 'navajo white', width=8, height=1, command=start)
            btn_voltar.place (x = 0,y = 0)

            #Painel da direita (log-In)
            painel_log_in = PanedWindow(painel_inicial, width = 260, height= 310, background='white')
            painel_log_in.place(x = 500, y = 10)

            lbl_Log_In = Label(painel_log_in, text = 'Log In', fg='black', font = ('Helvetica', 20), background='white')
            lbl_Log_In.place(x = 90, y = 0)

            lbl_name = Label(painel_log_in, text = 'Name:', fg='black', font = ('Helvetica', 15), background='white')
            lbl_name.place(x = 10, y = 60)
            Entry_name = Entry(painel_log_in, width = 27, background = 'white')
            Entry_name.place(x = 75, y = 66)

            lbl_pw = Label(painel_log_in, text = 'Password:', fg='black', font = ('Helvetica', 14), background='white')
            lbl_pw.place(x = 10, y = 95)
            Entry_pw = Entry(painel_log_in, width = 22, background = 'white', show='*')
            Entry_pw.place(x = 105, y = 101)

            #botao next
            btn_next = Button(painel_log_in, text = 'Next', font = ('Helvetica', 15), fg = 'white', relief='groove', background = 'green', width=15)
            btn_next.place (x = 44,y = 160)

            #botao caso não tenha conta
            btn_no_account = Button(painel_log_in, text = "Don't have an account? Click here", font = ('Helvetica', 10), fg = 'blue', relief='flat', background = 'white', command=Sign_In)
            btn_no_account.place (x = 25,y = 270)


        def Sign_In():
            start_window.title('Online Courses Manager - Sign In')
            painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='navajo white')
            painel_inicial.place(x = 40, y = 33)

            #container Canvas
            ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='navajo white')
            ctn_canvas.place(x = 0, y = 0)
            ctn_canvas.create_image(240,170, image = img1)

            #Botao voltar
            btn_voltar = Button(painel_inicial, text = 'back', font = ('Helvetica', 10), fg = 'black', relief='raised', background = 'navajo white', width=8, height=1, command=start)
            btn_voltar.place (x = 0,y = 0)

            #Painel da direita (log-In)
            painel_log_in = PanedWindow(painel_inicial, width = 260, height= 310, background='white')
            painel_log_in.place(x = 500, y = 10)

            lbl_Log_In = Label(painel_log_in, text = 'Sign In', fg='black', font = ('Helvetica', 20), background='white')
            lbl_Log_In.place(x = 85, y = 0)

            #botao caso não tenha conta
            btn_no_account = Button(painel_log_in, text = "Already have an account? Click here", font = ('Helvetica', 10), fg = 'blue', relief='flat', background = 'white', command=Log_In)
            btn_no_account.place (x = 20,y = 270)


        def info():
            start_window.title('Online Courses Manager - Extra Info')
            painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='navajo white')
            painel_inicial.place(x = 40, y = 33)

            #container Canvas
            ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='navajo white')
            ctn_canvas.place(x = 0, y = 0)
            ctn_canvas.create_image(240,170, image = img1)

            #Botao voltar
            btn_voltar = Button(painel_inicial, text = 'back', font = ('Helvetica', 10), fg = 'black', relief='raised', background = 'navajo white', width=8, height=1, command=start)
            btn_voltar.place (x = 0,y = 0)

            #Painel da direita (Ficha-Técnica)
            painel_log_in = PanedWindow(painel_inicial, width = 260, height= 310, background='white')
            painel_log_in.place(x = 500, y = 10)

            lbl_Log_In = Label(painel_log_in, text = 'Made by', fg='black', font = ('Helvetica', 20), background='white')
            lbl_Log_In.place(x = 80, y = 0)

            lbl_info1 = Label(painel_log_in, text = 'Tiago Ribeiro\nnº 40210462\n\nNuno Mendonça\nnº 40210260\n\nJosé Pedro\nnº 40210276', fg='black', font = ('Helvetica', 18), background='white')
            lbl_info1.place(x = 40, y = 50)



        painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='navajo white')
        painel_inicial.place(x = 40, y = 33)

        #Imagens
        img = PhotoImage(file = 'Bem-vindo.png')
        img1 = PhotoImage(file = 'Cursos-Online.png')

        #Canvas
        ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='navajo white')
        ctn_canvas.place(x = 0, y = 0)
        ctn_canvas.create_image(380,170, image = img)

        #Texto Welcome
        lbl_welcome = Label(painel_inicial, text = 'Welcome', fg='goldenrod', font = ('Helvetica', 23), background = 'white')
        lbl_welcome.place(x = 315, y = 97)

        #Botões
        btn_Log_In = Button(painel_inicial, text = 'Log In', font = ('Helvetica', 15), fg = 'black', relief='groove', background = 'SkyBlue2', width=10, height=1, command=Log_In)
        btn_Log_In.place (x = 260,y = 157)

        btn_Sign_In = Button(painel_inicial, text = 'Sign In', font = ('Helvetica', 15), fg = 'black', relief='groove', background = 'SkyBlue2', width=10, height=1, command=Sign_In)
        btn_Sign_In.place (x = 390,y = 157)

        btn_Exit = Button(painel_inicial, text = 'Exit', font = ('Helvetica', 15), fg = 'black', relief='groove', background = 'red', width=10, height=1, command = start_window.destroy)
        btn_Exit.place (x = 320,y = 207)

        #Botão de informação adicional (escondido)
        btn_info = Button(painel_inicial, fg = 'black', background = 'white', relief = 'flat', bitmap = 'info', width=40, height=40, command = info)
        btn_info.place (x = 170,y = 230)

        start_window.mainloop()  #event listening loop by calling the mainloop()


    start()

start_window()