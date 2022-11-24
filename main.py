from tkinter import *


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=350, height=200)
window.config(padx=50, pady=50)

def calculate():

    miles_to_km = round(float(entry.get()) * 1.609, 2)
    label3.config(text=miles_to_km)

# Labels
label = Label(text='is equal to')
label.grid(column=0, row=1)

label1 = Label(text='Miles')
label1.grid(column=2, row=0)

label2 = Label(text='Km')
label2.grid(column=2, row=1)

label3 = Label(text='')
label3.grid(column=1, row=1)

# Entry

entry = Entry(width=10)
entry.grid(column=1, row=0)


# Button
button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

window.mainloop()
