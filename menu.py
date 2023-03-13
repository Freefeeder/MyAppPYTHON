import tkinter as tk
from tkinter import ttk
from stock_buffet_window import StockBuffetWindow
from horarios_cancha import HorariosCanchasWindow

class MenuWindow:
    def __init__(self, parent, controller):
        # Create a top level window
        self.root = tk.Toplevel(parent)
        self.root.title("Menú Principal")
        self.root.geometry('350x200')
        self.root.resizable(width=False, height=False)

        # Add buttons to open windows
        stock_button = ttk.Button(self.root, text="Stock Buffet", 
                                  command=self.open_menu_stock)
        stock_button.pack(pady=20)

        schedules_button = ttk.Button(self.root, text="Horarios Canchas", 
                                      command=self.open_menu_canchas)
        schedules_button.pack(pady=20)

        self.controller = controller
 
    def open_menu_stock(self):
        # Destroy root window
        self.root.destroy()

        # Open the StockBuffetWindow
        app = StockBuffetWindow(tk.Toplevel(self.controller))
        app.mainloop()

    def open_menu_canchas(self):
        # Destroy root window
        self.root.destroy()

        # Open the HorariosCanchaWindow        
        app = HorariosCanchasWindow(tk.Toplevel(self.controller))
        app.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    menu_window = MenuWindow(root)
    root.mainloop()
