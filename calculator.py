import customtkinter as ctk


app = ctk.CTk()
app.title('calculator')
app.geometry('200x250')

text_var = ctk.StringVar(value='')
text = ''

def click(key): # creating a function for clicking interface buttons and storing
    global text # their value as a string in the variable called text
    text += str(key)
    text_var.set(text)
    # print(str(text))
    
def calculate():
    global text
    
    if len(text) > 0:
        text = str(eval(text))
        text_var.set(text)
        # print(text)
        
def backspace():
    global text
    text = text[:-1]
    text_var.set(text)
    # print(str(text))
    
Entry = ctk.CTkEntry(app, textvariable=text_var, height=50, width=200, font=('', 20), corner_radius=0, border_width=0)
Entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

button1 = ctk.CTkButton(app, text='1', command=lambda: click(1), width=50, height=50, corner_radius=0)
button1.grid(row=3, column=0, sticky='nsew')

button2 = ctk.CTkButton(app, text='2', command=lambda: click(2), width=50, height=50, corner_radius=0)
button2.grid(row=3, column=1, sticky='nsew')

button3 = ctk.CTkButton(app, text='3', command=lambda: click(3), width=50, height=50, corner_radius=0)
button3.grid(row=3, column=2, sticky='nsew')

button4 = ctk.CTkButton(app, text='4', command=lambda: click(4), width=50, height=50, corner_radius=0)
button4.grid(row=2, column=0, sticky='nsew')

button5 = ctk.CTkButton(app, text='5', command=lambda: click(5), width=50, height=50, corner_radius=0)
button5.grid(row=2, column=1, sticky='nsew')

button6 = ctk.CTkButton(app, text='6', command=lambda: click(6), width=50, height=50, corner_radius=0)
button6.grid(row=2, column=2, sticky='nsew')

button7 = ctk.CTkButton(app, text='7', command=lambda: click(7), width=50, height=50, corner_radius=0)
button7.grid(row=1, column=0, sticky='nsew')

button8 = ctk.CTkButton(app, text='8', command=lambda: click(8), width=50, height=50, corner_radius=0)
button8.grid(row=1, column=1, sticky='nsew')

button9 = ctk.CTkButton(app, text='9', command=lambda: click(9), width=50, height=50, corner_radius=0)
button9.grid(row=1, column=2, sticky='nsew')

calc_btn = ctk.CTkButton(app, text='=', command=lambda: calculate(), width=100, height=50, fg_color='#29417F', corner_radius=0)
calc_btn.grid(row=4, column=0, sticky='nsew', columnspan=2)

backspacebtn = ctk.CTkButton(app, text='⌫', command=lambda: backspace(), width=50, height=50, fg_color='#29417F', corner_radius=0)
backspacebtn.grid(row=4, column=2, sticky='nsew')

plus_button = ctk.CTkButton(app, text='+', command=lambda: click('+'), width=50, height=50, fg_color='#296C7F', corner_radius=0)
plus_button.grid(row=4, column=3, sticky='nsew')

minus_button = ctk.CTkButton(app, text='-', command=lambda: click('-'), width=50, height=50, fg_color='#296C7F', corner_radius=0)
minus_button.grid(row=3, column=3, sticky='nsew')

times_button = ctk.CTkButton(app, text='*', command=lambda: click('*'), width=50, height=50, fg_color='#296C7F', corner_radius=0)
times_button.grid(row=2, column=3, sticky='nsew')

division_button = ctk.CTkButton(app, text='/', command=lambda: click('/'), width=50, height=50, fg_color='#296C7F', corner_radius=0)
division_button.grid(row=1, column=3, sticky='nsew')

app.mainloop()