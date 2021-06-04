import requests
from tkinter import Tk, Message, Button, messagebox


root = Tk()
root.geometry("200x200")
root.resizable(False, False)
root["background"] = "red"


def joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        return data["value"]
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Your Offline", "Check Your Connection")


def get_new_joke():
    jk.configure(text=joke())


jk = Message(root, bg="red", text=joke())
jk.pack()

new_jk = Button(root, bg="red", text="New Joke", command=get_new_joke)
new_jk.pack(side="bottom")

root.mainloop()
