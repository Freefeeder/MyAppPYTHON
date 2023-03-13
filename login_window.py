import tkinter as tk
from tkinter import ttk
from menu import *

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Iniciar Sesión")
        self.root.geometry('500x350')
        self.root.resizable(width=False, height=False)

        title = tk.Label(
            self.root, text="SISTEMA DE RESERVAS\nDE CANCHAS", font=("Helvetica", "15"))
        title.pack(pady=20)

        user_frame = tk.Frame(self.root)
        user_frame.pack(pady=(0, 20))

        user_label = tk.Label(
            user_frame, text="Usuario:", font=("Helvetica", "12"), width=10, anchor='w')
        user_label.grid(column=0, row=0, sticky='w')

        self.user_entry = tk.Entry(user_frame, width=30)
        self.user_entry.grid(column=1, row=0, padx=(10, 0))

        password_label = tk.Label(
            user_frame, text="Contraseña:", font=("Helvetica", "12"), width=10, anchor='w')
        password_label.grid(column=0, row=1, sticky='w')

        self.password_entry = tk.Entry(
            user_frame, width=30, show="*")
        self.password_entry.grid(
            column=1, row=1, padx=(10, 0), pady=(10, 0))
        self.password_entry.bind('<Return>', self.login)

        login_button = ttk.Button(
            user_frame, text="Ingresar", command=self.login)
        login_button.grid(column=0, columnspan=2,
                           row=2, pady=(20, 0))

    def login(self, event=None):
        username = self.user_entry.get()
        password = self.password_entry.get()

        if not (username and password):
            tk.messagebox.showerror(
                '', 'Todos los campos son obligatorios')
            return

        if username == 'admin' and password == 'admin123':
            self.root.destroy()
            self.open_menu()
        else:
            tk.messagebox.showerror(
                '', 'Nombre de usuario o contraseña incorrectos')

    def open_menu(self):
        menu = tk.Tk()
        app = MenuWindow(menu, self.root)
        menu.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()