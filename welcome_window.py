import tkinter as tk
from tkinter import ttk
from login_window import LoginWindow

class WelcomeWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Bienvenido")
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill='both', expand=True)

        # Etiqueta con mensaje de bienvenida
        welcome_label = ttk.Label(self.frame, text="Bienvenido al sistema", font=('Arial', 20))
        welcome_label.pack(pady=60)

        # Temporizador para cerrar la ventana automáticamente
        self.parent.after(3000, self.close_window)


    def close_window(self):
        self.parent.destroy()
        root = tk.Tk()
        app = LoginWindow(root)
        root.mainloop()

# Para probar el modulo manualmente
if __name__ == '__main__':
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()
