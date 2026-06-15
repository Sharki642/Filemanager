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
    textfeld_ger = tk.Text(window, height=5, width=30)
    textfeld_ger.pack()

    def erstelle_date_ger():
        eingabe_name = textfeld_ger.get("1.0", tk.END).strip()
        if not eingabe_name:
            tk.Label(window, text="Bitte einen Namen eingeben!", fg="red").pack()
            return
        shutil.copy("vorlage_deutsch.docx", f"{eingabe_name}.docx")
        tk.Label(window, text=f"Datei '{eingabe_name}.docx' erstellt!", fg="green").pack()

    tk.Button(window, text="Datei erstellen", command=erstelle_date_ger).pack()

def create_protokoll_en():
    print("Creating English Protokoll...")
    window = tk.Toplevel(root)
    window.title("English Protokoll")
    window.minsize(300, 200)
    tk.Label(window, text="Lets create the english protokoll").pack()
    textfeld_eng = tk.Text(window, height=5, width=30)
    textfeld_eng.pack()

    def erstelle_date_eng():
        eingabe_name = textfeld_eng.get("1.0", tk.END).strip()
        if not eingabe_name:
            tk.Label(window, text="Please enter a name!", fg="red").pack()
            return
        shutil.copy("vorlage_english.docx", f"{eingabe_name}.docx")
        tk.Label(window, text=f"File '{eingabe_name}.docx' created!", fg="green").pack()

    tk.Button(window, text="Create File", command=erstelle_date_eng).pack()

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

Protokoll_en = tk.Button(root, text="Create English Protokoll", command=create_protokoll_en)
Protokoll_en.pack()



root.mainloop()