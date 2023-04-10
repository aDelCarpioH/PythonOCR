from typing import List
from Models.Purchase import Purchase
import sys
from io import StringIO

class PurchaseViews:
    
    def index(self,purchaseList: List[Purchase]):
        if len(purchaseList) > 0:
            headerCC = "Centro Comercial" + (" " * 40)
            headerDate = "Fecha" + (" " * 10)
            headerPath = "Imagen" + (" " * 100)
            print("\n",headerCC[:40],headerDate[:10],headerPath[:100])
            counter = 0
            for compra in purchaseList:
                print(counter,". ",compra)
                counter += 1
            
    
    def details(self,purchaseItem: Purchase):
        print("\n Purchase detail")
        print("Store: ", purchaseItem._centroComercial)
        print("Purchase date: ", purchaseItem._purchaseDate)
        print("Image path: ",purchaseItem._imagePath)
        print("\n Items")
        for item in purchaseItem.listItems:
            print(item)
        print("\n Items descartados")
        for linea in purchaseItem.listItemsDescartados:
            print(linea)
        print("\n Items sin procesar")
        for linea in purchaseItem.listItemsWithoutProcess:
            print(linea)
        input("Presione enter para regresar al menu")
        
    def Create(self):
        print("New purchase")
        centroComercial = input("Set a Store: ")
        purchaseDate = input("Set a Purchase date: ")
        imagePath = input("Set the Image path: ")
        newPurchase = Purchase(imagePath,purchaseDate,centroComercial)
        return newPurchase
    
    def Edit(self, purchaseEdit: Purchase):
        print("Update purchase information")
        # sys.stdin = StringIO(purchaseEdit._centroComercial)
        centroComercial = input("Set a Store : " + purchaseEdit._centroComercial + " :") 
        # sys.stdin = StringIO(purchaseEdit._purchaseDate)
        purchaseDate = input("Set a Purchase date: " + purchaseEdit._purchaseDate + " :")
        # sys.stdin = StringIO(purchaseEdit._imagePath)
        imagePath = input("Set the Image path: " + purchaseEdit._imagePath + " :")
        purchaseEdit._centroComercial = centroComercial
        purchaseEdit._purchaseDate = purchaseDate
        purchaseEdit._imagePath = imagePath
        return purchaseEdit
    
    def Delete(self,Index):
        print("Desea eliminar la compra ubicada en el indice ", Index,"?")
        respuesta = input("1. SI / 2. No, ingrese el numero de la opcion deseada:")
        return respuesta == "1"