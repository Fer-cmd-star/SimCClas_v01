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
Controlador de Lazo cerrado ("Close Loop").
Librerias de Arranque...
'''
#--------------Control Lazo Cerrado Proporcional ("Close Loop (P)")------------
def CL_P(Kp,num,den,num_fb,den_fb,fb_gain,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    fb_sys = control.TransferFunction(num_fb, den_fb)
    fb_gain_SyS=fb_gain*sys*fb_sys#Retroalimentacion ingresada...
    p_controller=control.TransferFunction([Kp],[1])#Ajustes de control...
    CP_sys=control.feedback(p_controller*fb_gain_SyS)
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(CP_sys, T=t)
    return (t,y)
#--------Control Lazo Cerrado Proporcional-Integral ("Close Loop (PI)")--------
def CL_PI(Kp,Ki,num,den,num_fb,den_fb,fb_gain,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    fb_sys = control.TransferFunction(num_fb, den_fb)
    fb_gain_SyS=fb_gain*sys*fb_sys#Retroalimentacion ingresada...
    fb_gain_SyS=fb_gain*sys#Retroalimentacion ingresada...
    p_controller=control.TransferFunction([Kp,Ki],[1,0])#Ajustes de control...
    CP_sys=control.feedback(p_controller*fb_gain_SyS)
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(CP_sys, T=t)
    return (t,y)
#-------Control Lazo Cerrado Proporcional-Derivativo ("Close Loop (PD)")-------
def CL_PD(Kp,Kd,num,den,num_fb,den_fb,fb_gain,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    fb_sys = control.TransferFunction(num_fb, den_fb)
    fb_gain_SyS=fb_gain*sys*fb_sys#Retroalimentacion ingresada...
    fb_gain_SyS=fb_gain*sys#Retroalimentacion ingresada...
    p_controller=control.TransferFunction([Kd,Kp],[1])#Ajustes de control...
    CP_sys=control.feedback(p_controller*fb_gain_SyS)
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(CP_sys, T=t)
    return (t,y)
#--Control Lazo Cerrado Proporcional-Integral-Derivativo ("Close Loop (PID)")--
def CL_PID(Kp,Ki,Kd,num,den,num_fb,den_fb,fb_gain,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    fb_sys = control.TransferFunction(num_fb, den_fb)
    fb_gain_SyS=fb_gain*sys*fb_sys#Retroalimentacion ingresada...
    fb_gain_SyS=fb_gain*sys#Retroalimentacion ingresada...
    p_controller=control.TransferFunction([Kd,Kp,Ki],[1,0])#Ajustes de control...
    CP_sys=control.feedback(p_controller*fb_gain_SyS)
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(CP_sys, T=t)
    return (t,y)