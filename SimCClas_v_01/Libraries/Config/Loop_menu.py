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
def open_loop():
    def no_control():
        open_loop_window = tk.Toplevel()
        open_loop_window.title("Lazo abierto sin control")
        open_loop_window.geometry("600x420")  
        label_Ti=tk.Label(open_loop_window, text="Tiempo inicial (Ti):")
        fig, ax = plt.subplots(figsize=(8,4))
        ax.plot(0, 0)
        ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo abierto sin control')
        ax.grid()
        canvas = FigureCanvasTkAgg(fig, master=open_loop_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=10,y=125)
        #Ti
        label_Ti.grid(row=3, column=0, padx=5, pady=5)
        entry_Ti=tk.Entry(open_loop_window)
        entry_Ti.grid(row=3, column=1, padx=5, pady=5)
        #To
        label_To=tk.Label(open_loop_window, text="Tiempo final (To):")
        label_To.grid(row=4, column=0, padx=5, pady=5)
        entry_To=tk.Entry(open_loop_window)
        entry_To.grid(row=4, column=1, padx=5, pady=5)
        #Step
        label_step=tk.Label(open_loop_window, text="Intervalo (Step):")
        label_step.grid(row=5, column=0, padx=5, pady=5)
        entry_step=tk.Entry(open_loop_window)
        entry_step.grid(row=5, column=1, padx=5, pady=5)
        #FT
        label_FT = tk.Label(open_loop_window, text="PLANTA")
        label_FT.grid(row=3, column=2, padx=1, pady=1)
        entry_FT_num = tk.Entry(open_loop_window)
        entry_FT_num.insert(0, "[Numerador]")
        entry_FT_num.grid(row=4, column=2, padx=1, pady=0)
        entry_FT_dem = tk.Entry(open_loop_window)
        entry_FT_dem.insert(1, "[Denominador]")
        entry_FT_dem.grid(row=5, column=2, padx=1, pady=0)
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
            FT_num = convert_string_to_list(entry_FT_num.get()) if entry_FT_num.get() else None
            FT_dem = convert_string_to_list(entry_FT_dem.get()) if entry_FT_dem.get() else None 
            t,y=OP_MSC_step(FT_num,FT_dem,Ti,To,step)
            #Grafica
            fig, ax = plt.subplots(figsize=(8,4))
            ax.plot(t, y)
            ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo abierto sin control')
            ax.grid()
            canvas = FigureCanvasTkAgg(fig, master=open_loop_window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.place(x=10,y=125)
        boton_graficar=tk.Button(open_loop_window, text="Graficar", command=simular)
        boton_graficar.grid(row=4, column=5, padx=5, pady=5)
    def yes_control():
        open_loop_window = tk.Toplevel()
        open_loop_window.title("Lazo abierto con control")
        open_loop_window.geometry("640x420")
        label_Ti=tk.Label(open_loop_window, text="Tiempo inicial (Ti):")
        fig, ax = plt.subplots(figsize=(7,4))
        ax.plot(0, 0)
        ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo abierto sin control')
        ax.grid()
        canvas = FigureCanvasTkAgg(fig, master=open_loop_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=100,y=125)
        #Ti
        label_Ti.grid(row=2, column=0, padx=5, pady=5)
        entry_Ti=tk.Entry(open_loop_window)
        entry_Ti.grid(row=2, column=1, padx=5, pady=5)
        #To
        label_To=tk.Label(open_loop_window, text="Tiempo final (To):")
        label_To.grid(row=3, column=0, padx=5, pady=5)
        entry_To=tk.Entry(open_loop_window)
        entry_To.grid(row=3, column=1, padx=5, pady=5)
        #Step
        label_step=tk.Label(open_loop_window, text="Intervalo (Step):")
        label_step.grid(row=4, column=0, padx=5, pady=5)
        entry_step=tk.Entry(open_loop_window)
        entry_step.grid(row=4, column=1, padx=5, pady=5)
        #Kp
        label_kp=tk.Label(open_loop_window, text="Kp")
        label_kp.grid(row=2, column=3, padx=5, pady=5)
        entry_kp=tk.Entry(open_loop_window)
        entry_kp.grid(row=2, column=4, padx=5, pady=5)
        #Ki
        label_ki=tk.Label(open_loop_window, text="Ki")
        label_ki.grid(row=3, column=3, padx=5, pady=5)
        entry_ki=tk.Entry(open_loop_window)
        entry_ki.grid(row=3, column=4, padx=5, pady=5)
        #Kd
        label_kd=tk.Label(open_loop_window, text="Kd")
        label_kd.grid(row=4, column=3, padx=5, pady=5)
        entry_kd=tk.Entry(open_loop_window)
        entry_kd.grid(row=4, column=4, padx=5, pady=5)
        #FT
        label_FT = tk.Label(open_loop_window, text="PLANTA")
        label_FT.grid(row=2, column=2, padx=1, pady=1)
        entry_FT_num = tk.Entry(open_loop_window)
        entry_FT_num.insert(0, "[Numerador]")
        entry_FT_num.grid(row=3, column=2, padx=1, pady=0)
        entry_FT_dem = tk.Entry(open_loop_window)
        entry_FT_dem.insert(1, "[Denominador]")
        entry_FT_dem.grid(row=4, column=2, padx=1, pady=0)
        label_text=tk.Label(open_loop_window, text="*Ingresar datos como vector")
        label_text.grid(row=5, column=1, padx=5, pady=5)
        selected_curves=[]
        a=6
        curves_labels=['P', 'PI', 'PD', 'PID']       
        for i, curve in enumerate(curves_labels):
            var = StringVar()
            check = Checkbutton(open_loop_window, text=curve,variable=var,\
                                onvalue=curve, offvalue="")
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
        boton_graficar=tk.Button(open_loop_window, text="Graficar", command=simular)
        boton_graficar.grid(row=5, column=2, padx=5, pady=5)
    control_window = tk.Toplevel()
    control_window.title("Lazo Abierto")
    control_window.geometry("200x100")
    no_controlB = tk.Button(control_window, text="Sin control",command=no_control)
    no_controlB.pack(pady=10)
    yes_controlB = tk.Button(control_window, text="Con control", command=yes_control)
    yes_controlB.pack(pady=10)
    pass

def close_loop():
    def yes_control():
        close_loop_window = tk.Toplevel()
        close_loop_window.title("Lazo cerrado con control")
        close_loop_window.geometry("780x420")  
        label_Ti=tk.Label(close_loop_window, text="Tiempo inicial (Ti):")
        fig, ax = plt.subplots(figsize=(9,4))
        ax.plot(0, 0)
        ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo cerrado con control')
        ax.grid()
        canvas = FigureCanvasTkAgg(fig, master=close_loop_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=100,y=125)
        #Ti
        label_Ti.grid(row=2, column=0, padx=5, pady=5)
        entry_Ti=tk.Entry(close_loop_window)
        entry_Ti.grid(row=2, column=1, padx=5, pady=5)
        #To
        label_To=tk.Label(close_loop_window, text="Tiempo final (To):")
        label_To.grid(row=3, column=0, padx=5, pady=5)
        entry_To=tk.Entry(close_loop_window)
        entry_To.grid(row=3, column=1, padx=5, pady=5)
        #Step
        label_step=tk.Label(close_loop_window, text="Intervalo (Step):")
        label_step.grid(row=4, column=0, padx=5, pady=5)
        entry_step=tk.Entry(close_loop_window)
        entry_step.grid(row=4, column=1, padx=5, pady=5)
        #Kp
        label_kp=tk.Label(close_loop_window, text="Kp")
        label_kp.grid(row=2, column=4, padx=5, pady=5)
        entry_kp=tk.Entry(close_loop_window)
        entry_kp.grid(row=2, column=5, padx=1, pady=1)
        #Ki
        label_ki=tk.Label(close_loop_window, text="Ki")
        label_ki.grid(row=3, column=4, padx=5, pady=5)
        entry_ki=tk.Entry(close_loop_window)
        entry_ki.grid(row=3, column=5, padx=1, pady=1)
        #Kd
        label_kd=tk.Label(close_loop_window, text="Kd")
        label_kd.grid(row=4, column=4, padx=5, pady=5)
        entry_kd=tk.Entry(close_loop_window)
        entry_kd.grid(row=4, column=5, padx=1, pady=1)
        #FT
        label_FT = tk.Label(close_loop_window, text="PLANTA")
        label_FT.grid(row=2, column=2, padx=1, pady=1)
        entry_FT_num = tk.Entry(close_loop_window)
        entry_FT_num.insert(0, "[Numerador]")
        entry_FT_num.grid(row=3, column=2, padx=1, pady=0)
        entry_FT_dem = tk.Entry(close_loop_window)
        entry_FT_dem.insert(1, "[Denominador]")
        entry_FT_dem.grid(row=4, column=2, padx=1, pady=0)
        #G
        label_G = tk.Label(close_loop_window, text="RETROALIMENTACION")
        label_G.grid(row=2, column=3, padx=1, pady=1)
        entry_G_num = tk.Entry(close_loop_window)
        entry_G_num.insert(0, "[Numerador]")
        entry_G_num.grid(row=3, column=3, padx=1, pady=0)
        entry_G_dem = tk.Entry(close_loop_window)
        entry_G_dem.insert(1, "[Denominador]")
        entry_G_dem.grid(row=4, column=3, padx=1, pady=0)
        label_feedback_gain=tk.Label(close_loop_window, text="Feedback Gain")
        label_feedback_gain.grid(row=5, column=0, padx=5, pady=5)
        entry_feedback_gain=tk.Entry(close_loop_window)
        entry_feedback_gain.grid(row=5, column=1, padx=5, pady=5)
        label_text=tk.Label(close_loop_window, text="*Ingresar datos como vector")
        label_text.grid(row=5, column=3, padx=5, pady=5)
        selected_curves=[]
        a=6
        curves_labels=['P', 'PI', 'PD', 'PID']       
        for i, curve in enumerate(curves_labels):
            var = StringVar()
            check = Checkbutton(close_loop_window, text=curve,variable=var,\
                                onvalue=curve, offvalue="")
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
            feedback_gain = float(entry_feedback_gain.get()) if entry_feedback_gain.get() else None
            G_num = convert_string_to_list(entry_G_num.get()) if entry_G_num.get() else None
            G_dem = convert_string_to_list(entry_G_dem.get()) if entry_G_dem.get() else None
            FT_num = convert_string_to_list(entry_FT_num.get()) if entry_FT_num.get() else None
            FT_dem = convert_string_to_list(entry_FT_dem.get()) if entry_FT_dem.get() else None 
            t,p=CL_P(kp,FT_num,FT_dem,G_num,G_dem,feedback_gain,Ti,To,step)
            t,pi=CL_PI(kp,ki,FT_num,FT_dem,G_num,G_dem,feedback_gain,Ti,To,step)
            t,pd=CL_PD(kp,kd,FT_num,FT_dem,G_num,G_dem,feedback_gain,Ti,To,step)
            t,pid=CL_PID(kp,ki,kd,FT_num,FT_dem,G_num,G_dem,feedback_gain,Ti,To,step)
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
        boton_graficar=tk.Button(close_loop_window, text="Graficar", command=simular)
        boton_graficar.grid(row=5, column=2, padx=5, pady=5)
    def no_control():
        close_loop_window = tk.Toplevel()
        close_loop_window.title("Lazo cerrado sin control")
        close_loop_window.geometry("600x420")  
        label_Ti=tk.Label(close_loop_window, text="Tiempo inicial (Ti):")
        fig, ax = plt.subplots(figsize=(8,4))
        ax.plot(0, 0)
        ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo cerrado sin control')
        ax.grid()
        canvas = FigureCanvasTkAgg(fig, master=close_loop_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=10,y=125)
        #Ti
        label_Ti.grid(row=3, column=0, padx=5, pady=5)
        entry_Ti=tk.Entry(close_loop_window)
        entry_Ti.grid(row=3, column=1, padx=5, pady=5)
        #To
        label_To=tk.Label(close_loop_window, text="Tiempo final (To):")
        label_To.grid(row=4, column=0, padx=5, pady=5)
        entry_To=tk.Entry(close_loop_window)
        entry_To.grid(row=4, column=1, padx=5, pady=5)
        #Step
        label_step=tk.Label(close_loop_window, text="Intervalo (Step):")
        label_step.grid(row=5, column=0, padx=5, pady=5)
        entry_step=tk.Entry(close_loop_window)
        entry_step.grid(row=5, column=1, padx=5, pady=5)
        #FT
        label_FT = tk.Label(close_loop_window, text="PLANTA")
        label_FT.grid(row=3, column=2, padx=1, pady=1)
        entry_FT_num = tk.Entry(close_loop_window)
        entry_FT_num.insert(0, "[Numerador]")
        entry_FT_num.grid(row=4, column=2, padx=1, pady=0)
        entry_FT_dem = tk.Entry(close_loop_window)
        entry_FT_dem.insert(1, "[Denominador]")
        entry_FT_dem.grid(row=5, column=2, padx=1, pady=0)
        #G
        label_G = tk.Label(close_loop_window, text="RETROALIMENTACION")
        label_G.grid(row=3, column=3, padx=1, pady=1)
        entry_G_num = tk.Entry(close_loop_window)
        entry_G_num.insert(0, "[Numerador]")
        entry_G_num.grid(row=4, column=3, padx=1, pady=0)
        entry_G_dem = tk.Entry(close_loop_window)
        entry_G_dem.insert(1, "[Denominador]")
        entry_G_dem.grid(row=5, column=3, padx=1, pady=0)
        label_feedback_gain=tk.Label(close_loop_window, text="Feedback Gain")
        label_feedback_gain.grid(row=6, column=0, padx=5, pady=5)
        entry_feedback_gain=tk.Entry(close_loop_window)
        entry_feedback_gain.grid(row=6, column=1, padx=5, pady=5)
        label_text=tk.Label(close_loop_window, text="*Ingresar datos como vector")
        label_text.grid(row=6, column=3, padx=5, pady=5)
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
            feedback_gain = float(entry_feedback_gain.get()) if entry_feedback_gain.get() else None
            G_num = convert_string_to_list(entry_G_num.get()) if entry_G_num.get() else None
            G_dem = convert_string_to_list(entry_G_dem.get()) if entry_G_dem.get() else None
            FT_num = convert_string_to_list(entry_FT_num.get()) if entry_FT_num.get() else None
            FT_dem = convert_string_to_list(entry_FT_dem.get()) if entry_FT_dem.get() else None 
            t,y=CP_MSC_step(FT_num,FT_dem,G_num,G_dem,feedback_gain,Ti,To,step)
            #Grafica
            fig, ax = plt.subplots(figsize=(8,4))
            ax.plot(t, y)
            ax.set(xlabel='Tiempo', ylabel='Salida del sistema', title='Lazo cerrado con control')
            ax.grid()
            canvas = FigureCanvasTkAgg(fig, master=close_loop_window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.place(x=10,y=125)
        boton_graficar=tk.Button(close_loop_window, text="Graficar", command=simular)
        boton_graficar.grid(row=6, column=2, padx=5, pady=5)  
    control_window = tk.Toplevel()
    control_window.title("Lazo Cerrado")
    control_window.geometry("200x100")
    no_controlB = tk.Button(control_window, text="Sin control", command=no_control)
    no_controlB.pack(pady=10)
    yes_controlB = tk.Button(control_window, text="Con control", command=yes_control)
    yes_controlB.pack(pady=10)
    pass