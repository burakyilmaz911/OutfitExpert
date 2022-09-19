import tkinter as tk
import tkinter.ttk

def btn_start_clicked(event):
    root.destroy()
    import OutfitExpert_pg2

root = tk.Tk()
root.geometry("500x500")

frm = tk.Frame(master=root, background="black")
frm.pack(fill=tk.BOTH, expand=True)

lbl = tk.Label(
    master=frm,
    text="Hello World",
    background="black",
    foreground="white"
)
lbl.pack()

btn_start = tk.Button(master=frm, text="Start")
btn_start.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
btn_start.bind("<Button-1>", btn_start_clicked)

root.mainloop()