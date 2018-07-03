#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

global provedores
global productos


def main(args):
    IniciarDatos()
    menu()


def IniciarDatos():
    # aqui se ingresan los provedores
    global provedores
    provedores = []
    # aqui se ingresa los productos electronicos
    global productos
    productos = []


def menu():
    while True:
        os.system("cls")
        print("\t::Menu::")
        print("1.- Registrar Proveedor")
        print("2.- Registrar Productos Electronico")
        print("3.- Listar Proveedores")
        print("4.- Listar Productos Electronicos")
        print("5.- Salir")
        iOpcion = int(input("Seleccione una opcion. "))
        if iOpcion == 1:
            OpcionUno()
            continue
        elif iOpcion == 2:
            # opcionDos()
            continue
        elif iOpcion == 3:
            opcionTres()
            continue
        elif iOpcion == 4:
            # opcionDos()
            continue
        elif iOpcion == 5:
            print("Programa finalizado")
            break


def OpcionUno():
    global provedores
    CodPro = input("Codigo de Proveedor. ")
    if (CodPro.isdigit()):
        CodProv = int(CodPro)
    else:
        print("Deve ingresarv numeros")
        input("Sera regresado al Menu,presione Enter para continuar...")
        menu()
    NomProv = input("Nombre Proveedor. ")
    PaiProv = input("Pais Proveedor. ")
    DirProv = input("Direccion Proveedor. ")
    TelefProv = input("Telefono de Proveedor. ")
    if (TelefProv.isdigit()):
        TelProv = int(TelefProv)
    else:
        print("Deve ingresar numeros. ")
        input("Sera regresado al Menu, presione Enter para continuar...")
        menu()
    CorrProv = input("Email Proveedor. ")
    proveedor = (CodPro, NomProv, PaiProv, DirProv, TelProv, CorrProv)
    provedores.append(proveedor)
    input("Registro exitoso, Enter para regresar a menu...")


def opcionTres():
    while True:
        os.system("cls")
        global provedores
        for proveedor in provedores:
            print(proveedor)
        input("Presione Enter para Continuar")
        menu()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))