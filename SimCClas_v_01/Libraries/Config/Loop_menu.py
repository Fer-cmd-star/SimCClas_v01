#!/usr/bin/env python3
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
from tkinter import StringVar,Checkbutton
import ast
import matplotlib.pyplot as plt
from Libraries.SySModel.OpenLoop_MSC_v_1 import OP_MSC_step
from Libraries.SySModel.CloseLoop_MSC_v_1 import CP_MSC_step
from Libraries.ControlSyS.OpenLoop_v_1 import OL_P,OL_PI,OL_PD,OL_PID
from Libraries.ControlSyS.CloseLoop_v_1 import CL_P,CL_PI,CL_PD,CL_PID
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
open_loop_no_control=False
open_loop_yes_control=False
close_loop_yes_control=False
close_loop_no_control=False
open_loop_window = False
close_loop_window = False 
close_loop_window_1=None
close_loop_window_2=None
control_window_1 = None
open_loop_window_2=None
control_window_2 = None
open_loop_window_1=None
def closing_close_loop_1():
    global open_loop_window
    global control_window_1
    open_loop_window=False
    control_window_1.destroy()
    return
def closing_close_loop_2():
    global close_loop_window
    global control_window_2
    close_loop_window=False
    control_window_2.destroy()
    return
def closing_close_loop_3():
    global open_loop_window_1
    global open_loop_no_control
    open_loop_no_control=False
    open_loop_window_1.destroy()
    return
def closing_close_loop_4():
    global open_loop_window_2
    global open_loop_yes_control
    open_loop_yes_control=False
    open_loop_window_2.destroy()
    return
def closing_close_loop_5():
    global close_loop_window_1
    global close_loop_yes_control
    close_loop_yes_control=False
    close_loop_window_1.destroy()
    return
def closing_close_loop_6():
    global close_loop_window_2
    global close_loop_no_control
    close_loop_no_control=False
    close_loop_window_2.destroy()
    return
    
    
def open_loop():
    def no_control():
        def save_plot():
            global fig
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                fig.savefig(file_path)
                canvas_widget.get_tk_widget().update()
        global open_loop_window_1
        global open_loop_no_control
        if open_loop_no_control is False:
            open_loop_window_1 = tk.Toplevel()
            open_loop_window_1.title("Lazo abierto sin control")
            open_loop_window_1.geometry("600x420")  
            menubar = tk.Menu(open_loop_window_1)
            open_loop_window_1.config(menu=menubar)
            file_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Archivo", menu=file_menu)
            file_menu.add_command(label="Exportar imagen", command=save_plot)
            label_Ti=tk.Label(open_loop_window_1, text="Tiempo inicial (Ti):")
            fig, ax = plt.subplots(figsize=(8,4))
            ax.plot(0, 0)
            ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo abierto sin control')
            ax.grid()
            canvas = FigureCanvasTkAgg(fig, master=open_loop_window_1)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.place(x=10,y=125)
            #Ti
            label_Ti.grid(row=3, column=0, padx=5, pady=5)
            entry_Ti=tk.Entry(open_loop_window_1)
            entry_Ti.grid(row=3, column=1, padx=5, pady=5)
            #To
            label_To=tk.Label(open_loop_window_1, text="Tiempo final (To):")
            label_To.grid(row=4, column=0, padx=5, pady=5)
            entry_To=tk.Entry(open_loop_window_1)
            entry_To.grid(row=4, column=1, padx=5, pady=5)
            #Step
            label_step=tk.Label(open_loop_window_1, text="Intervalo (Step):")
            label_step.grid(row=5, column=0, padx=5, pady=5)
            entry_step=tk.Entry(open_loop_window_1)
            entry_step.grid(row=5, column=1, padx=5, pady=5)
            #FT
            label_FT = tk.Label(open_loop_window_1, text="PLANTA")
            label_FT.grid(row=3, column=2, padx=1, pady=1)
            entry_FT_num = tk.Entry(open_loop_window_1)
            entry_FT_num.insert(0, "Numerador")
            entry_FT_num.grid(row=4, column=2, padx=1, pady=0)
            entry_FT_dem = tk.Entry(open_loop_window_1)
            entry_FT_dem.insert(1, "Denominador")
            entry_FT_dem.grid(row=5, column=2, padx=1, pady=0)
            label_text=tk.Label(open_loop_window_1, text="*Ingresar datos como vector. Ejemplo: 1,1,1")
            label_text.place(x=270,y=100)
            def simular():
                global fig
                t=[]
                y=[]
                def convert_string_to_list(s):
                    try:
                        return ast.literal_eval(s)
                    except (ValueError, SyntaxError):   
                        return None
                Ti = float(entry_Ti.get()) if entry_Ti.get() else None
                To = float(entry_To.get()) if entry_To.get() else None
                step = float(entry_step.get()) if entry_step.get() else None
                FT_num = convert_string_to_list(entry_FT_num.get()) if entry_FT_num.get() else None
                FT_dem = convert_string_to_list(entry_FT_dem.get()) if entry_FT_dem.get() else None 
                t,y=OP_MSC_step(FT_num,FT_dem,Ti,To,step)
                #Grafica
                fig, ax = plt.subplots(figsize=(8,4))
                ax.plot(t, y)
                ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo abierto sin control')
                ax.grid()
                canvas = FigureCanvasTkAgg(fig, master=open_loop_window_1)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.place(x=10,y=125)
            boton_graficar=tk.Button(open_loop_window_1, text="Graficar", command=simular)
            boton_graficar.grid(row=4, column=5, padx=5, pady=5)
            open_loop_no_control=True
            open_loop_window_1.protocol("WM_DELETE_WINDOW",closing_close_loop_3)
            
    def yes_control():
        def save_plot():
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                fig.savefig(file_path)
                canvas_widget.get_tk_widget().update()
        global open_loop_window_2
        global open_loop_yes_control
        if open_loop_yes_control is False:
            open_loop_window_2 = tk.Toplevel()
            open_loop_window_2.title("Lazo abierto con control")
            open_loop_window_2.geometry("740x420")
            menubar = tk.Menu(open_loop_window_2)
            open_loop_window_2.config(menu=menubar)
            file_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Archivo", menu=file_menu)
            file_menu.add_command(label="Exportar imagen", command=save_plot)
            label_Ti=tk.Label(open_loop_window_2, text="Tiempo inicial (Ti):")
            fig, ax = plt.subplots(figsize=(8.8,4))
            ax.plot(0, 0)
            ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo abierto sin control')
            ax.grid()
            canvas = FigureCanvasTkAgg(fig, master=open_loop_window_2)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.place(x=100,y=125)
            #Ti
            label_Ti=tk.Label(open_loop_window_2, text="Tiempo inicial (Ti):")
            label_Ti.grid(row=2, column=0, padx=5, pady=5)
            entry_Ti=tk.Entry(open_loop_window_2)
            entry_Ti.grid(row=2, column=1, padx=5, pady=5)
            #To
            label_To=tk.Label(open_loop_window_2, text="Tiempo final (To):")
            label_To.grid(row=3, column=0, padx=5, pady=5)
            entry_To=tk.Entry(open_loop_window_2)
            entry_To.grid(row=3, column=1, padx=5, pady=5)
            #Step
            label_step=tk.Label(open_loop_window_2, text="Intervalo (Step):")
            label_step.grid(row=4, column=0, padx=5, pady=5)
            entry_step=tk.Entry(open_loop_window_2)
            entry_step.grid(row=4, column=1, padx=5, pady=5)
            #Kp
            label_kp=tk.Label(open_loop_window_2, text="Kp")
            label_kp.grid(row=2, column=3, padx=5, pady=5)
            entry_kp=tk.Entry(open_loop_window_2)
            entry_kp.grid(row=2, column=4, padx=5, pady=5)
            #Ki
            label_ki=tk.Label(open_loop_window_2, text="Ki")
            label_ki.grid(row=3, column=3, padx=5, pady=5)
            entry_ki=tk.Entry(open_loop_window_2)
            entry_ki.grid(row=3, column=4, padx=5, pady=5)
            #Kd
            label_kd=tk.Label(open_loop_window_2, text="Kd")
            label_kd.grid(row=4, column=3, padx=5, pady=5)
            entry_kd=tk.Entry(open_loop_window_2)
            entry_kd.grid(row=4, column=4, padx=5, pady=5)
            #FT
            label_FT = tk.Label(open_loop_window_2, text="PLANTA")
            label_FT.grid(row=2, column=2, padx=1, pady=1)
            entry_FT_num = tk.Entry(open_loop_window_2)
            entry_FT_num.insert(0, "Numerador")
            entry_FT_num.grid(row=3, column=2, padx=1, pady=0)
            entry_FT_dem = tk.Entry(open_loop_window_2)
            entry_FT_dem.insert(1, "Denominador")
            entry_FT_dem.grid(row=4, column=2, padx=1, pady=0)
            label_text_1=tk.Label(open_loop_window_2, text="*Ingresar datos como vector. Ejemplo: 1,1,1")
            label_text_1.grid(row=5, column=2, padx=5, pady=5)
            label_text_2=tk.Label(open_loop_window_2, text="*Inicializar en 0 si no se utiliza")
            label_text_2.grid(row=5, column=4, padx=5, pady=5)
            selected_curves=[]
            a=6
            curves_labels=['P', 'PI', 'PD', 'PID']       
            for i, curve in enumerate(curves_labels):
                var = StringVar()
                check = Checkbutton(open_loop_window_2, text=curve,variable=var,onvalue=curve, offvalue="")
                a=a+1
                check.grid(row=a, column=0, padx=5, pady=5)
                selected_curves.append(var)
            def simular():
                def convert_string_to_list(s):
                    try:
                        return ast.literal_eval(s)
                    except (ValueError, SyntaxError):   
                        return None
                Ti = float(entry_Ti.get()) if entry_Ti.get() else None
                To = float(entry_To.get()) if entry_To.get() else None
                step = float(entry_step.get()) if entry_step.get() else None
                kp = float(entry_kp.get()) if entry_kp.get() else None
                ki = float(entry_ki.get()) if entry_ki.get() else None
                kd = float(entry_kd.get()) if entry_kd.get() else None
                FT_num = convert_string_to_list(entry_FT_num.get()) if entry_FT_num.get() else None
                FT_dem = convert_string_to_list(entry_FT_dem.get()) if entry_FT_dem.get() else None 
                t,p=OL_P(kp,FT_num,FT_dem,Ti,To,step)
                t,pi=OL_PI(kp,ki,FT_num,FT_dem,Ti,To,step)
                t,pd=OL_PD(kp,kd,FT_num,FT_dem,Ti,To,step)
                t,pid=OL_PID(kp,ki,kd,FT_num,FT_dem,Ti,To,step)
                ax.clear()
                for var in selected_curves:
                    curve=var.get()
                    if curve == 'P':
                        ax.plot(t, p, 'b-', label='P')
                    elif curve == 'PI':
                        ax.plot(t, pi, 'g-', label='PI')
                    elif curve == 'PD':
                        ax.plot(t, pd, 'r-', label='PD')
                    elif curve == 'PID':
                        ax.plot(t, pid, 'm-', label='PID')
                t = []
                p = []
                pi = []
                pd = []
                pid = []
                ax.set_title('Lazo abierto con control')
                ax.set_xlabel('Tiempo')
                ax.set_ylabel('Salida del sistema')
                ax.grid()
                ax.legend()
                fig.tight_layout()
                canvas.draw()
            boton_graficar=tk.Button(open_loop_window_2, text="Graficar", command=simular)
            boton_graficar.grid(row=5, column=1, padx=5, pady=5)
            open_loop_yes_control=True
            open_loop_window_2.protocol("WM_DELETE_WINDOW",closing_close_loop_4)
    global open_loop_window
    global control_window_1 
    if open_loop_window is False:
        def left_window(window, width, height):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x = (screen_width - width) // screen_width
            y = (screen_height - height) // screen_height
            window.geometry(f"{width}x{height}+{x}+{y}")
        control_window_1 = tk.Toplevel()
        control_window_1.title("Lazo Abierto")
        control_window_1.geometry("400x340")
        Lazo_abierto_logo_imag = tk.PhotoImage(file="Images/Lazo_abierto_logo.png")
        Lazo_abierto_imag = tk.Label(control_window_1, image=Lazo_abierto_logo_imag)
        Lazo_abierto_imag.place(x=0, y=245)
        Lazo_abierto_SC_logo_imag = tk.PhotoImage(file="Images/Lazo_abierto_SC_logo.png")
        Lazo_abierto_SC_imag = tk.Label(control_window_1, image=Lazo_abierto_SC_logo_imag)
        Lazo_abierto_SC_imag.place(x=0, y=100)
        font_bold_1 = ("Arial", 12, "bold")
        font_bold_2 = ("Arial", 10, "bold")
        label_text_1 = tk.Label(control_window_1, text="Los sistemas de control de lazo abierto se caracterizan", font=font_bold_2, fg="black")
        label_text_2 = tk.Label(control_window_1, text="por actuar sobre la señal de entrada, sin necesidad de", font=font_bold_2, fg="black")
        label_text_3 = tk.Label(control_window_1, text="tomar en cuenta lo que ocurrirá en la señal de salida.", font=font_bold_2, fg="black")
        label_text_1.place(x=4,y=1)
        label_text_2.place(x=4,y=15)
        label_text_3.place(x=2,y=30)
        no_controlB = tk.Button(control_window_1, text="Sin control",font=font_bold_1,command=no_control, width=41)
        no_controlB.place(x=2,y=65)
        yes_controlB = tk.Button(control_window_1, text="Con control",font=font_bold_1,command=yes_control, width=41)
        yes_controlB.place(x=2,y=200)
        Lazo_abierto_imag.image=Lazo_abierto_logo_imag
        Lazo_abierto_SC_imag.image=Lazo_abierto_SC_logo_imag
        open_loop_window=True
        control_window_1.protocol("WM_DELETE_WINDOW",closing_close_loop_1)
        left_window(control_window_1, 400, 340)
        control_window_1.mainloop()
    pass

def close_loop():
    def yes_control():
        def save_plot():
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                fig.savefig(file_path)
                canvas_widget.get_tk_widget().update()
        global close_loop_yes_control
        global close_loop_window_1
        if close_loop_yes_control is False:
            close_loop_window_1 = tk.Toplevel()
            close_loop_window_1.title("Lazo cerrado con control")
            close_loop_window_1.geometry("780x420")
            menubar = tk.Menu(close_loop_window_1)
            close_loop_window_1.config(menu=menubar)
            file_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Archivo", menu=file_menu)
            file_menu.add_command(label="Exportar imagen", command=save_plot)
            label_Ti=tk.Label(close_loop_window_1, text="Tiempo inicial (Ti):")
            fig, ax = plt.subplots(figsize=(9,4))
            ax.plot(0, 0)
            ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo cerrado con control')
            ax.grid()
            canvas = FigureCanvasTkAgg(fig, master=close_loop_window_1)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.place(x=100,y=125)
            #Ti
            label_Ti.grid(row=2, column=0, padx=5, pady=5)
            entry_Ti=tk.Entry(close_loop_window_1)
            entry_Ti.grid(row=2, column=1, padx=5, pady=5)
            #To
            label_To=tk.Label(close_loop_window_1, text="Tiempo final (To):")
            label_To.grid(row=3, column=0, padx=5, pady=5)
            entry_To=tk.Entry(close_loop_window_1)
            entry_To.grid(row=3, column=1, padx=5, pady=5)
            #Step
            label_step=tk.Label(close_loop_window_1, text="Intervalo (Step):")
            label_step.grid(row=4, column=0, padx=5, pady=5)
            entry_step=tk.Entry(close_loop_window_1)
            entry_step.grid(row=4, column=1, padx=5, pady=5)
            #Kp
            label_kp=tk.Label(close_loop_window_1, text="Kp")
            label_kp.grid(row=2, column=4, padx=5, pady=5)
            entry_kp=tk.Entry(close_loop_window_1)
            entry_kp.grid(row=2, column=5, padx=1, pady=1)
            #Ki
            label_ki=tk.Label(close_loop_window_1, text="Ki")
            label_ki.grid(row=3, column=4, padx=5, pady=5)
            entry_ki=tk.Entry(close_loop_window_1)
            entry_ki.grid(row=3, column=5, padx=1, pady=1)
            #Kd
            label_kd=tk.Label(close_loop_window_1, text="Kd")
            label_kd.grid(row=4, column=4, padx=5, pady=5)
            entry_kd=tk.Entry(close_loop_window_1)
            entry_kd.grid(row=4, column=5, padx=1, pady=1)
            #FT
            label_FT = tk.Label(close_loop_window_1, text="PLANTA")
            label_FT.grid(row=2, column=2, padx=1, pady=1)
            entry_FT_num = tk.Entry(close_loop_window_1)
            entry_FT_num.insert(0, "Numerador")
            entry_FT_num.grid(row=3, column=2, padx=1, pady=0)
            entry_FT_dem = tk.Entry(close_loop_window_1)
            entry_FT_dem.insert(1, "Denominador")
            entry_FT_dem.grid(row=4, column=2, padx=1, pady=0)
            #G
            label_G = tk.Label(close_loop_window_1, text="RETROALIMENTACION")
            label_G.grid(row=2, column=3, padx=1, pady=1)
            entry_G_num = tk.Entry(close_loop_window_1)
            entry_G_num.insert(0, "Numerador")
            entry_G_num.grid(row=3, column=3, padx=1, pady=0)
            entry_G_dem = tk.Entry(close_loop_window_1)
            entry_G_dem.insert(1, "Denominador")
            entry_G_dem.grid(row=4, column=3, padx=1, pady=0)
            #label_feedback_gain=tk.Label(close_loop_window_1, text="Feedback Gain")
            #label_feedback_gain.grid(row=5, column=0, padx=5, pady=5)
            #entry_feedback_gain=tk.Entry(close_loop_window_1)
            #entry_feedback_gain.grid(row=5, column=1, padx=5, pady=5)
            label_text=tk.Label(close_loop_window_1, text="*Ingresar datos como vector. Ejemplo 1,1,1")
            label_text.place(x=270,y=100)
            label_text_2=tk.Label(close_loop_window_1, text="*Inicializar en 0 si no se utiliza")
            label_text_2.place(x=570,y=100)
            selected_curves=[]
            a=6
            curves_labels=['P', 'PI', 'PD', 'PID']       
            for i, curve in enumerate(curves_labels):
                var = StringVar()
                check = Checkbutton(close_loop_window_1, text=curve,variable=var,onvalue=curve, offvalue="")
                a=a+1
                check.grid(row=a, column=0, padx=5, pady=5)
                selected_curves.append(var)
            def simular():
                def convert_string_to_list(s):
                    try:
                        return ast.literal_eval(s)
                    except (ValueError, SyntaxError):   
                        return None
                Ti = float(entry_Ti.get()) if entry_Ti.get() else None
                To = float(entry_To.get()) if entry_To.get() else None
                step = float(entry_step.get()) if entry_step.get() else None
                kp = float(entry_kp.get()) if entry_kp.get() else None
                ki = float(entry_ki.get()) if entry_ki.get() else None
                kd = float(entry_kd.get()) if entry_kd.get() else None
                #feedback_gain = float(entry_feedback_gain.get()) if entry_feedback_gain.get() else None
                G_num = convert_string_to_list(entry_G_num.get()) if entry_G_num.get() else None
                G_dem = convert_string_to_list(entry_G_dem.get()) if entry_G_dem.get() else None
                FT_num = convert_string_to_list(entry_FT_num.get()) if entry_FT_num.get() else None
                FT_dem = convert_string_to_list(entry_FT_dem.get()) if entry_FT_dem.get() else None 
                t,p=CL_P(kp,FT_num,FT_dem,G_num,G_dem,1,Ti,To,step)
                t,pi=CL_PI(kp,ki,FT_num,FT_dem,G_num,G_dem,1,Ti,To,step)
                t,pd=CL_PD(kp,kd,FT_num,FT_dem,G_num,G_dem,1,Ti,To,step)
                t,pid=CL_PID(kp,ki,kd,FT_num,FT_dem,G_num,G_dem,1,Ti,To,step)
                ax.clear()
                for var in selected_curves:
                    curve=var.get()
                    if curve == 'P':
                        ax.plot(t, p, 'b-', label='P')
                    elif curve == 'PI':
                        ax.plot(t, pi, 'g-', label='PI')
                    elif curve == 'PD':
                        ax.plot(t, pd, 'r-', label='PD')
                    elif curve == 'PID':
                        ax.plot(t, pid, 'm-', label='PID')
                #Grafica
                t = []
                p = []
                pi = []
                pd = []
                pid = []
                ax.set_title('Lazo cerrado con control')
                ax.set_xlabel('Tiempo')
                ax.set_ylabel('Salida del sistema')
                ax.grid()
                ax.legend()
                fig.tight_layout()
                canvas.draw()
            boton_graficar=tk.Button(close_loop_window_1, text="Graficar", command=simular)
            boton_graficar.place(x=150,y=90)
            close_loop_yes_control=True
            close_loop_window_1.protocol("WM_DELETE_WINDOW",closing_close_loop_5)
    def no_control():
        def save_plot():
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                fig.savefig(file_path)
                canvas_widget.get_tk_widget().update()
        global close_loop_no_control
        global close_loop_window_2
        if close_loop_no_control is False:
            close_loop_window_2 = tk.Toplevel()
            close_loop_window_2.title("Lazo cerrado sin control")
            close_loop_window_2.geometry("600x420")  
            menubar = tk.Menu(close_loop_window_2)
            close_loop_window_2.config(menu=menubar)
            file_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Archivo", menu=file_menu)
            file_menu.add_command(label="Exportar imagen", command=save_plot)
            label_Ti=tk.Label(close_loop_window_2, text="Tiempo inicial (Ti):")
            fig, ax = plt.subplots(figsize=(8,4))
            ax.plot(0, 0)
            ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo cerrado sin control')
            ax.grid()
            canvas = FigureCanvasTkAgg(fig, master=close_loop_window_2)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.place(x=10,y=125)
            #Ti
            label_Ti.grid(row=3, column=0, padx=5, pady=5)
            entry_Ti=tk.Entry(close_loop_window_2)
            entry_Ti.grid(row=3, column=1, padx=5, pady=5)
            #To
            label_To=tk.Label(close_loop_window_2, text="Tiempo final (To):")
            label_To.grid(row=4, column=0, padx=5, pady=5)
            entry_To=tk.Entry(close_loop_window_2)
            entry_To.grid(row=4, column=1, padx=5, pady=5)
            #Step
            label_step=tk.Label(close_loop_window_2, text="Intervalo (Step):")
            label_step.grid(row=5, column=0, padx=5, pady=5)
            entry_step=tk.Entry(close_loop_window_2)
            entry_step.grid(row=5, column=1, padx=5, pady=5)
            #FT
            label_FT = tk.Label(close_loop_window_2, text="PLANTA")
            label_FT.grid(row=3, column=2, padx=1, pady=1)
            entry_FT_num = tk.Entry(close_loop_window_2)
            entry_FT_num.insert(0, "Numerador")
            entry_FT_num.grid(row=4, column=2, padx=1, pady=0)
            entry_FT_dem = tk.Entry(close_loop_window_2)
            entry_FT_dem.insert(1, "Denominador")
            entry_FT_dem.grid(row=5, column=2, padx=1, pady=0)
            #G
            label_G = tk.Label(close_loop_window_2, text="RETROALIMENTACION")
            label_G.grid(row=3, column=3, padx=1, pady=1)
            entry_G_num = tk.Entry(close_loop_window_2)
            entry_G_num.insert(0, "Numerador")
            entry_G_num.grid(row=4, column=3, padx=1, pady=0)
            entry_G_dem = tk.Entry(close_loop_window_2)
            entry_G_dem.insert(1, "Denominador")
            entry_G_dem.grid(row=5, column=3, padx=1, pady=0)
            #label_feedback_gain=tk.Label(close_loop_window_2, text="Feedback Gain")
            #label_feedback_gain.grid(row=6, column=0, padx=5, pady=5)
            #entry_feedback_gain=tk.Entry(close_loop_window_2)
            #entry_feedback_gain.grid(row=6, column=1, padx=5, pady=5)
            label_text=tk.Label(close_loop_window_2, text="*Ingresar datos como vector. Ejemplo 1,1,1")
            label_text.place(x=270,y=100)
            def simular():
                t=[]
                y=[]
                def convert_string_to_list(s):
                    try:
                        return ast.literal_eval(s)
                    except (ValueError, SyntaxError):   
                        return None
                Ti = float(entry_Ti.get()) if entry_Ti.get() else None
                To = float(entry_To.get()) if entry_To.get() else None
                step = float(entry_step.get()) if entry_step.get() else None
                #feedback_gain = float(entry_feedback_gain.get()) if entry_feedback_gain.get() else None
                G_num = convert_string_to_list(entry_G_num.get()) if entry_G_num.get() else None
                G_dem = convert_string_to_list(entry_G_dem.get()) if entry_G_dem.get() else None
                FT_num = convert_string_to_list(entry_FT_num.get()) if entry_FT_num.get() else None
                FT_dem = convert_string_to_list(entry_FT_dem.get()) if entry_FT_dem.get() else None 
                t,y=CP_MSC_step(FT_num,FT_dem,G_num,G_dem,1,Ti,To,step)
                #Grafica
                fig, ax = plt.subplots(figsize=(8,4))
                ax.plot(t, y)
                ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo cerrado con control')
                ax.grid()
                canvas = FigureCanvasTkAgg(fig, master=close_loop_window_2)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.place(x=10,y=125)
            boton_graficar=tk.Button(close_loop_window_2, text="Graficar", command=simular)
            boton_graficar.place(x=150,y=90)
            close_loop_no_control=True
            close_loop_window_2.protocol("WM_DELETE_WINDOW",closing_close_loop_6)
    global close_loop_window
    global control_window_2
    if close_loop_window is False:
        def right_window(window, width, height):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x = (screen_width + width) // 1
            y = (screen_height + height) // screen_height
            window.geometry(f"{width}x{height}+{x}+{y}")
        control_window_2= tk.Toplevel()
        control_window_2.title("Lazo Cerrado")
        control_window_2.geometry("400x500")
        Lazo_cerrado_logo_imag = tk.PhotoImage(file="Images/Lazo_cerrado_logo.png")
        Lazo_cerrado_imag = tk.Label(control_window_2, image=Lazo_cerrado_logo_imag)
        Lazo_cerrado_imag.place(x=0, y=320)
        Lazo_cerrado_SC_logo_imag = tk.PhotoImage(file="Images/Lazo_cerrado_SC_logo.png")
        Lazo_cerrado_SC_imag = tk.Label(control_window_2, image=Lazo_cerrado_SC_logo_imag)
        Lazo_cerrado_SC_imag.place(x=0, y=100)
        font_bold_1 = ("Arial", 12, "bold")
        font_bold_2 = ("Arial", 10, "bold")
        label_text_1 = tk.Label(control_window_2, text="Los sistemas de control de lazo cerrado se caracterizan", font=font_bold_2, fg="black")
        label_text_2 = tk.Label(control_window_2, text="por la necesidad de corregir las desviaciones de un mo-", font=font_bold_2, fg="black")
        label_text_3 = tk.Label(control_window_2, text="delo que no puede mantenerse constante, esta correcci-", font=font_bold_2, fg="black")
        label_text_4 = tk.Label(control_window_2, text="ón se presenta de la salida frente a la referencia.", font=font_bold_2, fg="black")
        label_text_1.place(x=0,y=1)
        label_text_2.place(x=0,y=15)
        label_text_3.place(x=0,y=30)
        label_text_4.place(x=2,y=45)
        no_controlB = tk.Button(control_window_2, text="Sin control",font=font_bold_1,command=no_control, width=41)
        no_controlB.place(x=2,y=75)
        yes_controlB = tk.Button(control_window_2, text="Con control",font=font_bold_1 ,command=yes_control, width=41)
        yes_controlB.place(x=2,y=285)
        Lazo_cerrado_imag.image=Lazo_cerrado_logo_imag
        Lazo_cerrado_SC_imag.image=Lazo_cerrado_SC_logo_imag
        close_loop_window = True
        control_window_2.protocol("WM_DELETE_WINDOW",closing_close_loop_2)
        right_window(control_window_2, 400, 500)
    pass