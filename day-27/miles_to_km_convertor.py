from tkinter import *

window = Tk()
window.title("Miles to Km Convertor")

window.minsize(width=300, height=200)

def convert_miles_to_km():
    miles = miles_input.get();
    km =  int(miles) * 1.6
    km_value.config(text=km)

my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

# Input Miles
miles_input = Entry()
miles_input.grid(column=1, row=0)

# Mile label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# KM label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# KM label
km_value = Label(text="0")
km_value.grid(column=1, row=1)

# Button for calculate

calculate = Button(text="Calculate", command=convert_miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()