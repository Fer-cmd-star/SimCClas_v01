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
Modelo sin controlador de Lazo abierto ("Open Loop No controller").
Librerias de Arranque...
'''
def OP_MSC_step(num,den,t_start,t_end,t_step):
    sys=control.TransferFunction(num,den)
    step=int((t_end-t_start)/t_step)+1
    t=np.linspace(t_start,t_end,step)
    t,y=control.step_response(sys,T=t)
    
    return (t,y)


