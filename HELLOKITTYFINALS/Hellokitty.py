import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import csv
import os

DATA_FILE = "sanrio_members.csv"

# Create file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Middle Name", "Last Name", "Birthday", "Gender", "Sanrio Character"])


def sign_up():
    def save_data():
        try:
            first = entry_first.get()
            middle = entry_middle.get()
            last = entry_last.get()
            birthday = entry_birthday.get()
            gender = gender_var.get()
            character = character_var.get()

            if not all([first, middle, last, birthday, gender, character]):
                raise ValueError("All fields must be filled.")

            with open(DATA_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([first, middle, last, birthday, gender, character])
            
            messagebox.showinfo("Yay!", f"You're now a Sanrio Land Member!\nCharacter: {character}")
            signup_window.destroy()
        except Exception as e:
            messagebox.showerror("Oops!", str(e))

    signup_window = tk.Toplevel(root)
    signup_window.title("Sanrio Sign Up")
    signup_window.configure(bg="#ffe6f0")

    labels = ["First Name", "Middle Name", "Last Name", "Birthday (YYYY-MM-DD)", "Gender", "Sanrio Character"]
    
    tk.Label(signup_window, text="First Name", bg="#ffe6f0", font=("Comic Sans MS", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_first = tk.Entry(signup_window, font=("Comic Sans MS", 12))
    entry_first.grid(row=0, column=1)

    tk.Label(signup_window, text="Middle Name", bg="#ffe6f0", font=("Comic Sans MS", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_middle = tk.Entry(signup_window, font=("Comic Sans MS", 12))
    entry_middle.grid(row=1, column=1)

    tk.Label(signup_window, text="Last Name", bg="#ffe6f0", font=("Comic Sans MS", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_last = tk.Entry(signup_window, font=("Comic Sans MS", 12))
    entry_last.grid(row=2, column=1)

    tk.Label(signup_window, text="Birthday (YYYY-MM-DD)", bg="#ffe6f0", font=("Comic Sans MS", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_birthday = tk.Entry(signup_window, font=("Comic Sans MS", 12))
    entry_birthday.grid(row=3, column=1)

    tk.Label(signup_window, text="Gender", bg="#ffe6f0", font=("Comic Sans MS", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
    gender_var = tk.StringVar()
    entry_gender = tk.OptionMenu(signup_window, gender_var, "Female", "Male")
    entry_gender.config(font=("Comic Sans MS", 12))
    entry_gender.grid(row=4, column=1)

    # Sanrio Character Dropdown
    tk.Label(signup_window, text="Sanrio Character", bg="#ffe6f0", font=("Comic Sans MS", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="e")
    character_var = tk.StringVar()
    characters = ["Hello Kitty", "My Melody", "Kuromi", "Cinnamoroll", "Pompompurin", "Keroppi", "Badtz-Maru", "Chococat", "Little Twin Stars"]
    character_menu = tk.OptionMenu(signup_window, character_var, *characters)
    character_menu.config(font=("Comic Sans MS", 12))
    character_menu.grid(row=5, column=1)

    #Submit Button
    tk.Button(signup_window, text="🌸 Join Now! 🌸", bg= "#feb9ca", command=save_data, font=("Comic Sans MS", 12)).grid(row=6, columnspan=2, pady=15)


def view_all():
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            records = list(reader)

        view_window = tk.Toplevel(root)
        view_window.title("All Sanrio Members")
        view_window.configure(bg="#ffe6f0")
        text = tk.Text(view_window, width=60, height=20, font=("Comic Sans MS", 12), bg="white", fg="black")
        text.pack()

        for row in records:
            text.insert(tk.END, ', '.join(row) + '\n')
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_record():
    try:
        keyword = simpledialog.askstring("Search", "Enter Last Name:")
        if not keyword:
            return

        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            records = list(reader)

        found = [row for row in records if keyword.lower() in row[0].lower() or keyword.lower() in row[2].lower()]

        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        result_window.configure(bg="#ffe6f0")
        text = tk.Text(result_window, width=60, height=20, font=("Comic Sans MS", 12), bg="white", fg="black")
        text.pack()

        if found:
            for row in found:
                text.insert(tk.END, ', '.join(row) + '\n')
        else:
            text.insert(tk.END, "No matching Sanrio friends found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# MAIN GUI WINDOW
root = tk.Tk()
root.title("Join Sanrio Land")
root.geometry("500x500")


try:
    bg_image = Image.open("HELLOKITTYFINALS/bgsan.png")
    bg_image = bg_image.resize((500, 500))  
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Background image not found:", e)



try:
    logo_img = Image.open("HELLOKITTYFINALS/sanriologo.png")
    logo_img = logo_img.resize((200, 200))  
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_photo, bg="#ffe6f0")
    logo_label.pack(pady=(20, 10))  


    welcome_label = tk.Label(root, text="Welcome to Sanrio Land!", bg="#ffe6f0", font=("Comic Sans MS", 20, "bold"))
    welcome_label.pack(pady=(0, 20))  
except Exception as e:
    print("Logo not found or error loading:", e)
    tk.Label(root, text="Welcome to Sanrio Land!", bg="#ffe6f0", font=("Comic Sans MS", 20, "bold")).pack(pady=20)



frame = tk.Frame(root, bg="#ffe6f0")
frame.pack(expand=True)

btn_font = ("Comic Sans MS", 14)

tk.Button(frame, text="✨ Join Sanrio Land ✨", width=20, bg="#feb9ca", font=btn_font, command=sign_up).pack(pady=3)
tk.Button(frame, text="🌈 View All Members", width=20, bg= "#c8e3ff", font=btn_font, command=view_all).pack(pady=3)
tk.Button(frame, text="🔍 Search for a Friend", width=20, bg="#d7b8f2", font=btn_font, command=search_record).pack(pady=3)
tk.Button(frame, text="🚪 Exit", width=20, font=btn_font, bg= "#fff9b0", command=root.quit).pack(pady=3)

root.mainloop()

