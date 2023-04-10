from Controllers.PurchaseController import PurchaseController
from Service.PurchaseService import PurchaseService
from Repository.PurchaseRepository import PurchaseRepository
from typing import List
from Models.Purchase import Purchase
import os

purchaseDB= []
pRepository = PurchaseRepository(purchaseDB)
pService = PurchaseService(pRepository)
pController = PurchaseController(pService)
mensaje = ""

while True:
    # os.system('clear')
    pController.Index()
    print("\n**** Menu ****")
    print("1. ADD")
    print("2. DETAILS")
    print("3. EDIT")
    print("4. DELETE")
    print("5. EXIT")
    opcion = input("Ingrese numero de la opcion: ")
    if not opcion.isnumeric():
        mensaje = "El valor ingresado no es un numero"
    else:
        if int(opcion) < 1 or int(opcion)>5:
            mensaje = "El numero ingresado no corresponde a una de las opciones"
        else :
            if int(opcion) == 1:
                pController.Create()
            elif int(opcion) == 2:
                index = ""
                while not index.isnumeric():
                    index = input("Ingrese indice a actualizar: ")
                pController.Details(int(index))
            elif int(opcion) == 3:
                index = ""
                while not index.isnumeric():
                    index = input("Ingrese indice a actualizar: ")
                pController.Edit(int(index))
            elif int(opcion) == 4:
                index = ""
                while not index.isnumeric():
                    index = input("Ingrese indice a actualizar: ")
                pController.Delete(int(index))
            else:
                break    