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
Controlador de Lazo abierto ("Open Loop").
Librerias de Arranque...
'''
#--------------Control Lazo Abierto Proporcional ("Open Loop (P)")-------------
def OL_P(Kp,num,den,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    p_controller=control.TransferFunction([Kp],[1])#Ajustes de control...
    OP_sys=p_controller*sys
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(OP_sys, T=t)
    return (t,y)
#---------Control Lazo Abierto Proporcional-Integral ("Open Loop (PI)")--------
def OL_PI(Kp,Ki,num,den,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    pi_controller=control.TransferFunction([Kp,Ki],[1,0])#Ajustes de control...
    OP_sys=pi_controller*sys
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(OP_sys, T=t)
    return (t,y)
#-------Control Lazo Abierto Proporcional-Derivativo ("Open Loop (PD)")--------
def OL_PD(Kp,Kd,num,den,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    pi_controller=control.TransferFunction([Kd,Kp],[1])#Ajustes de control...
    OP_sys=pi_controller*sys
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(OP_sys, T=t)
    return (t,y)
#---Control Lazo Abierto Proporcional-Integral-Derivativo ("Open Loop (PID)")--
def OL_PID(Kp,Ki,Kd,num,den,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)#F.T. ingresada...
    pi_controller=control.TransferFunction([Kd,Kp,Ki],[1,0])#Ajustes de control...
    OP_sys=pi_controller*sys
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(OP_sys, T=t)
    return (t,y)