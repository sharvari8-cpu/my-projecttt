import tkinter as tk
from time import strftime

root = tk.Tk()

root.title("digital clock")
root.configure(bg="pink")

heading=tk.Label(root,text="Clock It Girl💋",
font=('calibri',28,'bold'),bg="pink", foreground="white")
heading.pack(pady=65)

def time():
 string = strftime('%H:%M:%S %p \n%d/%m/%y')
 label.config(text=string)
 label.after(1000,time)

label = tk.Label(root, font=('calibri', 80, 'bold'), background='pink', foreground='white')
label.pack(anchor='center')

extra_text= tk.Label(root,text="Work Until It Shows🌷",font=('calibri',28,'bold'),bg="pink",fg='white')
extra_text.pack(pady=65)

time()
root.mainloop()


