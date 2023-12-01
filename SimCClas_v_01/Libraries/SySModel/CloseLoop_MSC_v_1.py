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
import control 
import numpy as np

'''
Modelo sin controlador de Lazo abierto ("Close Loop No controller").
Librerias de Arranque...
'''
def CP_MSC_step(num,den,num_fb,den_fb,feedback_gain,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)
    fb_sys = control.TransferFunction(num_fb, den_fb)
    fb_gain_SyS=fb_sys*sys*feedback_gain
    sc=fb_gain_SyS/(1+fb_gain_SyS)
    step = int((t_end-t_start)/t_step)+1
    t = np.linspace(t_start, t_end, step)
    t, y = control.step_response(sc, T=t)
    
    return (t,y)
