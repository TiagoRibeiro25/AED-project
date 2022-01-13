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

    #Imagens
    menu_abrir = PhotoImage(file = 'menu_abrir.png')
    menu_fechar = PhotoImage(file = 'menu_fechar.png')
    user_avatar = PhotoImage(file = 'user.png')

    #Limpa as páginas (para evitar memory leak)
    def fundo():
        global main_painel
        main_painel = PanedWindow(main_window, width = 1024, height= 550, background='#b9b9b9')
        main_painel.place(x = 0, y = 50)

    #chama a página inicial/principal
    def start():
        main_painel.destroy
        fundo()

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

        def admin():
            print('admin')

        def settings():
            fechar_menu()
            main_painel.destroy
            fundo()

            #painel da esquerda
            settings_painel = PanedWindow(main_painel, width = 350, height= 510, background='black')
            settings_painel.place(x = 20, y = 20)
            #user avatar
            ctn_canvas = Canvas(settings_painel, width = 200, height = 200, background='#b9b9b9')
            ctn_canvas.place(x = 70, y = 50)
            ctn_canvas.create_image(100,100, image = user_avatar)
            #Info:
            #UserID
            userID_info = Label(settings_painel, text = 'User ID: {0}'.format(Dados[0]), fg='white', font = ('Arial', 13), background='black')
            userID_info.place(x = 70, y = 260)
            #Name
            name_info = Label(settings_painel, text = 'Name: {0}'.format(Dados[1]), fg='white', font = ('Arial', 13), background='black')
            name_info.place(x = 70, y = 290)
            #Email
            email_info = Label(settings_painel, text = 'Email: {0}'.format(Dados[2]), fg='white', font = ('Arial', 13), background='black')
            email_info.place(x = 70, y = 320)
            #Password
            def show_pw():
                show = val.get()
                if show == 0:
                    pw_info1.configure(text = 'hidden')
                if show == 1:
                    pw_info1.configure(text = Dados[3])
                
            pw_info = Label(settings_painel, text = 'Password:', fg='white', font = ('Arial', 13), background='black')
            pw_info1 = Label(settings_painel, text = 'hidden', fg='white', font = ('Arial', 13), background='black')
            pw_info.place(x = 70, y = 350)
            pw_info1.place(x = 150, y = 350)
            #show password
            val = IntVar(0)    
            btn_pw_visible = Checkbutton(settings_painel, text = "Show Password", font = ('Arial', 7), fg = 'white', background = 'black', variable= val, command=show_pw)
            btn_pw_visible.place (x = 70,y = 370)
            #Type of user
            type_of_user_info = Label(settings_painel, text = 'Type of user: {0}'.format(Dados[4]), fg='white', font = ('Arial', 13), background='black')
            type_of_user_info.place(x = 70, y = 400)
            #Data de registo
            sign_up_date_info = Label(settings_painel, text = 'Sign up date: {0}'.format(Dados[5]), fg='white', font = ('Arial', 13), background='black')
            sign_up_date_info.place(x = 70, y = 440)

            #Painel Direita (credenciais)
            settings_painel1 = PanedWindow(main_painel, width = 600, height= 510, background='black')
            settings_painel1.place(x = 400, y = 20)
            #change name
            change_name = Label(settings_painel1, text = 'Change name:', fg='white', font = ('Arial', 15), background='black')
            change_name.place(x = 20, y = 20)
            change_name_entry = Entry(settings_painel1, width = 40, background = 'white')
            change_name_entry.place(x = 155, y = 26)
            #change password
            change_pw = Label(settings_painel1, text = 'Change password:', fg='white', font = ('Arial', 15), background='black')
            change_pw.place(x = 20, y = 80)
            change_pw_entry = Entry(settings_painel1, width = 34, background = 'white', show='*')
            change_pw_entry.place(x = 191, y = 86)
            #show password
            def show_pw1():
                pw_info1 = val1.get()
                if pw_info1 == 1:
                    change_pw_entry.configure(show='')
                if pw_info1 == 0:
                    change_pw_entry.configure(show='*')

            val1 = IntVar(0)    
            btn_show_pw1 = Checkbutton(settings_painel1, text = "Show Password",fg ='white', font = ('Arial', 7), background = 'black', variable= val1, command=show_pw1)
            btn_show_pw1.place (x = 20,y = 110)
            #change email
            change_email = Label(settings_painel1, text = 'Change email:', fg='white', font = ('Arial', 15), background='black')
            change_email.place(x = 20, y = 170)
            change_email_entry = Entry(settings_painel1, width = 40, background = 'white')
            change_email_entry.place(x = 155, y = 176)

            #Simbolos que seram visiveis após "aplicar"
            lbl_red1 = Label(settings_painel1, text='X', fg='black', font = ('Arial', 10), background='black',height=1)
            lbl_red2 = Label(settings_painel1, text='X', fg='black', font = ('Arial', 10), background='black',height=1)
            lbl_red3 = Label(settings_painel1, text='X', fg='black', font = ('Arial', 10), background='black',height=1)
            lbl_red1.place(x = 400, y = 24)
            lbl_red2.place(x = 400, y = 84)
            lbl_red3.place(x = 400, y = 174)

            def verify_name():
                name_correct = 0
                new_name = change_name_entry.get()                          #nome
                new_name_letters = len(new_name)                            #Numero de caracteres do nome

                if new_name_letters > 20 or new_name_letters == 0:          #Máximo 29 caracteres para evitar nomes muito grandes
                    lbl_red1.configure(text='X', fg='red')
                    name_correct = 0
                elif new_name.count(' ') == new_name_letters:               #Verificar se o nome tem alguma letra/número (não seja so espaços)
                    lbl_red1.configure(text='X', fg='red')
                    name_correct = 0
                else:
                    lbl_red1.configure(text='✔', fg='green')
                    name_correct = 1

                if name_correct == 1:
                    f = open("data/utilizadores.txt", 'r+', encoding='UTF-8')
                    linhas = f.readlines()
                    


            def verify_pw():
                pw_correct = 0
                new_pw = change_pw_entry.get()                                  #Password

                #password
                if new_pw.count(' ') == len(new_pw) or new_pw == '':            #Verificar se existe uma senha e se a senha tem alguma letra ou número (nao seja so espaços)
                    lbl_red2.configure(text='X', fg='red')
                    pw_correct = 0
                else:
                    lbl_red2.configure(text='✔', fg='green')
                    pw_correct = 1

            def verify_email():
                email_correct = 0
                new_email = change_email_entry.get()                        #Email
                    
                #email
                if new_email.find('@') == -1 or new_email.find('.') == -1:  #verifica se o email tem um '@' e um '.'
                    lbl_red3.configure(text='X', fg='red')
                    email_correct = 0
                elif new_email.rfind('.') < new_email.find('@'):            #Verifica se o '.' está depois do '@'  (xxxx@xxx.xx)
                    lbl_red3.configure(text='X', fg='red')                  #                                           ^   ^
                    email_correct = 0
                else:
                    lbl_red3.configure(text='✔', fg='green')
                    email_correct = 1



            #Aplicar
            btn_apply_name = Button(settings_painel1,text = 'Apply', font = ('Arial', 7), fg = 'black', relief='flat', background = 'white', width=10, command=verify_name)
            btn_apply_name.place (x = 25,y = 50)
            btn_apply_pw = Button(settings_painel1,text = 'Apply', font = ('Arial', 7), fg = 'black', relief='flat', background = 'white', width=10, command=verify_pw)
            btn_apply_pw.place (x = 25,y = 130)
            btn_apply_email = Button(settings_painel1,text = 'Apply', font = ('Arial', 7), fg = 'black', relief='flat', background = 'white', width=10, command=verify_email)
            btn_apply_email.place (x = 25,y = 200)







        #Painel-botoes do sub-menu
        sub_menu = PanedWindow(main_window, width = 300, height= 600, background='black')
        sub_menu.place(x = 0, y = 0)
        btn_menu_fechar = Button(sub_menu, image = menu_fechar, font = ('Arial', 11), fg = 'black', relief='flat', background = '#b9b9b9', width=39, height=28, command=fechar_menu)
        btn_menu_fechar.place (x = 5,y = 7)

        #Imagem do utilizador
        ctn_canvas = Canvas(sub_menu, width = 200, height = 200, background='#b9b9b9')
        ctn_canvas.place(x = 45, y = 80)
        ctn_canvas.create_image(100,100, image = user_avatar)

        #Nome do user abaixo do avatar
        lbl_name = Label(sub_menu, text = Dados[1], fg='white', font = ('Arial', 13), background='black')
        lbl_name.place(x = 45, y = 290)

        #Start-Page
        btn_admin_page = Button(sub_menu, text = 'Admin Tools', font = ('Arial', 18), fg = 'black', relief='groove', background = 'white', width=15, command=admin)
        btn_admin_page.place (x = 35,y = 390)
        if Dados[4] == 'user':
            btn_admin_page.configure(state=DISABLED)

        #Settings
        btn_settings = Button(sub_menu, text = 'Settings', font = ('Arial', 18), fg = 'black', relief='groove', background = 'white', width=15, command=settings)
        btn_settings.place (x = 35,y = 460)

        #Log out
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
    fundo()
    start()

    main_window.mainloop() 