#importing the tkinter module
import tkinter as tk
import shutil

print("hello world!")
#starting the window
root = tk.Tk()

def create_protokoll_de():
    print("Creating German Protokoll...")
    window = tk.Toplevel(root)
    window.title("German Protokoll")
    window.minsize(300, 200)
    tk.Label(window, text="Lets dreat the german protokoll").pack()
    textfeld = tk.Text(window, height=5, width=30)
    textfeld.pack()

    def erstelle_datei():
        eingabe_name = textfeld.get("1.0", tk.END).strip()
        if not eingabe_name:
            tk.Label(window, text="Bitte einen Namen eingeben!", fg="red").pack()
            return
        shutil.copy("vorlage_deutsch.docx", f"{eingabe_name}.docx")
        tk.Label(window, text=f"Datei '{eingabe_name}.docx' erstellt!", fg="green").pack()

    tk.Button(window, text="Datei erstellen", command=erstelle_datei).pack()


#title
root.title("FileManager")
root.minsize(400, 400)
#inside

root.configure(bg="White")
tk.Label(root, text="Welcome to FileManager").pack()
image = tk.PhotoImage(file="image2.png")
tk.Label(root, image=image).pack()


Protokoll_de = tk.Button(root, text="Create German Protokoll", command=create_protokoll_de)
Protokoll_de.pack()



root.mainloop()