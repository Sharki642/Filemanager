#importing the tkinter module
import tkinter as tk

print("hello world!")
#starting the window
root = tk.Tk()
#title
root.title("FileManager")
root.minsize(400, 400)
#inside

root.configure(bg="White")
tk.Label(root, text="Welcome to FileManager").pack()
image = tk.PhotoImage(file="image2.png")
tk.Label(root, image=image).pack()


Protokoll_de = tk.Button(root, text="Create German Protokoll")
Protokoll_de.pack()



root.mainloop()