# -*- coding: utf-8 -*-
"""
Universidad Autonoma de Zacatecas "Francisco Garcias Salinas"
Unidad Academica de Ingenieria Electrica. <-------> Ingenieria en Electronica
Industrial.
Agencia Espacial Mexicana. <-----> Centro Regional de Desarrollo Espacial.
SimCClas version 1.0 
Autor: Fernando Campos Campos.; Especializacion en Telecomunicaciones.
Correo institucional: 37185687@uaz.edu.mx
"""
import tkinter as tk
from Libraries.Config.Loop_menu import open_loop, close_loop
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // screen_height
    window.geometry(f"{width}x{height}+{x}+{y}")
ventana = tk.Tk()
ventana.title("SimCClas version 1")
ventana.geometry("400x500")
UAZ_logo_imag = tk.PhotoImage(file="Images/UAZ_logo.png")
UAZ_imag = tk.Label(ventana, image=UAZ_logo_imag)
UAZ_imag.grid(row=0, column=0, columnspan=1, pady=1)
UAIE_logo_imag = tk.PhotoImage(file="Images/UAIE_logo.png")
UAIE_imag = tk.Label(ventana, image=UAIE_logo_imag)
UAIE_imag.grid(row=0, column=3, columnspan=1, pady=1)
CREDES_logo_imag = tk.PhotoImage(file="Images/CREDES_logo.png")
CREDES_imag = tk.Label(ventana, image=CREDES_logo_imag)
CREDES_imag.grid(row=0, column=2, columnspan=1, pady=1)
Lazo_abierto_logo_imag = tk.PhotoImage(file="Images/Lazo_abierto_logo.png")
Lazo_abierto_imag = tk.Label(ventana, image=Lazo_abierto_logo_imag)
Lazo_abierto_imag.place(x=0, y=200)
Lazo_cerrado_logo_imag = tk.PhotoImage(file="Images/Lazo_cerrado_logo.png")
Lazo_cerrado_imag = tk.Label(ventana, image=Lazo_cerrado_logo_imag)
Lazo_cerrado_imag.place(x=5, y=325)
font_bold_1 = ("Arial", 14, "bold") 
font_bold_2 = ("Arial", 12, "bold")
label_text = tk.Label(ventana, text="¡Bienvenido a SimCClas!", font=font_bold_1, fg="brown")
label_text.place(x=80,y=115)
open_loopB = tk.Button(ventana, text="Lazo Abierto", font=font_bold_2, command=open_loop, width=41)
close_loopB = tk.Button(ventana, text="Lazo Cerrado", font=font_bold_2 ,command=close_loop, width=41)
open_loopB.place(x=2, y=150)
close_loopB.place(x=2, y=275)
center_window(ventana, 400, 500)

ventana.mainloop()

