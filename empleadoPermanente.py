#!/usr/bin/python3
from empleado import Empleado

class EmpleadoPermanente:
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.antiguedad = antiguedad

    def calcular_comision(self):
        comision = self.salario * self.antiguedad / 100
        return comision

    