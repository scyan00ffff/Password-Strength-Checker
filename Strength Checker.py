import random
import string
import tkinter as tk 

LARGEFONT = ("Veranda", 20, "bold")
MEDIUMFONT = ("Veranda", 15, "underline")
SMALLFONT = ("Veranda", 10, "bold")

class PasswordApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("600x400")

        main_container = tk.Frame(self)
        main_container.pack(side="top", fill="both", expand=True)

        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Generator, Tester):
            frame = F(main_container, self)

            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Title = tk.Label(self, text="Password4You", font=LARGEFONT)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        Title.grid(row=0, column=1, padx=10, pady=10)

        GeneratorButton = tk.Button(self, text="Password Generator", command = lambda : controller.show_frame(Generator))
        GeneratorButton.grid(row= 1, column=0, padx=10, pady=10)

        TesterButton = tk.Button(self, text="Password Tester", command = lambda : controller.show_frame(Tester))
        TesterButton.grid(row= 1, column=2, padx=10, pady=10)

        info_label = tk.Label(self,text="This is a small and simple password \n generator and strength tester application\n created as a side project for a personal portfolio.\n Find my github at: https://github.com/scyan00ffff")
        info_label.grid(row=2, column=1, padx=10, pady=10)


class Generator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global checkButton1
        global checkButton2
        global checkButton3

        checkButton1 = tk.IntVar()
        checkButton2 = tk.IntVar()
        checkButton3 = tk.IntVar()

        global password_length
        password_length = tk.StringVar()
        
        Title = tk.Label(self, text="Password Generator", font=LARGEFONT)

        global SpecialCharactersCheck
        global UppercaseCharactersCheck
        global NumbersCheck

        SpecialCharactersCheck = tk.Checkbutton(self, 
                                                text="Special Characters",
                                                variable=checkButton1,
                                                onvalue=1,
                                                offvalue=0,
                                                height=2,
                                                width=20,
                                                )
        UppercaseCharactersCheck = tk.Checkbutton(self, 
                                        text="UpperCase Characters",
                                        variable=checkButton2,
                                        onvalue=1,
                                        offvalue=0,
                                        height=2,
                                        width=20,
                                        )
        NumbersCheck = tk.Checkbutton(self, 
                                        text="Numbers",
                                        variable=checkButton3,
                                        onvalue=1,
                                        offvalue=0,
                                        height=2,
                                        width=20,
                                        )
        
        password_length_label = tk.Label(self, text="Length:", font=MEDIUMFONT)
        password_length_entry = tk.Entry(self, textvariable=password_length)
        global password_length_error
        password_length_error = tk.Label(self, text="")

        password_submit_button = tk.Button(self, text="Submit", command=submit)

        HomeButton = tk.Button(self, text="Home", command= lambda : controller.show_frame(Home))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        Title.grid(row=0, column=1, padx=10, pady=10)
        HomeButton.grid(row=5, column=2, padx=10, pady=10)

        SpecialCharactersCheck.grid(row=1, column=0, padx=10, pady=5, sticky="W")
        UppercaseCharactersCheck.grid(row=2, column=0, padx=10, pady=5, sticky="W")
        NumbersCheck.grid(row=3, column=0, padx=10, pady=5, sticky="W")

        password_length_label.grid(row=4, column=0, padx= 10, pady=10)
        password_length_entry.grid(row=5, column=0, padx=10, pady=10)
        password_submit_button.grid(row=6, column = 0, padx=10, pady=10)
        password_length_error.grid(row=7, column=0, padx=10, pady=10)
        
        generated_password_label = tk.Label(self, text="Generated Password", font=MEDIUMFONT)

        generated_password_label.grid(row=2, column=1, padx=10, pady=10)

        generate_button = tk.Button(self, text="Generate", command=password_generator)
        generate_button.grid(row=3, column=1, padx=10, pady=10)
        
        global generated_password
        generated_password = tk.Label(self, text="")
        generated_password.grid(row=4, column=1, padx=10, pady=10)

def submit():
    global length
    if password_length.get() != "":
        length = password_length.get()
        password_length_error.config(text="")
    else:
        password_length_error.config(text="Enter a length!", fg="red")


def password_generator():
    
    character_list=string.ascii_lowercase

    global GeneratedPassword
    GeneratedPassword= tk.StringVar()

    password = []

    if checkButton1.get() == 1: 
        character_list += string.punctuation
    if checkButton2.get() == 1:
        character_list += string.ascii_uppercase
    if checkButton3.get() == 1:
        character_list += string.digits
    
    length_of_password = length

    for desired_length in range (int(length_of_password)):
        randomchar = random.choice(character_list)
        password.append(randomchar)
    print(str(password))

    generated_password.config(text= password, bg="green", borderwidth=2, relief="solid")


class Tester(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Title = tk.Label(self, text="Password Tester", font=LARGEFONT)

        HomeButton = tk.Button(self, text="Home", command= lambda : controller.show_frame(Home))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        
        Title.grid(row=0, column=1, padx=10, pady=10)
        HomeButton.grid(row=3, column=2, padx=10, pady=10)

        enter_password_label = tk.Label(self, text="Enter Password:", font=MEDIUMFONT)
        enter_password_label.grid(row=1, column=1, padx=10, pady=10)

        global user_password
        user_password = tk.StringVar()

        user_password_entry = tk.Entry(self, textvariable=user_password)
        user_password_entry.grid(row=2, column=1, padx=10, pady=10)

        global strength_label
        strength_label = tk.Label(self, text="")
        strength_label.grid(row=3, column=1, padx=10, pady=10)


        password_submit_button = tk.Button(self, text="Submit", command=strength_checker)
        password_submit_button.grid(row=6, column=1, padx=10, pady=10)

        breached_label = tk.Label(self, text="Number of times found in databreaches: ", fg="red", font=SMALLFONT)
        breached_label.grid(row=4, column=1, padx=10, pady=10)

        global breached_amount
        breached_amount = tk.Label(self, text="")
        breached_amount.grid(row=5, column=1, padx=10, pady=10)


def strength_checker():

    numbers = ["1","2","3","4","5","6","7","8","9"]
    special_characters = ["!","@","$","£","%","^","&","*","(",")","_","-","+","_","[","]","{","}","<",">","/","?",";",":"]
    characters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

    user_input = user_password.get()

    score = 0

    for x in range(0, len(special_characters)):
        if special_characters[x] in user_input:
            score += 1

    for y in range(0, len(numbers)):
        if numbers[y] in user_input:
            score += 1

    for g in range (0, len(user_input)):
        if user_input[g].isupper():
            score +=1

    passwords_file = open("rockyou.txt", "r", encoding="utf-8",errors="replace")
    lines = passwords_file.readlines()

    counter = 0

    for line in lines:
        if user_input in line:
            counter +=1
    breached_amount.config(text=str(counter), fg="red", font=SMALLFONT)
    passwords_file.close()

    if score == 0 and counter >=100: 
        strength_label.config(text="Very Weak Password!", fg="red", font=SMALLFONT)
    elif score >= 1 and score < 3 and counter <=99:
        strength_label.config(text="Weak Password!", fg="orange",font=SMALLFONT)
    elif score >= 3 and score < 5 and counter <=50:
        strength_label.config(text="Good Password!", fg="green2",font=SMALLFONT)
    elif score >= 5 and score < 7 and counter <=25:
        strength_label.config(text="Strong Password!", fg="green4",font=SMALLFONT)
    elif score >= 7 and counter == 0:
        strength_label.config(text="Very Strong Password!", fg="deep sky blue",font=SMALLFONT)


app = PasswordApp()
app.mainloop()


