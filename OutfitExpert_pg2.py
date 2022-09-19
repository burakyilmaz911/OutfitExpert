import tkinter as tk
import tkinter.ttk

#Initialize buttons
class BtnInit:
    def __init__(self, frm, text, bg, fg, placey):
        self.btn = tk.Button(master=frm, text=text, background=bg, foreground=fg, cursor="hand2",command=lambda: btn_clicked(self.btn, placey))
        self.btn.place(relx=0.5, rely=placey, anchor=tk.CENTER)

#Replace button with textbox input
class TxtBoxInit:
    def __init__(self, fg, bg, w, placey):
        self.txtbox = tk.Entry(foreground=fg, background=bg, width=w)
        self.txtbox.place(relx = 0.5, rely=placey, anchor=tk.CENTER)
        btn_validate = tk.Button(text="Enter", command=lambda: validate_txt(self.txtbox))
        btn_validate.place(relx=0.5, rely=placey+0.05, anchor=tk.CENTER)

#Event called for when button is clicked and replaced with a text box for user
def btn_clicked(button:tk.Button, placey):
    button.destroy() 
    txt_box = TxtBoxInit("black", "white", 25, placey)

def validate_txt(txt_box:tk.Entry):
    user_input = txt_box.get()
    user_input = user_input.lower()
    if user_input not in all_colors:
        print("Color not in color wheel, please try again")
        txt_box.delete('0', tk.END)
    else:
        print(user_input)

all_colors = ["yellow", "yellow-orange", "orange", "red-orange", "red", "red-violet", "violet", "blue-violet", "blue", "blue-green", "green", "yellow-green"]

#Initialize root window
root = tk.Tk()
root.geometry("500x500")

#Initialize parent frame
frm = tk.Frame(background="black")
frm.pack(fill=tk.BOTH, expand=True)

#Create the list of buttons required for this page and initialize
btn_names = ["shirt", "pants", "shoes"]
btns = []

for x,name in enumerate(btn_names):
    btn = BtnInit(frm, name, "black", "white", 0.4 + x/10)
    btns.append(btn)

root.mainloop()

#Here's how were gonna do the color selection:
#Using the color wheel, make 4 lists; 1 list of all the colors, 1 list for half the wheel and the other for the remaining and last list is white, grey, and black
#Current Issues: user input not working as intended
