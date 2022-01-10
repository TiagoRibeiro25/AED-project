from tkinter import *
from tkinter import messagebox
from datetime import datetime
from PIL import ImageTk,Image
import main_menu

def start_window():

    #Criar janela principal
    start_window = Tk()  
    start_window.geometry('850x400+500+300')
    start_window.resizable(0,0)
    start_window.configure(background='black')
    start_window.iconbitmap("hat.ico")
        
    def start():
        start_window.title('Online Courses Manager')

        def Log_In():
            start_window.title('Online Courses Manager - Log In')
            painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='#b9b9b9')
            painel_inicial.place(x = 40, y = 33)

            #container Canvas
            ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='#b9b9b9')
            ctn_canvas.place(x = 0, y = 0)
            ctn_canvas.create_image(320,170, image = img1)

            #Botao voltar
            btn_voltar = Button(painel_inicial, text = 'back', font = ('Arial', 10), fg = 'black', relief='raised', background = '#b9b9b9', width=8, height=1, command=start)
            btn_voltar.place (x = 0,y = 0)

            #Painel da direita (log-In)
            painel_log_in = PanedWindow(painel_inicial, width = 260, height= 310, background='white')
            painel_log_in.place(x = 500, y = 10)

            lbl_Log_In = Label(painel_log_in, text = 'Log In', fg='black', font = ('Arial', 20), background='white')
            lbl_Log_In.place(x = 90, y = 0)

            #Username
            lbl_name = Label(painel_log_in, text = 'Name:', fg='black', font = ('Arial', 15), background='white')
            lbl_name.place(x = 10, y = 60)
            Entry_name = Entry(painel_log_in, width = 27, background = 'white')
            Entry_name.place(x = 75, y = 66)

            #Password
            lbl_pw = Label(painel_log_in, text = 'Password:', fg='black', font = ('Arial', 14), background='white')
            lbl_pw.place(x = 10, y = 95)
            Entry_pw = Entry(painel_log_in, width = 22, background = 'white', show='*')
            Entry_pw.place(x = 105, y = 101)

            def verify():
                global user_number
                verified = 0
                with open('data/utilizadores.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        param = line.split(";")
                        if Entry_name.get() == param[1] and Entry_pw.get() == param[3]:
                            verified = 1
                            user_number = param[0]
                            start_window.destroy()
                            main_menu.main_menu(user_number)
                    if verified == 0:
                        messagebox.showerror(
                            title="Warning!", message="The username or password are incorrect!")

            #botao next
            btn_next = Button(painel_log_in, text = 'Next', font = ('Arial', 15), fg = 'white', relief='groove', background = 'green', width=15, command=verify)
            btn_next.place (x = 44,y = 160)

            #botao caso não tenha conta
            btn_no_account = Button(painel_log_in, text = "Don't have an account? Click here", font = ('Arial', 10), fg = 'blue', relief='flat', background = 'white', command=Sign_Up)
            btn_no_account.place (x = 25,y = 270)


        def Sign_Up():
            start_window.title('Online Courses Manager - Sign In')
            painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='#b9b9b9')
            painel_inicial.place(x = 40, y = 33)

            #container Canvas
            ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='#b9b9b9')
            ctn_canvas.place(x = 0, y = 0)
            ctn_canvas.create_image(320,170, image = img1)

            #Botao voltar
            btn_voltar = Button(painel_inicial, text = 'back', font = ('Arial', 10), fg = 'black', relief='raised', background = '#b9b9b9', width=8, height=1, command=start)
            btn_voltar.place (x = 0,y = 0)

            #Painel da direita (Sign-up)
            painel_sign_up = PanedWindow(painel_inicial, width = 260, height= 310, background='white')
            painel_sign_up.place(x = 500, y = 10)

            lbl_Log_In = Label(painel_sign_up, text = 'Sign Up', fg='black', font = ('Arial', 20), background='white')
            lbl_Log_In.place(x = 85, y = 0)

            #Username
            lbl_name = Label(painel_sign_up, text = 'Name:', fg='black', font = ('Arial', 15), background='white')
            lbl_name.place(x = 10, y = 60)
            Entry_name = Entry(painel_sign_up, width = 27, background = 'white')
            Entry_name.place(x = 75, y = 66)

            #Email
            lbl_email = Label(painel_sign_up, text = 'Email:', fg='black', font = ('Arial', 14), background='white')
            lbl_email.place(x = 10, y = 95)
            Entry_email = Entry(painel_sign_up, width = 27, background = 'white')
            Entry_email.place(x = 75, y = 101)

            #Password
            lbl_pw = Label(painel_sign_up, text = 'Password:', fg='black', font = ('Arial', 14), background='white')
            lbl_pw.place(x = 10, y = 130)
            Entry_pw = Entry(painel_sign_up, width = 22, background = 'white', show='*')
            Entry_pw.place(x = 105, y = 136)
            
            #Mostrar password
            def show_pw():
                pw_info = val.get()
                if pw_info == 1:
                    Entry_pw.configure(show='')
                    Entry_pw.configure(state=DISABLED)
                if pw_info == 0:
                    Entry_pw.configure(show='*')
                    Entry_pw.configure(state=NORMAL)

            val = IntVar(0)    
            btn_pw_visible = Checkbutton(painel_sign_up, text = "Show Password", font = ('Arial', 7), background = 'white', variable= val, command=show_pw)
            btn_pw_visible.place (x = 10,y = 155)

            #Tipo de usuário (user/admin)
            lbl_user_type = Label(painel_sign_up, text = 'Choose which type of user:', fg='black', font = ('Arial', 12), background='white')
            lbl_user_type.place(x = 10, y = 185)

            user_type_selected = StringVar()
            User = Radiobutton(painel_sign_up, text='User', font = ('Arial', 10), background = 'white', variable= user_type_selected, value='user')
            Admin = Radiobutton(painel_sign_up, text='Admin', font = ('Arial', 10), background = 'white', variable= user_type_selected, value='admin')
            User.place(x = 10, y = 210)
            Admin.place(x = 150, y = 210)
            user_type_selected.set('user')   #Por predefinição, o tipo de usuário escolhido será do tipo "user"
            #user_type_selected.get() - para pegar o valor user/admin

            lbl_info = Label(painel_inicial, text="Username - can't exceed 29 letters\n\nEmail - must be a valid\n\nPassword - must have at least\n a letter/number\n\nUser type - Only one can be selected\ndefault selected - User", fg='black', font = ('Arial', 8), background='#b9b9b9')
            lbl_info.place(x = 313, y = 100)


            #Cruzes ao lado direito de cada linha (user,email,password). Caso as informações tenham erros, a funçao verify irá torná-la visivel
            lbl_red1 = Label(painel_sign_up, text='X', fg='white', font = ('Arial', 10), background='white',height=1)
            lbl_red2 = Label(painel_sign_up, text='X', fg='white', font = ('Arial', 10), background='white',height=1)
            lbl_red3 = Label(painel_sign_up, text='X', fg='white', font = ('Arial', 10), background='white',height=1)
            lbl_red1.place(x = 242, y = 65)
            lbl_red2.place(x = 242, y = 100)
            lbl_red3.place(x = 242, y = 135)

            #FUnçao que verifica os dados introduzidos
            def verify():
                name_correct = 0
                email_correct = 0
                pw_correct = 0

                name = Entry_name.get()              #nome
                name_letters = len(name)             #Numero de caracteres do nome
                email =Entry_email.get()             #Email
                pw = Entry_pw.get()                  #Password

                #name
                if name_letters > 29 or name_letters == 0:          #Máximo 29 caracteres para evitar nomes muito grandes
                    lbl_red1.configure(text='X', fg='red')
                elif name.count(' ') == name_letters:                  #Verificar se o nome tem alguma letra/número (não seja so espaços)
                    lbl_red1.configure(text='X', fg='red')
                else:
                    lbl_red1.configure(text='✔', fg='green')
                    name_correct = 1
                    Entry_name.configure(state=DISABLED)
                    
                #email
                if email.find('@') == -1 or email.find('.') == -1:  #verifica se o email tem um '@' e um '.'
                    lbl_red2.configure(text='X', fg='red')
                elif email.rfind('.') < email.find('@'):            #Verifica se o '.' está depois do '@'  (xxxx@xxx.xx)
                    lbl_red2.configure(text='X', fg='red')          #                                           ^   ^
                else:
                    lbl_red2.configure(text='✔', fg='green')
                    email_correct = 1
                    Entry_email.configure(state=DISABLED)

                #password
                if pw.count(' ') == len(pw) or pw == '':            #Verificar se existe uma senha e se a senha tem alguma letra ou número (nao seja so espaços)
                    lbl_red3.configure(text='X', fg='red')
                else:
                    lbl_red3.configure(text='✔', fg='green')
                    pw_correct = 1
                    Entry_pw.configure(state=DISABLED)


                #REALIZAR O REGISTO!
                if name_correct == 1 and email_correct == 1 and pw_correct == 1:
                    t = datetime.now().date()
                    date = t.strftime('%d/%m/%Y')
                    messagebox.showinfo(
                        title="Sucess", message="Your account has been created!")
                    with open("data/utilizadores.txt", "r", encoding="UTF-8") as f:
                        cont_line=f.readlines()
                    #ID, Nome, Email, Senha, Tipo de user, Data de registo
                    save = '\n' + str(len(cont_line)) + ';' + Entry_name.get() + ';' + Entry_email.get() + ';' + Entry_pw.get() + ';' + user_type_selected.get() + ';' + date + ';'
                    with open("data/utilizadores.txt", "a", encoding="UTF-8") as f: 
                        f.write(save)  
                    
                    btn_create_account.configure(state=DISABLED)
                                 
            #Botão reset de dados 
            #(caso o utilizador tenha inserido um nome/email/senha válida mas queira alterar)
            def reset_data():
                reset_info = reset.get()
                if reset_info == 1:
                    Entry_name.configure(state=NORMAL)
                    Entry_name.delete(0, END)
                    lbl_red1.configure(fg='white')

                    Entry_email.configure(state=NORMAL)
                    Entry_email.delete(0, END)
                    lbl_red2.configure(fg='white')

                    Entry_pw.configure(state=NORMAL)
                    Entry_pw.delete(0, END)
                    lbl_red3.configure(fg='white')

                    btn_create_account.configure(state=NORMAL)
                    reset.set(0)

            reset = IntVar(0)    
            btn_pw_visible = Checkbutton(painel_sign_up, text = "Reset data", font = ('Arial', 7), fg='red', background = 'white', variable= reset, command=reset_data)
            btn_pw_visible.place (x = 170,y = 155)

            #Botão para verificar e criar conta
            btn_create_account = Button(painel_sign_up, text = 'Create Account', font = ('Arial', 10), fg = 'white', relief='groove', background = 'green', width=15, command=verify)
            btn_create_account.place (x = 65,y = 240)

            #botao caso não tenha conta
            btn_no_account = Button(painel_sign_up, text = "Already have an account? Click here", font = ('Arial', 10), fg = 'blue', relief='flat', background = 'white', command=Log_In)
            btn_no_account.place (x = 20,y = 270)


        def info():
            start_window.title('Online Courses Manager - Extra Info')
            painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='#b9b9b9')
            painel_inicial.place(x = 40, y = 33)

            #container Canvas
            ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='#b9b9b9')
            ctn_canvas.place(x = 0, y = 0)
            ctn_canvas.create_image(320,170, image = img1)

            #Botao voltar
            btn_voltar = Button(painel_inicial, text = 'back', font = ('Arial', 10), fg = 'black', relief='raised', background = '#b9b9b9', width=8, height=1, command=start)
            btn_voltar.place (x = 0,y = 0)

            #Informação sobre o trabalho
            lbl_info1 = Label(painel_inicial, text = 'TSIW', fg='black', font = ('Arial', 22), background='#b9b9b9')
            lbl_info2 = Label(painel_inicial, text = 'AED Project\n2021-2022', fg='black', font = ('Arial', 18), background='#b9b9b9')
            lbl_info1.place(x = 360, y = 100)
            lbl_info2.place(x = 335, y = 140)

            #Painel da direita (Ficha-Técnica)
            painel_log_in = PanedWindow(painel_inicial, width = 260, height= 310, background='white')
            painel_log_in.place(x = 500, y = 10)

            lbl_Log_In = Label(painel_log_in, text = 'Made by', fg='black', font = ('Arial', 20), background='white')
            lbl_Log_In.place(x = 80, y = 0)

            lbl_info1 = Label(painel_log_in, text = 'Tiago Ribeiro\nnº 40210462\n\nNuno Mendonça\nnº 40210260\n\nJosé Pedro\nnº 40210276', fg='black', font = ('Arial', 18), background='white')
            lbl_info1.place(x = 40, y = 50)


        painel_inicial = PanedWindow(start_window, width = 770, height= 330, background='#b9b9b9')
        painel_inicial.place(x = 40, y = 33)

        #Imagens
        #img = PhotoImage(file = 'Bem-vindo.png')
        img = PhotoImage(file = 'Welcome.png')
        img1 = PhotoImage(file = 'Cursos-Online.png')

        #Canvas
        ctn_canvas = Canvas(painel_inicial, width = 770, height = 330, background='#b9b9b9')
        ctn_canvas.place(x = 0, y = 0)
        ctn_canvas.create_image(380,170, image = img)

        #Botões
        btn_Log_In = Button(painel_inicial, text = 'Log In', font = ('Arial', 11), fg = 'white', relief='groove', background = 'black', width=10, height=1, command=Log_In)
        btn_Log_In.place (x = 215,y = 160)

        btn_Sign_Up = Button(painel_inicial, text = 'Sign Up', font = ('Arial', 11), fg = 'white', relief='groove', background = 'black', width=10, height=1, command=Sign_Up)
        btn_Sign_Up.place (x = 445,y = 160)

        btn_Exit = Button(painel_inicial, text = 'Exit', font = ('Arial', 9), fg = 'black', relief='groove', background = 'white', width=10, height=1, command = start_window.destroy)
        btn_Exit.place (x = 338,y = 232)

        #Botão de informação adicional (escondido)
        btn_info = Button(painel_inicial, fg = 'black', background = '#b9b9b9', relief = 'flat', bitmap = 'info', width=20, height=20, command = info)
        btn_info.place (x = 205,y = 246)

        start_window.mainloop()  #event listening loop by calling the mainloop()


    start()

start_window()