import time
import os
os.system('cls')
Semaforo=int(input("En que color esta el semaforo: \n1.Amarillo  \n2.Verde  \n3.Rojo  \n"))
time.sleep(2)
if Semaforo == 1:
    print("Esperar")
elif Semaforo ==2:
    print("Avanzar")
elif Semaforo ==3:
    print("Detenerse")
else:
    print("Invalido")

    