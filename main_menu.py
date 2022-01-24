from tkinter import *
from tkinter.tix import Tree
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
from time import strftime
from tkinter import messagebox
import start_menu

# Estrutura
def main_menu(usernumber):
    window = Tk()
    window.geometry('1250x800+300+100')
    window.title("Online Courses Manager")
    window.resizable(0,0)
    window.configure(background='#b9b9b9')
    window.iconbitmap("png\hat.ico")


# Retrieve de dados do User
    def addinfo():
        global Dados
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
    relogio_label.place(x=1150, y=8)


    #Imagens
    menu_abrir = PhotoImage(file = 'png/button.png')
    menu_fechar = PhotoImage(file = 'png/menu_fechar.png')
    user_avatar = PhotoImage(file = 'png/user.png')
    js_img = PhotoImage(file = 'png/js.png')
    c_img = PhotoImage(file = 'png/c.png')
    html_img = PhotoImage(file = 'png/html.png')
    py_img = PhotoImage(file = 'png/py.png')
    css_img = PhotoImage(file = 'png/css.png')
    go_img = PhotoImage(file = 'png/go.png')



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
            print('admin')

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

        def save_coments():
            ficheiro = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/data/coments.txt"
            linha = txt_texto.get("1.0","end")
            f = open(ficheiro, "w", encoding="utf-8")
            f.write(linha)
            f.close()

        # Box para os cursos
        def painel():
            global panel1
            panel1 = PanedWindow(main_painel, width=570, height=470, bd="6", relief="sunken")
            panel1.place(x=320,y=270)    
        
        painel()

        # Botões box central
        def windowScript():
            windowjs = Toplevel()
            windowjs.geometry("900x700+500+100")
            windowjs.title("JavaScript")
            windowjs.resizable()
            panedjs = PanedWindow(windowjs, width=898, height=698, bd="8", relief="sunken")
            panedjs.place(x=0,y=0)
            titlejs = Label(panedjs, text="JavaScript", fg="blue",bd= "8" ,relief="raised", font=("Helvetica", 34))
            titlejs.place(x=340,y=20)
            lbl_js = Label(panedjs, text="Challenge:", fg="blue", font=("Helvetica, 14"))
            lbl_js.place(x=90,y=110)
            txt_js = Text(panedjs, width=30, height=20, wrap="word")
            txt_js.place(x=80,y=150)
            lbl_js2 = Label(panedjs, text="Comments: ", fg="black", font=("Helvetica, 12"))
            lbl_js2.place(x=90,y=500)
            btn_js = Button(panedjs,text="Save", fg="blue", font=("Helvetica, 16"), command= save_coments)
            btn_js.place(x=650,y=600)
            fav_js = Button(panedjs,text="Add to Favorites", fg="blue", font=("Helvetica, 16"))
            fav_js.place(x=650,y=550)
            cmt_js = Text(panedjs,width=30, height=5, wrap='word')
            cmt_js.place(x=80,y=550)
        
        def windowC():
            window_cpro = Toplevel()
            window_cpro.geometry("900x700+500+100")
            window_cpro.title("C++")
            window_cpro.resizable(0,0)
            panedc = PanedWindow(window_cpro, width=898, height=698, bd="8", relief="sunken")
            panedc.place(x=0,y=0)
            titlec = Label(panedc, text="C++", fg="blue",bd= "8" ,relief="raised", font=("Helvetica", 34))
            titlec.place(x=400,y=20)
            lbl_c = Label(panedc, text="Challenge:", fg="blue", font=("Helvetica, 14"))
            lbl_c.place(x=90,y=110)
            txt_c = Text(panedc, width=30, height=20, wrap="word")
            txt_c.place(x=80,y=150)
            lbl_c2 = Label(panedc, text="Comments: ", fg="black", font=("Helvetica, 12"))
            lbl_c2.place(x=90,y=500)
            btn_c = Button(panedc,text="Save", fg="blue", font=("Helvetica, 16"), command= save_coments)
            btn_c.place(x=650,y=600)
            fav_c = Button(panedc,text="Add to Favorites", fg="blue", font=("Helvetica, 16"))
            fav_c.place(x=650,y=550)
            cmt_c = Text(panedc,width=30, height=5, wrap='word')
            cmt_c.place(x=80,y=550)    
        
        def windowHTML():
            window_html = Toplevel()
            window_html.geometry("900x700+500+100")
            window_html.title("HTML")
            window_html.resizable(0,0)
            panedhtml = PanedWindow(window_html, width=898, height=698, bd="8", relief="sunken")
            panedhtml.place(x=0,y=0)
            title_html = Label(panedhtml, text="JavaScript", fg="blue",bd= "8" ,relief="raised", font=("Helvetica", 34))
            title_html.place(x=340,y=20)
            lbl_html = Label(panedhtml, text="Challenge:", fg="blue", font=("Helvetica, 14"))
            lbl_html.place(x=90,y=110)
            txt_html = Text(panedhtml, width=30, height=20, wrap="word")
            txt_html.place(x=80,y=150)
            lbl_html2 = Label(panedhtml, text="Comments: ", fg="black", font=("Helvetica, 12"))
            lbl_html2.place(x=90,y=500)
            btn_html = Button(panedhtml,text="Save", fg="blue", font=("Helvetica, 16"), command= save_coments)
            btn_html.place(x=650,y=600)
            fav_html = Button(panedhtml,text="Add to Favorites", fg="blue", font=("Helvetica, 16"))
            fav_html.place(x=650,y=550)
            cmt_html = Text(panedhtml,width=30, height=5, wrap='word')
            cmt_html.place(x=80,y=550)


        js = Button(panel1, image = js_img, relief='raised', bd=4, width=150, height=100, command= windowScript)
        js.place (x = 50,y = 30)
            
                

        c = Button(panel1, image = c_img, relief='raised',bd=4, width=150, height=100, command= windowC)
        c.place (x = 50,y = 180)
                        


        html = Button(panel1, image = html_img, relief='raised', bd=4, width=150, height=100, command=windowHTML)
        html.place (x = 50,y = 330)



        pyth = Button(panel1, image = py_img, relief='raised', bd=4, width=150, height=100)
        pyth.place (x = 350,y = 30)

        css_tag = Button(panel1, image = css_img, relief='raised', bd=4, width=150, height=100)
        css_tag.place (x = 350,y = 180)

        google = Button(panel1, image = go_img, relief='raised', bd=4, width=150, height=100)
        google.place (x = 350,y = 330)

        """
        # Botões right side
        # new Window para a lista dos favoritos
        def favorites(username):
            global datafav
            f = open("/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/data/fav.txt", 'r', encoding='UTF-8')
            linha = f.readlines()
            f.close()
            datafav = split(';')     
        favorites()
        """
        def create():
            new = Toplevel()
            new.geometry("270x350+500+100")
            new.title("Favorites List")
            new.resizable(0,0)
            paned1 = PanedWindow(new, width=270, height=350, bd="6", relief="sunken" )
            paned1.place(x=0,y=0)
            lista = ["Python", "CSS", "HTML", "C++", "Go", "JavaScript"]
            lbox = Listbox(paned1, height= 11, width=17, font="Arial, 18",selectmode="multiple", fg="blue")
            for i in lista:
                lbox.insert(END, i)
            lbox.place(x=0,y=0)
            file = open("/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projecto/data/fav.txt", "r", encoding="utf-8")
            linhas = file.readlines()
            file.close()
            

        
        btn_filter = Button(main_painel, text = "Favorites List", font = ('Arial, 18'),width=10, height=2, fg = 'blue', relief='flat', background = 'white', command=create)
        btn_filter.place (x = 970,y = 270)


        def rating():
            new2 = Toplevel()
            new2.geometry("900x700+500+100")
            new2.title("Rate")
            new2.resizable()
            paned2 = PanedWindow(new2, width=898, height=698, bd="8", relief="sunken")
            paned2.place(x=0,y=0)
            lbl_title = Label(new2, text="Rate our Courses", fg="blue",bd= "8" ,relief="raised", font=("Helvetica", 34))
            lbl_title.place(x=270,y=20)
            # Label e scale js
            lbl_js = Label(new2, text = "JavaScript", fg="blue",bd="8", relief="raised", font=("Helvetica", 20))
            lbl_js.place(x=240,y=130)
            scale1 = Scale(new2, width=20, from_= 0, to= 10, orient="horizontal")
            scale1.place(x=560,y=120)
            #Label e scale c++
            lbl_c = Label(new2, text = "C++", fg="blue",bd="8", relief="raised", font=("Helvetica", 20))
            lbl_c.place(x=240,y=210)
            scale2 = Scale(new2, width=20, from_= 0, to= 10,orient="horizontal")
            scale2.place(x=560,y=200)
            # Label e scale html
            lbl_html = Label(new2, text = "HTML", fg="blue", bd="8", relief="raised", font=("Helvetica", 20))
            lbl_html.place(x=240,y=290)
            scale3 = Scale(new2, width=20, from_= 0, to= 10, orient="horizontal")
            scale3.place(x=560,y=280)
            # Label e scale py
            lbl_py = Label(new2, text = "Python", fg="blue", bd="8", relief="raised", font=("Helvetica", 20))
            lbl_py.place(x=240,y=370)      
            scale4 = Scale(new2, width=20, from_= 0, to= 10, orient="horizontal")
            scale4.place(x=560,y=360)
            # Label e scale CSS
            lbl_css = Label(new2, text = "CSS", fg="blue", bd="8", relief="raised", font=("Helvetica", 20))
            lbl_css.place(x=240,y=450)      
            scale5 = Scale(new2, width=20, from_= 0, to= 10, orient="horizontal")
            scale5.place(x=560,y=440)
            # Label e scale Go
            lbl_go = Label(new2, text = "Go", fg="blue", bd="8", relief="raised", font=("Helvetica", 20))
            lbl_go.place(x=240,y=530)      
            scale4 = Scale(new2, width=20, from_= 0, to= 10, orient="horizontal")
            scale4.place(x=560,y=520)
            # Botao save
            btn_save = Button(new2, text="Save", fg="blue",relief="raised", bd="6",font=("Helvetica", 22))
            btn_save.place(x=730,y=620)
            

        
        btn_rate = Button(main_painel, text = "Most Rated", font = ('Arial, 18'),width=10, height=2, fg = 'blue', relief='flat', background = 'white', command= rating)
        btn_rate.place (x = 970,y = 370)

        
        btn_rate = Button(main_painel, text = "Notifications", font = ('Arial, 18'),width=10, height=2, fg = 'blue', relief='flat', background = 'white', command="noaction")
        btn_rate.place (x = 970,y = 470)



    btn_menu()
    fundo()
    start()
    clock()
    messagebox.showinfo(title="Welcome!", message="Enjoy :)")
    window.mainloop()
