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
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
ventana = tk.Tk()
ventana.title("SimCClas version 1")
ventana.geometry("300x400")
open_loopB = tk.Button(ventana, text="Lazo Abierto", command=open_loop)
close_loopB = tk.Button(ventana, text="Lazo Cerrado", command=close_loop)
open_loopB.grid(row=2, column=1, pady=10)
close_loopB.grid(row=1, column=1, pady=10)
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(0, weight=1)
center_window(ventana, 300, 400)

ventana.mainloop()

