import requests
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

window = Tk()
window.geometry("400x350")
window.title("Exchange Rate Converter")
window.resizable(False, False)
window["background"] = "purple"

response = requests.get("https://v6.exchangerate-api.com/v6/21d57e3e0d14d58eee61f22c/latest/USD")
data = response.json()
exc_rate = data["conversion_rates"]


def info():
    for rate in exc_rate:
        combox = combobox_choice
        if combox == getattr(exc_rate, rate):
            exc_rate[rate] * num_1_entry

#  The clearing function.
def clear():
    num_1_entry.delete(0, END)
    num_2_lb.config(text="")


#  The exiting function.
def exit_window():
    msg = messagebox.askquestion("You Sure?", "You want to leave the program?")
    if msg == "yes":
        window.destroy()
    else:
        print("You Returned")


heading = Label(window, text="/ Enter Your Amount /", fg="orange", bg="purple")
heading.place(x=125, y=10)

num_1_lb = Label(window, text="Enter Amount : ", bg="purple", fg="orange")
num_1_lb.place(x=50, y=80)
num_1_entry = Entry(window, bg="orange")
num_1_entry.place(x=180, y=80)

combobox_choice = Combobox(window, values=("exac_rate"))

num_2_lb = Label(window, text="", bg="purple", fg="orange")
num_2_lb.place(x=150, y=130)


clear_btn = Button(window, text="/ Clear /", bg="purple", fg="orange", width=15, command=clear)
clear_btn.place(x=130, y=230)
change_btn = Button(window, text="/ Change /", bg="purple", fg="orange", width=15, command=info)
change_btn.place(x=130, y=195)
exit_button = Button(window, text="/ Exit /", bg="purple", fg="orange", width=20, command=exit_window)
exit_button.place(x=110, y=290)

window.mainloop()
