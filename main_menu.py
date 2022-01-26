from distutils import command
from hashlib import new
from inspect import CORO_SUSPENDED
from tkinter import *
from tkinter.tix import Tree
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
from time import strftime
from tkinter import messagebox
import webbrowser

from pip import main
import start_menu

# Estrutura
def main_menu(usernumber):
    window = Tk()
    window.geometry('1250x800+300+100')
    window.title("Online Courses Manager")
    window.resizable(0,0)
    window.configure(background='#b9b9b9')
    #window.iconbitmap("/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/hat.ico")
    window.iconbitmap("png/hat.ico")


# Retrieve de dados do User
    def addinfo():
        global Dados
        #f = open("/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/data/utilizadores.txt", 'r', encoding='UTF-8')
        f = open("data/utilizadores.txt", 'r', encoding='UTF-8')
        linha = f.readlines()
        #Variável user number é do tipo string
        info = linha[int(usernumber)]               #   Dados[0] = User Number |  Dados[3] = Password
        f.close()                                   #   Dados[1] = Name        |  Dados[4] = Admin/User
        Dados = info.split(';')                     #   Dados[2] = Email       |  Dados[5] = Register Date
    addinfo()
    
    painel_preto_cima = PanedWindow(window, width = 1250, height= 50, background='black')
    painel_preto_cima.place(x = 0, y = 0)


    # Relógio
    def clock():
        tack = strftime("%H:%M:%S")
        relogio_label.config(text= tack)
        relogio_label.after(500, clock)
    
    relogio_label = Label(painel_preto_cima,font=("calibri", 17), fg = 'white',background = "black")
    relogio_label.place(x=1050, y=8)

    #Imagens
    #menu_abrir = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/button.png')
    #menu_fechar = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/menu_fechar.png')
    #user_avatar = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/user.png')
    #js_img = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/js.png')
    #c_img = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/c.png')
    #html_img = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/html.png')
    #py_img = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/py.png')
    #css_img = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/css.png')
    #go_img = PhotoImage(file = '/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/png/go.png')

    menu_abrir = PhotoImage(file = 'png/button.png')
    menu_fechar = PhotoImage(file = 'png/menu_fechar.png')
    user_avatar = PhotoImage(file = 'png/user.png')
    js_img = PhotoImage(file = 'png/js.png')
    c_img = PhotoImage(file = 'png/c.png')
    html_img = PhotoImage(file = 'png/html.png')
    py_img = PhotoImage(file = 'png/py.png')
    css_img = PhotoImage(file = 'png/css.png')
    go_img = PhotoImage(file = 'png/go.png')
    main_img = PhotoImage(file = 'png/main_img.png')



    #Limpa as páginas (para evitar memory leak)
    def fundo():
        global main_painel
        main_painel = PanedWindow(window, width = 1250, height= 750, background='#b9b9b9')
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
            window.destroy()
            start_menu.start_window()

        def admin():
            fechar_menu()
            main_painel.destroy
            fundo()
            
            #Botão voltar
            back_btn = Button(main_painel, text = 'Main Page', font = ('Arial', 10), fg = 'black', relief='raised', background = '#b9b9b9', width=8, height=1, command=start)
            back_btn.place (x = 20,y = 20)

            painel = PanedWindow(main_painel, width = 1000, height= 510, background='black')
            painel.place(x = 120, y = 110)

            change_info_lbl = Label(painel, text = 'Change Course Description', fg='white', font = ('Arial', 13), background='black')
            change_info_lbl.place(x = 20, y = 8)

            def view_desc():
                course_desc.delete("1.0", "end")
                with open('data/categorias.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if param[0] == course_selected:
                            course_desc.insert("1.0", param[1])
            
            def reset_btns():
                Python_btn.configure(state=NORMAL)
                CSS_btn.configure(state=NORMAL)
                HTML_btn.configure(state=NORMAL)
                C_btn.configure(state=NORMAL)
                Go_btn.configure(state=NORMAL)
                JavaScript_btn.configure(state=NORMAL)

            def Py():
                global course_selected
                course_selected = "Python"
                reset_btns()
                Python_btn.configure(state= DISABLED)
                view_desc()
            def CSS():
                global course_selected
                course_selected = "CSS"
                reset_btns()
                CSS_btn.configure(state= DISABLED)
                view_desc()
            def HTML():
                global course_selected
                course_selected = "HTML"
                reset_btns()
                HTML_btn.configure(state= DISABLED)
                view_desc()
            def C():
                global course_selected
                course_selected = "C++"
                reset_btns()
                C_btn.configure(state= DISABLED)
                view_desc()
            def Go():
                global course_selected
                course_selected = "Go"
                reset_btns()
                Go_btn.configure(state= DISABLED)
                view_desc()
            def JS():
                global course_selected
                course_selected = "JavaScript"
                reset_btns()
                JavaScript_btn.configure(state= DISABLED)
                view_desc()
            
            #Box text 1
            course_desc = Text(painel,width=65, height=8, wrap='word')
            course_desc.place(x=25,y=130)

            global course_selected
            course_selected = ""

            Python_btn = Button(painel, text = 'Python', font = ('Arial', 10), fg = 'black', relief='flat', background = 'white', command=Py)
            CSS_btn = Button(painel, text = 'CSS', font = ('Arial', 10), fg = 'black', relief='flat', background = 'white', command=CSS)
            HTML_btn = Button(painel, text = 'HTML', font = ('Arial', 10), fg = 'black', relief='flat', background = 'white', command=HTML)
            C_btn = Button(painel, text = 'C++', font = ('Arial', 10), fg = 'black', relief='flat', background = 'white', command=C)
            Go_btn = Button(painel, text = 'Go', font = ('Arial', 10), fg = 'black', relief='flat', background = 'white', command=Go)
            JavaScript_btn = Button(painel, text = 'JavaScript', font = ('Arial', 10), fg = 'black', relief='flat', background = 'white', command=JS)

            Py() #selected by default

            Python_btn.place(x=85, y = 30)
            CSS_btn.place(x=25, y = 30)
            HTML_btn.place(x=25, y = 90)
            C_btn.place(x=25, y = 60)
            Go_btn.place(x=85, y = 60)
            JavaScript_btn.place(x=85, y = 90)

            def change_desc():
                new_desc = course_selected + ";" + course_desc_new.get("1.0", "end-1c")
                current_desc = course_selected + ";" + course_desc.get("1.0", "end-2c")
                
                with open("data/categorias.txt", "r", encoding="UTF-8") as f:
                    newText=f.read().replace(current_desc, new_desc)
                with open("data/categorias.txt", "w", encoding="UTF-8") as f:
                    f.write(newText)
                view_desc()


            #Box text 2
            course_desc_new = Text(painel,width=65, height=8, wrap='word')
            course_desc_new.place(x=25,y=350)
            course_desc_new_btn = Button(painel, text = 'Change\nDescription', font = ('Arial', 13), fg = 'black', relief='flat', background = 'white', command=change_desc)
            course_desc_new_btn.place (x = 560, y = 390)



        def settings():
            fechar_menu()
            main_painel.destroy
            fundo()
            
            #Botão voltar
            back_btn = Button(main_painel, text = 'Main Page', font = ('Arial', 10), fg = 'black', relief='raised', background = '#b9b9b9', width=8, height=1, command=start)
            back_btn.place (x = 20,y = 20)

            #painel da esquerda
            settings_painel = PanedWindow(main_painel, width = 350, height= 510, background='black')
            settings_painel.place(x = 100, y = 110)
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
            settings_painel1.place(x = 550, y = 110)
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
                    with open("data/utilizadores.txt", "r", encoding="UTF-8") as f:
                        new_text = ""
                        var_user = ""
                        for line in f:
                            user = line.split(";")
                            if Dados[0] == user[0]:
                                if new_name == user[1]:
                                    messagebox.showerror(title="Warning!",message="Your new name is the same as the old name, try again!") 
                                    var_user = user[1]      
                                    break
                                messagebox.showinfo(title="Sucess", message="Your name has been changed!")  
                                var_user = user[1]
                                user[1] = new_name
                                new_text = new_text + ";".join(user)
                            else:
                                new_text = new_text + line
                    if new_name != var_user:
                        with open("data/utilizadores.txt", "w", encoding="UTF-8") as f: 
                            f.write(new_text)
                            old_name =Dados[1] 
                            Dados[1] = new_name

                        #Change name in rates.txt
                        with open("data/rates.txt", "r") as f:
                            newText=f.read().replace(old_name, new_name)
                        with open("data/rates.txt", "w") as f:
                            f.write(newText)

                        #Change name in comments.txt
                        with open("data/comments.txt", "r") as f:
                            newText=f.read().replace(old_name, new_name)
                        with open("data/comments.txt", "w") as f:
                            f.write(newText)



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

                if pw_correct == 1:
                    with open("data/utilizadores.txt", "r", encoding="UTF-8") as f:
                        new_text = ""
                        var_pw = ""
                        for line in f:
                            user = line.split(";")
                            if Dados[0] == user[0]:
                                if new_pw == user[3]:
                                    messagebox.showerror(title="Warning!",message="Your new password is the same as the old  password, try again!")
                                    var_pw = user[3]      
                                    break
                                messagebox.showinfo(title="Sucess", message="Your password has been changed!")
                                var_pw = user[3]
                                user[3] = new_pw
                                new_text = new_text + ";".join(user)
                            else:
                                new_text = new_text + line
                    if new_pw != var_pw:
                        with open("data/utilizadores.txt", "w", encoding="UTF-8") as f:
                            f.write(new_text)
                            Dados[3] = new_pw


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

                if email_correct == 1:
                    with open("data/utilizadores.txt", "r", encoding="UTF-8") as f:
                        new_text = ""
                        var_email = ""
                        for line in f:
                            user = line.split(";")
                            if Dados[0] == user[0]:
                                if new_email == user[2]:
                                    messagebox.showerror(title="Warning!",message="Your new email is the same as the old email, try again!")
                                    var_email = user[2]      
                                    break
                                messagebox.showinfo(title="Sucess", message="Your email has been changed!")
                                var_email = user[2]
                                user[2] = new_email
                                new_text = new_text + ";".join(user)
                            else:
                                new_text = new_text + line
                    if new_email != var_email:
                        with open("data/utilizadores.txt", "w", encoding="UTF-8") as f:
                            f.write(new_text)
                            Dados[2] = new_email



            #Aplicar
            btn_apply_name = Button(settings_painel1,text = 'Apply', font = ('Arial', 7), fg = 'black', relief='flat', background = 'white', width=10, command=verify_name)
            btn_apply_name.place (x = 25,y = 50)
            btn_apply_pw = Button(settings_painel1,text = 'Apply', font = ('Arial', 7), fg = 'black', relief='flat', background = 'white', width=10, command=verify_pw)
            btn_apply_pw.place (x = 25,y = 130)
            btn_apply_email = Button(settings_painel1,text = 'Apply', font = ('Arial', 7), fg = 'black', relief='flat', background = 'white', width=10, command=verify_email)
            btn_apply_email.place (x = 25,y = 200)

            lbl_info = Label(settings_painel1, text = "AED - Project\nTSIW 2021-2022\n\nTiago Ribeiro\nNuno Mendonça\nJosé Pedro", fg='white', font = ('Arial', 13), background='black')
            lbl_info.place(x = 460, y = 380)





        #Painel-botoes do sub-menu
        sub_menu = PanedWindow(window, width = 300, height= 800, background='black')
        sub_menu.place(x = 0, y = 0)
        btn_menu_fechar = Button(sub_menu, image = menu_fechar, font = ('Arial', 11), fg = 'black', relief='flat', background = '#b9b9b9', width=39, height=28, command=fechar_menu)
        btn_menu_fechar.place (x = 5,y = 7)

        #Imagem do utilizador
        ctn_canvas = Canvas(sub_menu, width = 220, height = 220, background='#b9b9b9')
        ctn_canvas.place(x = 40, y = 240)
        ctn_canvas.create_image(110,110, image = user_avatar)

        #Nome do user abaixo do avatar
        lbl_name = Label(sub_menu, text = Dados[1], fg='white', font = ('Arial', 13), background='black')
        lbl_name.place(x = 45, y = 470)

        #Admin Tools
        btn_admin_page = Button(sub_menu, text = 'Admin Tools', font = ('Arial', 18), fg = 'black', relief='groove', background = 'white', width=15, command=admin)
        btn_admin_page.place (x = 35,y = 540)
        if Dados[4] == 'user':
            btn_admin_page.configure(state=DISABLED)

        #Settings
        btn_settings = Button(sub_menu, text = 'Settings', font = ('Arial', 18), fg = 'black', relief='groove', background = 'white', width=15, command=settings)
        btn_settings.place (x = 35,y = 610)

        #Log out
        btn_log_out = Button(sub_menu, text = 'Log out', font = ('Arial', 18), fg = 'black', relief='groove', background = 'white', width=15, command=log_out)
        btn_log_out.place (x = 35,y = 680)

    def btn_menu():
        #Botão abrir menu (sub-menu)
        def abrir_menu():
            btn_menu_abrir.destroy()
            sub_menu()

        btn_menu_abrir = Button(painel_preto_cima, image = menu_abrir, font = ('Arial', 20), relief='flat', width=39, height=28, command=abrir_menu)
        btn_menu_abrir.place (x = 15,y = 7)
  

    def start():
        main_painel.destroy
        fundo()

        # Box para os cursos
        def painel():
            global panel1
            panel1 = PanedWindow(main_painel, width=570, height=470, bd="6", relief="sunken")
            panel1.place(x=320,y=250)    

        painel()
        

        # Botões box central
        def windowScript():
            windowjs = Toplevel()
            windowjs.geometry("900x700+500+100")
            windowjs.title("JavaScript")
            windowjs.resizable()
            panedjs = PanedWindow(windowjs, width=898, height=698, bd="8", relief="sunken")
            panedjs.place(x=0,y=0)
            titlejs = Label(panedjs, text="JavaScript", fg="blue",bd= "8" ,relief="raised", font=("Arial", 34))
            titlejs.place(x=320,y=20)
            lbl_js = Label(panedjs, text="Description:", fg="blue", font=("Arial, 14"))
            lbl_js.place(x=90,y=110)

            txt_texto = Text(panedjs, width=90, height=15, wrap="word")
            txt_texto.place(x=80,y=150)

            with open("data/categorias.txt", "r", encoding="UTF-8") as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "JavaScript":
                        txt_texto.insert("1.0", param[1])

            #Button open
            def link():
                webbrowser.open_new_tab("https://javascript.info/")

            open_btn = Button(panedjs, text="OPEN COURSE", fg="blue", font=("Arial, 16"), command= link)
            open_btn.place (x = 650,y = 450)

            lbl_js2 = Label(panedjs, text="Comments: ", fg="black", font=("Arial, 12"))
            lbl_js2.place(x=90,y=420)

            def add_fav():
                with open("data/fav.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    for line in f:
                        user = line.split(";")
                        if Dados[0] == user[0]:
                            course_name = "JavaScript"
                            user[len(user)-1] = course_name + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/fav.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    fav_js.configure(text="Remove from Favorites", command= remove_fav)

            def remove_fav():
                fav_js.configure(text="Add to Favorites", command= add_fav)
        
            with open('data/fav.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if Dados[0] == param[0]:
                            i = 1
                            while i < len(param)-1:
                                if param[i] == "JavaScript":
                                    fav_js = Button(panedjs,text="Remove from Favorites", fg="blue", font=("Arial, 16"), command= remove_fav)
                                    fav_js.place(x=650,y=550)
                                    i = 99
                                else:
                                    i = i + 1

                            if i != 99:        
                                fav_js = Button(panedjs,text="Add to Favorites", fg="blue", font=("Arial, 16"), command= add_fav)
                            
                            fav_js.place(x=650,y=550)

            txt_cmt = Text(panedjs,width=65, height=8, wrap='word')
            txt_cmt.place(x=80,y=450)

            #Ler os comentarios do ficheiro
            def ler():
                with open('data/comments.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")       
                        if param[0] == "JavaScript":
                            i = 1
                            while i < len(param):
                                txt_cmt.insert("1.0", param[i] + "\n")
                                i = i + 1
            ler()

            #Add comment
            txt_add_cmt = Entry(panedjs, width = 87, background = 'white')
            txt_add_cmt.place(x = 80, y = 605)


            def post_cmt():
                comment_txt = txt_add_cmt.get()
                comment = Dados[1] + ": " + comment_txt   #Name: "comment";

                with open("data/comments.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "JavaScript"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = comment + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/comments.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)

                txt_cmt.delete("1.0", "end")
                ler()   #Update comment box

                

            btn_post = Button(panedjs,text="Post", fg="blue", font=("Arial, 16"), command=post_cmt)
            btn_post.place(x=650,y=600)

            def rate():
                info = Dados[1] + ";" + str(scale1.get())
                with open("data/rates.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "JavaScript"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = info + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/rates.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    rate_btn.configure(state=DISABLED)


            #Rate
            rate_btn = Button(panedjs, text="Rate", fg="blue", font=("Arial, 10"), command=rate)
            rate_btn.place(x=825,y=37)

            #In case the user did already vote in the past (can't vote again)
            with open('data/rates.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "JavaScript":
                        i = 1
                        while i < len(param):
                            if param[i] == Dados[1]:
                                rate_btn.configure(state=DISABLED)
                            i = i + 2

            scale1 = Scale(panedjs, width=20, from_= 0, to= 10, orient="horizontal")
            scale1.place(x=720,y=20)

        
        def windowC():
            window_cpro = Toplevel()
            window_cpro.geometry("900x700+500+100")
            window_cpro.title("C++")
            window_cpro.resizable(0,0)
            panedc = PanedWindow(window_cpro, width=898, height=698, bd="8", relief="sunken")
            panedc.place(x=0,y=0)
            titlec = Label(panedc, text="C++", fg="blue",bd= "8" ,relief="raised", font=("Arial", 34))
            titlec.place(x=390,y=20)
            lbl_c = Label(panedc, text="Description:", fg="blue", font=("Arial, 14"))
            lbl_c.place(x=90,y=110)

            txt_texto = Text(panedc, width=90, height=15, wrap="word")
            txt_texto.place(x=80,y=150)

            with open("data/categorias.txt", "r", encoding="UTF-8") as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "C++":
                        txt_texto.insert("1.0", param[1])

            #Button open
            def link():
                webbrowser.open_new_tab("https://www.w3schools.com/cpp/cpp_intro.asp")

            open_btn = Button(panedc, text="OPEN COURSE", fg="blue", font=("Arial, 16"), command= link)
            open_btn.place (x = 650,y = 450)

            lbl_c2 = Label(panedc, text="Comments: ", fg="black", font=("Arial, 12"))
            lbl_c2.place(x=90,y=420)

            def add_fav():
                with open("data/fav.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    for line in f:
                        user = line.split(";")
                        if Dados[0] == user[0]:
                            course_name = "C++"
                            user[len(user)-1] = course_name + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/fav.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    fav_c.configure(text="Remove from Favorites", command= remove_fav)

            def remove_fav():
                fav_c.configure(text="Add to Favorites", command= add_fav)
        
            with open('data/fav.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if Dados[0] == param[0]:
                            i = 1
                            while i < len(param)-1:
                                if param[i] == "C++":
                                    fav_c = Button(panedc,text="Remove from Favorites", fg="blue", font=("Arial, 16"), command= remove_fav)
                                    fav_c.place(x=650,y=550)
                                    i = 99
                                else:
                                    i = i + 1

                            if i != 99:        
                                fav_c = Button(panedc,text="Add to Favorites", fg="blue", font=("Arial, 16"), command= add_fav)
                            
                            fav_c.place(x=650,y=550)

            txt_cmt = Text(panedc,width=65, height=8, wrap='word')
            txt_cmt.place(x=80,y=450)

            #Ler os comentarios do ficheiro
            def ler():
                with open('data/comments.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")       
                        if param[0] == "C++":
                            i = 1
                            while i < len(param):
                                txt_cmt.insert("1.0", param[i] + "\n")
                                i = i + 1
            ler()

            #Add comment
            txt_add_cmt = Entry(panedc, width = 87, background = 'white')
            txt_add_cmt.place(x = 80, y = 605)


            def post_cmt():
                comment_txt = txt_add_cmt.get()
                comment = Dados[1] + ": " + comment_txt   #Name: "comment";

                with open("data/comments.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "C++"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = comment + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/comments.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)

                txt_cmt.delete("1.0", "end")
                ler()   #Update comment box

                

            btn_post = Button(panedc,text="Post", fg="blue", font=("Arial, 16"), command=post_cmt)
            btn_post.place(x=650,y=600)    

            
            def rate():
                info = Dados[1] + ";" + str(scale1.get())
                with open("data/rates.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "C++"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = info + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/rates.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    rate_btn.configure(state=DISABLED)


            #Rate
            rate_btn = Button(panedc, text="Rate", fg="blue", font=("Arial, 10"), command=rate)
            rate_btn.place(x=825,y=37)

            #In case the user did already vote in the past (can't vote again)
            with open('data/rates.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "C++":
                        i = 1
                        while i < len(param):
                            if param[i] == Dados[1]:
                                rate_btn.configure(state=DISABLED)
                            i = i + 2

            scale1 = Scale(panedc, width=20, from_= 0, to= 10, orient="horizontal")
            scale1.place(x=720,y=20)

        
        def windowHTML():
            window_html = Toplevel()
            window_html.geometry("900x700+500+100")
            window_html.title("HTML")
            window_html.resizable(0,0)
            panedhtml = PanedWindow(window_html, width=898, height=698, bd="8", relief="sunken")
            panedhtml.place(x=0,y=0)
            title_html = Label(panedhtml, text="HTML", fg="blue",bd= "8" ,relief="raised", font=("Arial", 34))
            title_html.place(x=370,y=20)
            lbl_html = Label(panedhtml, text="Description:", fg="blue", font=("Arial, 14"))
            lbl_html.place(x=90,y=110)

            txt_texto = Text(panedhtml, width=90, height=15, wrap="word")
            txt_texto.place(x=80,y=150)

            with open("data/categorias.txt", "r", encoding="UTF-8") as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "HTML":
                        txt_texto.insert("1.0", param[1])

            #Button open
            def link():
                webbrowser.open_new_tab("https://www.w3schools.com/html/html_intro.asp")

            open_btn = Button(panedhtml, text="OPEN COURSE", fg="blue", font=("Arial, 16"), command= link)
            open_btn.place (x = 650,y = 450)

            lbl_html2 = Label(panedhtml, text="Comments: ", fg="black", font=("Arial, 12"))
            lbl_html2.place(x=90,y=420)

            def add_fav():
                with open("data/fav.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    for line in f:
                        user = line.split(";")
                        if Dados[0] == user[0]:
                            course_name = "HTML"
                            user[len(user)-1] = course_name + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/fav.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    fav_html.configure(text="Remove from Favorites", command= remove_fav)

            def remove_fav():
                fav_html.configure(text="Add to Favorites", command= add_fav)
        
            with open('data/fav.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if Dados[0] == param[0]:
                            i = 1
                            while i < len(param)-1:
                                if param[i] == "HTML":
                                    fav_html = Button(panedhtml,text="Remove from Favorites", fg="blue", font=("Arial, 16"), command= remove_fav)
                                    fav_html.place(x=650,y=550)
                                    i = 99
                                else:
                                    i = i + 1

                            if i != 99:        
                                fav_html = Button(panedhtml,text="Add to Favorites", fg="blue", font=("Arial, 16"), command= add_fav)
                            
                            fav_html.place(x=650,y=550)

            txt_cmt = Text(panedhtml,width=65, height=8, wrap='word')
            txt_cmt.place(x=80,y=450)

            #Ler os comentarios do ficheiro
            def ler():
                with open('data/comments.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")       
                        if param[0] == "HTML":
                            i = 1
                            while i < len(param):
                                txt_cmt.insert("1.0", param[i] + "\n")
                                i = i + 1
            ler()

            #Add comment
            txt_add_cmt = Entry(panedhtml, width = 87, background = 'white')
            txt_add_cmt.place(x = 80, y = 605)


            def post_cmt():
                comment_txt = txt_add_cmt.get()
                comment = Dados[1] + ": " + comment_txt   #Name: "comment";

                with open("data/comments.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "HTML"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = comment + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/comments.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)

                txt_cmt.delete("1.0", "end")
                ler()   #Update comment box

                

            btn_post = Button(panedhtml,text="Post", fg="blue", font=("Arial, 16"), command=post_cmt)
            btn_post.place(x=650,y=600)    

            
            def rate():
                info = Dados[1] + ";" + str(scale1.get())
                with open("data/rates.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "HTML"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = info + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/rates.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    rate_btn.configure(state=DISABLED)


            #Rate
            rate_btn = Button(panedhtml, text="Rate", fg="blue", font=("Arial, 10"), command=rate)
            rate_btn.place(x=825,y=37)

            #In case the user did already vote in the past (can't vote again)
            with open('data/rates.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "HTML":
                        i = 1
                        while i < len(param):
                            if param[i] == Dados[1]:
                                rate_btn.configure(state=DISABLED)
                            i = i + 2

            scale1 = Scale(panedhtml, width=20, from_= 0, to= 10, orient="horizontal")
            scale1.place(x=720,y=20)

            
            
        def windowPy():
            window_py = Toplevel()
            window_py.geometry("900x700+500+100")
            window_py.title("Python")
            window_py.resizable(0,0)
            panedpy = PanedWindow(window_py, width=898, height=698, bd="8", relief="sunken")
            panedpy.place(x=0,y=0)
            title_py = Label(panedpy, text="Python", fg="blue",bd= "8" ,relief="raised", font=("Arial", 34))
            title_py.place(x=360,y=20)
            lbl_py = Label(panedpy, text="Description:", fg="blue", font=("Arial, 14"))
            lbl_py.place(x=90,y=110)

            txt_texto = Text(panedpy, width=90, height=15, wrap="word")
            txt_texto.place(x=80,y=150)

            with open("data/categorias.txt", "r", encoding="UTF-8") as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "Python":
                        txt_texto.insert("1.0", param[1])

            #Button open
            def link():
                webbrowser.open_new_tab("https://www.python.org/")

            open_btn = Button(panedpy, text="OPEN COURSE", fg="blue", font=("Arial, 16"), command= link)
            open_btn.place (x = 650,y = 450)

            lbl_py2 = Label(panedpy, text="Comments: ", fg="black", font=("Arial, 12"))
            lbl_py2.place(x=90,y=420)

            def add_fav():
                with open("data/fav.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    for line in f:
                        user = line.split(";")
                        if Dados[0] == user[0]:
                            course_name = "Python"
                            user[len(user)-1] = course_name + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/fav.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    fav_py.configure(text="Remove from Favorites", command= remove_fav)

            def remove_fav():
                fav_py.configure(text="Add to Favorites", command= add_fav)
        
            with open('data/fav.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if Dados[0] == param[0]:
                            i = 1
                            while i < len(param)-1:
                                if param[i] == "Python":
                                    fav_py = Button(panedpy,text="Remove from Favorites", fg="blue", font=("Arial, 16"), command= remove_fav)
                                    fav_py.place(x=650,y=550)
                                    i = 99
                                else:
                                    i = i + 1

                            if i != 99:        
                                fav_py = Button(panedpy,text="Add to Favorites", fg="blue", font=("Arial, 16"), command= add_fav)
                            
                            fav_py.place(x=650,y=550)

            txt_cmt = Text(panedpy,width=65, height=8, wrap='word')
            txt_cmt.place(x=80,y=450)

            #Ler os comentarios do ficheiro
            def ler():
                with open('data/comments.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")       
                        if param[0] == "Python":
                            i = 1
                            while i < len(param):
                                txt_cmt.insert("1.0", param[i] + "\n")
                                i = i + 1
            ler()

            #Add comment
            txt_add_cmt = Entry(panedpy, width = 87, background = 'white')
            txt_add_cmt.place(x = 80, y = 605)


            def post_cmt():
                comment_txt = txt_add_cmt.get()
                comment = Dados[1] + ": " + comment_txt   #Name: "comment";

                with open("data/comments.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "Python"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = comment + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/comments.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)

                txt_cmt.delete("1.0", "end")
                ler()   #Update comment box

                

            btn_post = Button(panedpy,text="Post", fg="blue", font=("Arial, 16"), command=post_cmt)
            btn_post.place(x=650,y=600)    

            
            def rate():
                info = Dados[1] + ";" + str(scale1.get())
                with open("data/rates.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "Python"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = info + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/rates.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    rate_btn.configure(state=DISABLED)


            #Rate
            rate_btn = Button(panedpy, text="Rate", fg="blue", font=("Arial, 10"), command=rate)
            rate_btn.place(x=825,y=37)

            #In case the user did already vote in the past (can't vote again)
            with open('data/rates.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "Python":
                        i = 1
                        while i < len(param):
                            if param[i] == Dados[1]:
                                rate_btn.configure(state=DISABLED)
                            i = i + 2

            scale1 = Scale(panedpy, width=20, from_= 0, to= 10, orient="horizontal")
            scale1.place(x=720,y=20)


        def windowCSS():
            window_css = Toplevel()
            window_css.geometry("900x700+500+100")
            window_css.title("CSS")
            window_css.resizable(0,0)
            panedcss = PanedWindow(window_css, width=898, height=698, bd="8", relief="sunken")
            panedcss.place(x=0,y=0)
            title_css = Label(panedcss, text="CSS", fg="blue",bd= "8" ,relief="raised", font=("Arial", 34))
            title_css.place(x=390,y=20)
            lbl_css = Label(panedcss, text="Description:", fg="blue", font=("Arial, 14"))
            lbl_css.place(x=90,y=110)

            txt_texto = Text(panedcss, width=90, height=15, wrap="word")
            txt_texto.place(x=80,y=150)

            with open("data/categorias.txt", "r", encoding="UTF-8") as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "CSS":
                        txt_texto.insert("1.0", param[1])

            #Button open
            def link():
                webbrowser.open_new_tab("https://www.w3schools.com/css/css_intro.asp")

            open_btn = Button(panedcss, text="OPEN COURSE", fg="blue", font=("Arial, 16"), command= link)
            open_btn.place (x = 650,y = 450)

            lbl_css2 = Label(panedcss, text="Comments: ", fg="black", font=("Arial, 12"))
            lbl_css2.place(x=90,y=420)

            def add_fav():
                with open("data/fav.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    for line in f:
                        user = line.split(";")
                        if Dados[0] == user[0]:
                            course_name = "CSS"
                            user[len(user)-1] = course_name + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/fav.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    fav_css.configure(text="Remove from Favorites", command= remove_fav)

            def remove_fav():
                fav_css.configure(text="Add to Favorites", command= add_fav)
        
            with open('data/fav.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if Dados[0] == param[0]:
                            i = 1
                            while i < len(param)-1:
                                if param[i] == "CSS":
                                    fav_css = Button(panedcss,text="Remove from Favorites", fg="blue", font=("Arial, 16"), command= remove_fav)
                                    fav_css.place(x=650,y=550)
                                    i = 99
                                else:
                                    i = i + 1

                            if i != 99:        
                                fav_css = Button(panedcss,text="Add to Favorites", fg="blue", font=("Arial, 16"), command= add_fav)
                            
                            fav_css.place(x=650,y=550)

            txt_cmt = Text(panedcss,width=65, height=8, wrap='word')
            txt_cmt.place(x=80,y=450)

            #Ler os comentarios do ficheiro
            def ler():
                with open('data/comments.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")       
                        if param[0] == "CSS":
                            i = 1
                            while i < len(param):
                                txt_cmt.insert("1.0", param[i] + "\n")
                                i = i + 1
            ler()

            #Add comment
            txt_add_cmt = Entry(panedcss, width = 87, background = 'white')
            txt_add_cmt.place(x = 80, y = 605)


            def post_cmt():
                comment_txt = txt_add_cmt.get()
                comment = Dados[1] + ": " + comment_txt   #Name: "comment";

                with open("data/comments.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "CSS"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = comment + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/comments.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)

                txt_cmt.delete("1.0", "end")
                ler()   #Update comment box

                

            btn_post = Button(panedcss,text="Post", fg="blue", font=("Arial, 16"), command=post_cmt)
            btn_post.place(x=650,y=600)    

            
            def rate():
                info = Dados[1] + ";" + str(scale1.get())
                with open("data/rates.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "CSS"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = info + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/rates.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    rate_btn.configure(state=DISABLED)


            #Rate
            rate_btn = Button(panedcss, text="Rate", fg="blue", font=("Arial, 10"), command=rate)
            rate_btn.place(x=825,y=37)

            #In case the user did already vote in the past (can't vote again)
            with open('data/rates.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "CSS":
                        i = 1
                        while i < len(param):
                            if param[i] == Dados[1]:
                                rate_btn.configure(state=DISABLED)
                            i = i + 2

            scale1 = Scale(panedcss, width=20, from_= 0, to= 10, orient="horizontal")
            scale1.place(x=720,y=20)

        
        def windowGo():
            window_go = Toplevel()
            window_go.geometry("900x700+500+100")
            window_go.title("Go")
            window_go.resizable(0,0)
            panedgo = PanedWindow(window_go, width=898, height=698, bd="8", relief="sunken")
            panedgo.place(x=0,y=0)
            title_go = Label(panedgo, text="GO", fg="blue",bd= "8" ,relief="raised", font=("Arial", 34))
            title_go.place(x=400,y=20)
            lbl_go = Label(panedgo, text="Description:", fg="blue", font=("Arial, 14"))
            lbl_go.place(x=90,y=110)

            txt_texto = Text(panedgo, width=90, height=15, wrap="word")
            txt_texto.place(x=80,y=150)

            with open("data/categorias.txt", "r", encoding="UTF-8") as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "Go":
                        txt_texto.insert("1.0", param[1])

            #Button open
            def link():
                webbrowser.open_new_tab("https://go.dev/")

            open_btn = Button(panedgo, text="OPEN COURSE", fg="blue", font=("Arial, 16"), command= link)
            open_btn.place (x = 650,y = 450)

            lbl_go2 = Label(panedgo, text="Comments: ", fg="black", font=("Arial, 12"))
            lbl_go2.place(x=90,y=420)
            
            def add_fav():
                with open("data/fav.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    for line in f:
                        user = line.split(";")
                        if Dados[0] == user[0]:
                            course_name = "Go"
                            user[len(user)-1] = course_name + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/fav.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    fav_go.configure(text="Remove from Favorites", command= remove_fav)

            def remove_fav():
                fav_go.configure(text="Add to Favorites", command= add_fav)
        
            with open('data/fav.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if Dados[0] == param[0]:
                            i = 1
                            while i < len(param)-1:
                                if param[i] == "Go":
                                    fav_go = Button(panedgo,text="Remove from Favorites", fg="blue", font=("Arial, 16"), command= remove_fav)
                                    fav_go.place(x=650,y=550)
                                    i = 99
                                else:
                                    i = i + 1

                            if i != 99:        
                                fav_go = Button(panedgo,text="Add to Favorites", fg="blue", font=("Arial, 16"), command= add_fav)
                            
                            fav_go.place(x=650,y=550)

            txt_cmt = Text(panedgo,width=65, height=8, wrap='word')
            txt_cmt.place(x=80,y=450)

            #Ler os comentarios do ficheiro
            def ler():
                with open('data/comments.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")       
                        if param[0] == "Go":
                            i = 1
                            while i < len(param):
                                txt_cmt.insert("1.0", param[i] + "\n")
                                i = i + 1
            ler()

            #Add comment
            txt_add_cmt = Entry(panedgo, width = 87, background = 'white')
            txt_add_cmt.place(x = 80, y = 605)


            def post_cmt():
                comment_txt = txt_add_cmt.get()
                comment = Dados[1] + ": " + comment_txt   #Name: "comment";

                with open("data/comments.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "Go"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = comment + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/comments.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)

                txt_cmt.delete("1.0", "end")
                ler()   #Update comment box

                

            btn_post = Button(panedgo,text="Post", fg="blue", font=("Arial, 16"), command=post_cmt)
            btn_post.place(x=650,y=600)    

            
            def rate():
                info = Dados[1] + ";" + str(scale1.get())
                with open("data/rates.txt", "r", encoding="UTF-8") as f:
                    new_text = ""
                    course_name = "Go"
                    for line in f:
                        user = line.split(";")
                        if user[0] == course_name:
                            user[len(user)-1] = info + ";" + "\n"
                            new_text = new_text + ";".join(user)
                        else:
                            new_text = new_text + ";".join(user)
                with open("data/rates.txt", "w", encoding="UTF-8") as f:
                    f.write(new_text)
                    rate_btn.configure(state=DISABLED)


            #Rate
            rate_btn = Button(panedgo, text="Rate", fg="blue", font=("Arial, 10"), command=rate)
            rate_btn.place(x=825,y=37)

            #In case the user did already vote in the past (can't vote again)
            with open('data/rates.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "Go":
                        i = 1
                        while i < len(param):
                            if param[i] == Dados[1]:
                                rate_btn.configure(state=DISABLED)
                            i = i + 2

            scale1 = Scale(panedgo, width=20, from_= 0, to= 10, orient="horizontal")
            scale1.place(x=720,y=20)

        
        js = Button(panel1, image = js_img, relief='raised', bd=4, width=150, height=100, command= windowScript)
        js.place (x = 50,y = 30)
            
                
        c = Button(panel1, image = c_img, relief='raised',bd=4, width=150, height=100, command= windowC)
        c.place (x = 50,y = 180)
                        

        html = Button(panel1, image = html_img, relief='raised', bd=4, width=150, height=100, command=windowHTML)
        html.place (x = 50,y = 330)


        pyth = Button(panel1, image = py_img, relief='raised', bd=4, width=150, height=100, command= windowPy)
        pyth.place (x = 350,y = 30)

        css_tag = Button(panel1, image = css_img, relief='raised', bd=4, width=150, height=100, command= windowCSS)
        css_tag.place (x = 350,y = 180)

        goo = Button(panel1, image = go_img, relief='raised', bd=4, width=150, height=100, command=windowGo)
        goo.place (x = 350,y = 330)

        #Search function
        def search():
            js.configure(state=DISABLED)
            c.configure(state=DISABLED)
            html.configure(state=DISABLED)
            pyth.configure(state=DISABLED)
            css_tag.configure(state=DISABLED)
            goo.configure(state=DISABLED)

            result = search_box.get()
            if result.count(' ') == len(result):
                js.configure(state=NORMAL)
                c.configure(state=NORMAL)
                html.configure(state=NORMAL)
                pyth.configure(state=NORMAL)
                css_tag.configure(state=NORMAL)
                goo.configure(state=NORMAL)
            elif (result[0] == "P" and result[1] == "y") or (result[0] == "p" and result[1] == "y") or (result[0] == "P" and result[1] == "Y"):
                pyth.configure(state=NORMAL)
            elif result[0] == "J" or result[0] == "j":
                js.configure(state=NORMAL)
            elif (result[0] == "H" and result[1] == "m") or (result[0] == "H" and result[1] == "M") or (result[0] == "h" and result[1] == "m"):
                html.configure(state=NORMAL)
            elif result == "Go" or result == "GO" or result == "go" or result == "G" or result == "g":
                goo.configure(state=NORMAL)
            elif result == 'C' or result == 'c':
                c.configure(state=NORMAL)
                css_tag.configure(state=NORMAL)
            elif ((result[0] == "C" or result[0] == "c" ) and result[1] == "+"):
                c.configure(state=NORMAL)
            elif (result[0] == "C" or result[0] == "c") and (result[0] == "S" or result[0] == "s"):
                css_tag.configure(state=NORMAL)

        #Search 
        search_box = Entry(main_painel, width = 30, background = 'white')
        search_btn =  Button(main_painel, text = "search", relief='flat', bd=1, font=("Arial, 7"), command= search)
        search_box.place(x = 1000, y = 30)
        search_btn.place(x = 1185, y =30)
        
        def create():
            new = Toplevel()
            new.geometry("210x300+500+100")
            new.title("Favorites List")
            new.resizable(0,0)
            paned1 = PanedWindow(new, width=270, height=350, bd="6", relief="sunken" )
            paned1.place(x=0,y=0)
            with open('data/fav.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if Dados[0] == param[0]:
                        lista = []
                        i = 1
                        while i < len(param)-1:
                            lista.append(param[i])
                            i = i + 1
            lbox = Listbox(paned1, height= 11, width=17, font="Arial, 18",selectmode="multiple", fg="blue")
            for i in lista:
                lbox.insert(END, i)
            lbox.place(x=0,y=0)
        
        btn_filter = Button(main_painel, text = "Favorites List", font = ('Arial, 18'),width=10, height=2, fg = 'blue', relief='flat', background = 'white', command=create)
        btn_filter.place (x = 970,y = 270)

        def rating():
            new2 = Toplevel()
            new2.geometry("900x700+500+100")
            new2.title("Rate")
            new2.resizable(0,0)
            paned2 = PanedWindow(new2, width=898, height=698, bd="8", relief="sunken")
            paned2.place(x=0,y=0)
            lbl_title = Label(new2, text="Courses Rate Scores", fg="blue",bd= "8" ,relief="raised", font=("Arial", 34))
            lbl_title.place(x=240,y=20)

            with open('data/rates.txt', 'r', encoding='UTF-8') as f:
                for line in f:
                    param = line.split(";")
                    if param[0] == "JavaScript":
                        i = 2
                        soma = 0
                        n_total = 0
                        while i <= len(param)-1:
                            soma = soma + int(param[i])
                            n_total = n_total + 1
                            i = i + 2
                        rate_js = soma / n_total
                    if param[0] == "C++":
                        i = 2
                        soma = 0
                        n_total = 0
                        while i <= len(param)-1:
                            soma = soma + int(param[i])
                            n_total = n_total + 1
                            i = i + 2
                        rate_c = soma / n_total
                    if param[0] == "HTML":
                        i = 2
                        soma = 0
                        n_total = 0
                        while i <= len(param)-1:
                            soma = soma + int(param[i])
                            n_total = n_total + 1
                            i = i + 2
                        rate_html = soma / n_total
                    if param[0] == "Python":
                        i = 2
                        soma = 0
                        n_total = 0
                        while i <= len(param)-1:
                            soma = soma + int(param[i])
                            n_total = n_total + 1
                            i = i + 2
                        rate_py = soma / n_total
                    if param[0] == "CSS":
                        i = 2
                        soma = 0
                        n_total = 0
                        while i <= len(param)-1:
                            soma = soma + int(param[i])
                            n_total = n_total + 1
                            i = i + 2
                        rate_css = soma / n_total
                    if param[0] == "Go":
                        i = 2
                        soma = 0
                        n_total = 0
                        while i <= len(param)-1:
                            soma = soma + int(param[i])
                            n_total = n_total + 1
                            i = i + 2
                        rate_go = soma / n_total

            # Label e scale js
            lbl_js = Label(new2, text = "JavaScript", fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_js.place(x=240,y=130)
            lbl_js_rate = Label(new2, text = rate_js, fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_js_rate.place(x=600,y=130)

            #Label e scale c++
            lbl_c = Label(new2, text = "C++", fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_c.place(x=240,y=210)
            lbl_c_rate = Label(new2, text = rate_c, fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_c_rate.place(x=600,y=210)


            # Label e scale html
            lbl_html = Label(new2, text = "HTML", fg="blue", bd="8", relief="raised", font=("Arial", 20))
            lbl_html.place(x=240,y=290)
            lbl_html_rate = Label(new2, text = rate_c, fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_html_rate.place(x=600,y=290)

            # Label e scale py
            lbl_py = Label(new2, text = "Python", fg="blue", bd="8", relief="raised", font=("Arial", 20))
            lbl_py.place(x=240,y=370)   
            lbl_py_rate = Label(new2, text = rate_py, fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_py_rate.place(x=600,y=370)   

            # Label e scale CSS
            lbl_css = Label(new2, text = "CSS", fg="blue", bd="8", relief="raised", font=("Arial", 20))
            lbl_css.place(x=240,y=450)  
            lbl_css_rate = Label(new2, text = rate_css, fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_css_rate.place(x=600,y=450)    

            # Label e scale Go
            lbl_go = Label(new2, text = "Go", fg="blue", bd="8", relief="raised", font=("Arial", 20))
            lbl_go.place(x=240,y=530)    
            lbl_go_rate = Label(new2, text = rate_go, fg="blue",bd="8", relief="raised", font=("Arial", 20))
            lbl_go_rate.place(x=600,y=530)  
            
        
        btn_rate = Button(main_painel, text = "Most Rated", font = ('Arial, 18'),width=10, height=2, fg = 'blue', relief='flat', background = 'white', command= rating)
        btn_rate.place (x = 970,y = 370)

        
        btn_rate = Button(main_painel, text = "Notifications", font = ('Arial, 18'),width=10, height=2, fg = 'blue', relief='flat', background = 'white', command="noaction")
        btn_rate.place (x = 970,y = 470)

        canvas_main = Canvas(main_painel, width = 343, height = 200, background='#b9b9b9')
        canvas_main.place(x = 440, y = 25)
        canvas_main.create_image(150,103, image = main_img)

    btn_menu()
    fundo()
    start()
    clock()
    messagebox.showinfo(title="Welcome!", message="Enjoy :)")
    window.mainloop()
