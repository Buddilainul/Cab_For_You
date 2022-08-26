from tkinter import *
from tkinter import messagebox


# --------------Login screen-----------#

def Login_Screen():
    root = Tk()
    root.geometry("925x500+300+200")
    root.title("Login")
    root.config(bg='white')
    root.resizable(False, False)

    def login():
        username = user.get()
        password = code.get()
        values = v.get()
        if values == '1' and username == 'admin' and password == '1234':
            root.destroy()
            System_Manger_Screen()

        elif values == '2' and username == 'admin' and password == '1234':
            root.destroy()
            Driver_Screen()
        elif values == '3' and username == 'admin' and password == '1234':
            root.destroy()
            Welcome_Screen()
        else:
            messagebox.showerror('error', 'please try again')

    img = PhotoImage(file='./asset/login.png')
    Label(root, image=img, bg='white').place(x=50, y=50)

    ########################################

    frame1 = Frame(root, width=350, height=100, bg='white')
    frame1.place(x=480, y=50)

    v = StringVar(frame1, "0")

    Radiobutton(frame1, text="System manager", variable=v, value=1, bg='white',
                font=('Microsoft YaHei UI Light', 13, 'bold')).pack(side=LEFT, ipady=3)
    Radiobutton(frame1, text="Cab driver", variable=v, value=2, bg='white',
                font=('Microsoft YaHei UI Light', 13, 'bold')).pack(side=LEFT, ipady=3)
    Radiobutton(frame1, text="User", variable=v, value=3, bg='white',
                font=('Microsoft YaHei UI Light', 13, 'bold')).pack(side=LEFT, ipady=3)
    Radiobutton.place(frame1, x=480, y=10)

    frame = Frame(root, width=350, height=350, bg='white')
    frame.place(x=480, y=80)

    heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ########################################

    def on_enter(e):
        name = user.get()
        if name == 'Username':
            user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ########################################
    def on_enter(e):
        name = code.get()
        if name == 'Password':
            code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ########################################

    Button(frame, width=39, pady=7, text="Login", bg='#57a1f8', fg='white', border=0, command=login).place(x=35, y=204)
    label = Label(frame, text="Don't have an account?", fg='black', bg="white", font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    def go_to_signup():
        root.destroy()
        SignUp_screen()

    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                     command=go_to_signup)
    sign_up.place(x=215, y=270)

    root.mainloop()


# --------------Sign-UP screen ----------#

def SignUp_screen():
    screen = Tk()
    screen.geometry("925x500+300+200")
    screen.title("Sign-Up")
    screen.config(bg='white')
    screen.resizable(False, False)

    img = PhotoImage(file='./asset/signup.png')
    Label(screen, image=img, bg='white').place(x=50, y=90)

    def signup():
        values = v.get()
        username = user.get()
        password = code.get()
        conform_password = conform_code.get()

        if values != "0" and password != "" and password == conform_password and username != "":
            messagebox.showinfo('SignUp', 'Successfully signup')
        else:
            messagebox.showerror('error', 'please try again')

    def Back_to_login():
        screen.destroy()
        Login_Screen()

    ########################################

    frame1 = Frame(screen, width=350, height=100, bg='white')
    frame1.place(x=480, y=50)

    v = StringVar(frame1, "0")

    Radiobutton(frame1, text="System manager", variable=v, value=1, bg='white',
                font=('Microsoft YaHei UI Light', 13, 'bold')).pack(side=LEFT, ipady=3)
    Radiobutton(frame1, text="Cab driver", variable=v, value=2, bg='white',
                font=('Microsoft YaHei UI Light', 13, 'bold')).pack(side=LEFT, ipady=3)
    Radiobutton(frame1, text="User", variable=v, value=3, bg='white',
                font=('Microsoft YaHei UI Light', 13, 'bold')).pack(side=LEFT, ipady=3)
    Radiobutton.place(frame1, x=480, y=10)

    frame = Frame(screen, width=350, height=390, bg='white')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ########################################

    def on_enter(e):
        name = user.get()
        if name == 'Username':
            user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ########################################

    def on_enter(e):
        name = code.get()
        if name == 'Password':
            code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ########################################

    def on_enter(e):
        name = conform_code.get()
        if name == 'Conform Password':
            conform_code.delete(0, 'end')

    def on_leave(e):
        name = conform_code.get()
        if name == '':
            conform_code.insert(0, 'Conform Password')

    conform_code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    conform_code.place(x=30, y=220)
    conform_code.insert(0, 'Conform Password')
    conform_code.bind('<FocusIn>', on_enter)
    conform_code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    ########################################

    Button(frame, width=39, pady=7, text="Sign-Up", bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,
                                                                                                              y=304)
    label = Label(frame, text="I have an account", fg='black', bg="white", font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=370)

    sign_up = Button(frame, width=6, text='Login', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                     command=Back_to_login)
    sign_up.place(x=190, y=370)

    screen.mainloop()


# --------------Welcome screen user-----------#

def Welcome_Screen():
    screen = Tk()
    screen.geometry("925x500+300+200")
    screen.title("Cab For You")
    screen.config(bg='light green')

    def Back_to_login():
        screen.destroy()
        Login_Screen()

    def Bookcab():
        values = v.get()
        if values != "0":
            messagebox.showinfo('Successful', 'Your Cab on the way ')
        else:
            messagebox.showerror('error', 'Select an cab')

    Button(screen, width=10, pady=7, text="Log-Out", bg='#57a1f8', fg='black', border=0, command=Back_to_login) \
        .place(x=840, y=5)

    heading = Label(screen, text='Cab For You', fg='red', bg='light green',
                    font=('Microsoft YaHei UI Light', 25, 'bold'))
    heading.place(x=400, y=5)

    selecttitle = Label(screen, text='select an cab', fg='black', bg='light green',
                        font=('Microsoft YaHei UI Light', 23, 'bold'))
    selecttitle.place(x=100, y=50)

    frame = Frame(screen, width=905, height=390, bg='light green')
    frame.place(x=10, y=100)

    def inside():
        frame1 = Frame(screen, width=500, height=200, bg='light green')
        frame1.place(x=300, y=200)
        values = v.get()
        if values == "1":
            Label(frame1, text='maximum number of passengers is 3 to 4', fg='black', bg='light green',
                  font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=0, y=0)
            Label(frame1, text='AC/ or AC', fg='black', bg='light green',
                  font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=0, y=50)
        elif values == "2":
            Label(frame1, text='maximum number of passengers is 6 to 8', fg='black', bg='light green',
                  font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=0, y=0)
            Label(frame1, text='AC/ or AC', fg='black', bg='light green',
                  font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=0, y=50)
        elif values == "3":
            Label(frame1, text='maximum number of passengers is 3', fg='black', bg='light green',
                  font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=0, y=0)
        elif values == "4":
            Label(frame1, text='Size – 7 ft to 12 ft', fg='black', bg='light green',
                  font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=0, y=0)
        elif values == "5":
            Label(frame1, text='Max load - 2500kg to 3500kg', fg='black', bg='light green',
                  font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=0, y=0)

    v = StringVar(frame, "0")

    Radiobutton(frame, text="Car            ", variable=v, value=1, bg='light green', command=inside,
                font=('Microsoft YaHei UI Light', 20, 'bold')).pack(side=TOP, ipady=5)
    Radiobutton(frame, text="Van           ", variable=v, value=2, bg='light green', command=inside,
                font=('Microsoft YaHei UI Light', 20, 'bold')).pack(side=TOP, ipady=5)
    Radiobutton(frame, text="3 Wheelers", variable=v, value=3, bg='light green', command=inside,
                font=('Microsoft YaHei UI Light', 20, 'bold')).pack(side=TOP, ipady=5)
    Radiobutton(frame, text="Trucks        ", variable=v, value=4, bg='light green', command=inside,
                font=('Microsoft YaHei UI Light', 20, 'bold')).pack(side=TOP, ipady=5)
    Radiobutton(frame, text="Lorry         ", variable=v, value=5, bg='light green', command=inside,
                font=('Microsoft YaHei UI Light', 20, 'bold')).pack(side=TOP, ipady=5)
    Radiobutton.place(frame, x=10, y=110)

    Button(screen, width=39, pady=7, text="Book Cab", bg='#57a1f8', fg='white', border=0, command=Bookcab).place(x=600,
                                                                                                                 y=400)

    screen.mainloop()


# --------------driver dashboard  screen-----------#

def Driver_Screen():
    screen = Tk()
    screen.geometry("925x500+300+200")
    screen.title("Cab For You")
    screen.config(bg='white')

    def Back_to_login():
        screen.destroy()
        Login_Screen()

    heading = Label(screen, text='Driver Dashboard', fg='red', bg='white',
                    font=('Microsoft YaHei UI Light', 25, 'bold'))
    heading.place(x=400, y=5)

    selecttitle = Label(screen, text='Select an available hire', fg='black', bg='white',
                        font=('Microsoft YaHei UI Light', 18, 'bold'))
    selecttitle.place(x=100, y=80)

    Button(screen, width=10, pady=7, text="Log-Out", bg='#57a1f8', fg='black', border=0, command=Back_to_login) \
        .place(x=840, y=5)

    screen.mainloop()


# --------------system manager dashboard  screen-----------#

def System_Manger_Screen():
    screen = Tk()
    screen.geometry("925x500+300+200")
    screen.title("Cab For You")
    screen.config(bg='white')

    def Back_to_login():
        screen.destroy()
        Login_Screen()

    heading = Label(screen, text='System Manager', fg='red', bg='white',
                    font=('Microsoft YaHei UI Light', 25, 'bold'))
    heading.place(x=400, y=5)

    selecttitle = Label(screen, text='add new Vehicle', fg='black', bg='white',
                        font=('Microsoft YaHei UI Light', 18, 'bold'))
    selecttitle.place(x=100, y=80)

    Button(screen, width=10, pady=7, text="Log-Out", bg='#57a1f8', fg='black', border=0, command=Back_to_login) \
        .place(x=840, y=5)

    screen.mainloop()


# --------------starting program-----------#

Login_Screen()
