
import serial as s  #se requiere el modulo pyserial

arduino = s.Serial("COM5", timeout= 1, baudrate=9600)

if arduino.isOpen():
    while(True):
        cadena = arduino.readline()
        cadena = cadena.decode() ##decodificacion de la cadena

        cadena = cadena.replace("\r", "")
        cadena = cadena.replace("\n","")

        cadena = cadena.replace("E", "")
        cadena = cadena.replace("F", "")

        if cadena != "":
            print("R", cadena,"R")
            auxiliar = cadena.split("G")

            EstadosIniciales = list(map(int,auxiliar[:-1]))
            print()


