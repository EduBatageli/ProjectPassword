import mysql.connector
from mysql.connector import errorcode
from tkinter import * 
from tkinter import messagebox

conexao = mysql.connector.connect(
    host='127.0.0.1', # your localhost
    user='root', # user 
    password='', # default password is null
    database='senhas' # selecting the database
)
cursor = conexao.cursor()

def testingConnection():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='senhas')
        messagebox.showinfo(title='database', message='connection done')
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
         messagebox.showinfo(title='database', message='database doesnt exist')
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            messagebox.showinfo(title='database', message='user or password is wrong')
        else:
            print(error)

def creatingPassword():
        import random

        Senha = []
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        letter_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        letter_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        caracters = ['@','#','$','%','&']

        # 1 letter upper
        for x in range(1):
            senha = random.choice(letter_upper) 
            Senha.append(senha)
        # 2 letters lower
        for x in range(2):
            senha = random.choice(letter_lower) 
            Senha.append(senha)
        # 1 especial caracter
        for x in range(1):
            senha = random.choice(caracters) 
            Senha.append(senha)
        # 3 numbers
        for x in range(4):
            senha = random.choice(numbers) 
            Senha.append(senha)

        senha_gerada = "".join(Senha)
        return senha_gerada

def addPassword():
    window_add = Tk()
    window_add.geometry('600x300')
    window_add.configure(background = "black")
    window_add.resizable(width=False, height=False)


    user_label = Label(window_add, text='USUARIO:', font=('Century Gothic', 20), bg='black', fg='white')
    user_label.place(y=100, x=50)
    user_entry = Entry(window_add, width=30)
    user_entry.place(y=115, x=270)

    def addPasswordCommand():
        
        user = user_entry.get()

        if (user == ''):
            messagebox.showerror(title='error', message='you must complete all informations')
        else:
            comando = f'INSERT INTO MinhaSenhas(USUARIO, SENHA) VALUES ("{user}","{creatingPassword()}-{"Ncc"}")'
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo(title="adding password", message=f'COMPLETE')
            window_add.after(1000, window_add.destroy)

    buttton_addPassword_command = Button(window_add, text='execute', command=addPasswordCommand)
    buttton_addPassword_command.place(y = 150, x= 300)

def showPassFiltered():
    window_show = Tk()
    window_show.geometry('600x300')
    window_show.configure(background = "black")
    window_show.resizable(width=False, height=False)


    user_label = Label(window_show, text='USER:', font=('Century Gothic', 20), bg='black', fg='white')
    user_label.place(y=100, x=50)
    user_entry = Entry(window_show, width=30)
    user_entry.place(y=115, x=270)

    def showPass():
        if (user_entry.get() == ''):
            messagebox.showerror(title='error', message='you must complete all informations')
        else:
            comando = f"select SENHA from MinhaSenhas WHERE USUARIO = '{user_entry.get()}'"
            cursor.execute(comando)
            result = cursor.fetchall()
            messagebox.showinfo(message=result)
            window_show.after(1000, window_show.destroy)

    buttton_addPassword_command = Button(window_show, text='execute', command=showPass)
    buttton_addPassword_command.place(y = 150, x= 300)

def changePassword():
    window_change = Tk()
    window_change.geometry('600x300')
    window_change.configure(background = "black")
    window_change.resizable(width=False, height=False)


    user_label = Label(window_change, text='USUARIO:', font=('Century Gothic', 20), bg='black', fg='white')
    user_label.place(y=100, x=50)
    user_entry = Entry(window_change, width=30)
    user_entry.place(y=115, x=270)

    def changePasswordCommand():
        user = user_entry.get()

        if (user == ''):
            messagebox.showerror(title='error', message='you must complete all informations')
        else:
            comando = f'UPDATE MinhaSenhas SET SENHA = "{creatingPassword()}-{"Ncc"}" WHERE USUARIO = "{user}"'
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo(title="change password", message=f'COMPLETE')
            window_change.after(1000, window_change.destroy)

    buttton_addPassword_command = Button(window_change, text='execute', command=changePasswordCommand)
    buttton_addPassword_command.place(y = 150, x= 300)

def deletePassword():
    window_delete = Tk()
    window_delete.geometry('600x300')
    window_delete.configure(background = "black")
    window_delete.resizable(width=False, height=False)


    user_label = Label(window_delete, text='USUARIO:', font=('Century Gothic', 20), bg='black', fg='white')
    user_label.place(y=100, x=50)
    user_entry = Entry(window_delete, width=30)
    user_entry.place(y=115, x=270)

    def deletePasswordCommand():
        if (user_entry.get() == ''):
            messagebox.showerror(title='error', message='you must complete all informations')
        else:    
            comando = f'DELETE FROM MinhaSenhas WHERE USUARIO = "{user_entry.get()}"'
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo(title="change password", message=f'COMPLETE')
            window_delete.after(1000, window_delete.destroy)

    buttton_addPassword_command = Button(window_delete, text='execute', command=deletePasswordCommand)
    buttton_addPassword_command.place(y = 150, x= 300)

def OptionsPage():
    # removing buttons
    button_test_connection.place(y=5000, x=200)
    button_options.place(y=500, x=200)

    # adding buttons
    
    button_adding_password = Button(text='ADD PASSWORD', width=30, command=addPassword)
    button_adding_password.place(y=50, x=200)

    button_show = Button(text="SHOW PASSWORD", width=30, command=showPassFiltered)
    button_show.place(y = 100, x = 200)

    button_change = Button(text="CHANGE PASSWORD", width=30, command=changePassword)
    button_change.place(y = 150, x = 200)

    button_delete = Button(text="DELETE PASSWORD", width=30, command=deletePassword)
    button_delete.place(y = 200, x = 200)

# main window
window = Tk()
window.title('Program')

# window size
window.geometry('600x300')
window.configure(background = "black")
window.resizable(width=False, height=False)

button_test_connection = Button(text='TEST CONNECTION', width=30, command=testingConnection)
button_test_connection.place(y=100, x=200)

button_options = Button(text='OPERATIONS', width=30, command=OptionsPage)
button_options.place(y = 200, x = 200)

window.mainloop()
          
cursor.close()          
conexao.close()