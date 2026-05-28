from tkinter import *



window = Tk()

window.title("My GUI project")

window.minsize(width=500, height=300)

window.config(padx=20, pady=20)

def button_clicked():
    # print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Label
my_label = Label(text="I am a label", font=("Arial", 24))
# my_label.pack(side='left')
# my_label.pack()

my_label.grid(column=0, row=0)

# my_label['text'] = "New Text"
# my_label.config(text="New Text")


# Button
button = Button(text='Click  me', command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button = Button(text='New Button', command=button_clicked)
# button.pack()
button.grid(column=2, row=0)

# Input or Entry
input = Entry()
input.grid(column=3, row=2)
print(input.get())


window.mainloop()