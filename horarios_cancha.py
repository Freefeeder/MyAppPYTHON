import tkinter as tk
from tkinter import ttk
import reservation_manager
import db_manager

class Reservation:
    def __init__(self, court_no, start_time, end_time, available):
        self.court_no = court_no
        self.start_time = start_time
        self.end_time = end_time
        self.available = available

class HorariosCanchasWindow(tk.Frame):
    def __init__(self, parent, db_manager, reservation_manager):
        super().__init__(parent)
        self.db_manager = db_manager
        self.reservation_manager = reservation_manager
        self.create_main_frame()

    def create_main_frame(self):
        # Crear tabla para mostrar los horarios disponibles
        columns = (
            'No. de cancha',
            'Hora de inicio',
            'Hora de fin',
            'Disponibilidad'
        )
        table = ttk.Treeview(
            self, 
            columns=columns, 
            show='headings', 
            selectmode='none'
        )
        table.column('No. de cancha', width=100)
        table.column('Hora de inicio', width=150)
        table.column('Hora de fin', width=150)
        table.column('Disponibilidad', width=100)
        for col in columns:
            table.heading(col, text=col)
        table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Botón de reserva
        reserve_btn = tk.Button(
            self,
            text='Reservar',
            command=self.reserve_court
        )
        reserve_btn.pack(side=tk.RIGHT)

        # Obtener la lista de horarios desde la base de datos y agregarlos a la tabla
        reservations = self.reservation_manager.get_reservations()
        for res in reservations:
            table.insert('', 'end', values=[
                res.court_no,
                res.start_time,
                res.end_time,
                'Disponible' if res.available else 'Ocupado'
            ])

    def reserve_court(self):
        # Abrir ventana de reserva
        ReserveCourtWindow(self, self.reservation_manager)

class ReserveCourtWindow(tk.Toplevel):
    def __init__(self, parent, reservation_manager):
        super().__init__(parent)
        self.reservation_manager = reservation_manager
        self.court_no_entry = None
        self.start_time_entry = None
        self.end_time_entry = None
        self.create_main_frame()

    def create_main_frame(self):
        form = tk.Frame(self)
        form.pack(padx=10, pady=10)
        tk.Label(form, text='Número de cancha:').grid(column=0, row=0)
        self.court_no_entry = tk.Entry(form)
        self.court_no_entry.grid(column=1, row=0)
        tk.Label(form, text='Hora de inicio (HH:MM):').grid(column=0, row=1)
        self.start_time_entry = tk.Entry(form)
        self.start_time_entry.grid(column=1, row=1)
        tk.Label(form, text='Hora de fin (HH:MM):').grid(column=0, row=2)
        self.end_time_entry = tk.Entry(form)
        self.end_time_entry.grid(column=1, row=2)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        accept_btn = tk.Button(btn_frame, text='Aceptar', command=self.accept_reservation)
        accept_btn.pack(side=tk.LEFT)
        cancel_btn = tk.Button(btn_frame, text='Cancelar', command=self.destroy)
        cancel_btn.pack(side=tk.RIGHT)

    def accept_reservation(self):
        court_no = int(self.court_no_entry.get())
        start_time = self.start_time_entry.get().strip()
        end_time = self.end_time_entry.get().strip()

        reservation = Reservation(court_no, start_time, end_time)
        self.reservation_manager.add_reservation(reservation)

        self.master.update_table()
        self.destroy()
