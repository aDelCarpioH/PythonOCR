from typing import List
from Models.Purchase import Purchase
import sys
from io import StringIO

class PurchaseViews:
    
    def index(self,purchaseList: List[Purchase]):
        headerCC = "Centro Comercial" + (" " * 100)
        headerDate = "Fecha" + (" " * 20)
        headerPath = "Imagen" + (" " * 300)
        print(headerCC[:100],headerDate[:20],headerPath[:300])
        counter = 0
        for compra in purchaseList:
            print(counter,". ",compra)
        
    def details(self,purchaseItem: Purchase):
        print("Purchase detail")
        print("Store: ", purchaseItem._centroComercial)
        print("Purchase date: ", purchaseItem._purchaseDate)
        print("Image path: ",purchaseItem._imagePath)
        print("/n Items")
        for item in purchaseItem.listItems:
            print(item)
        print("/n Items descartados")
        for linea in purchaseItem.listItemsDescartados:
            print(linea)
        print("/n Items sin procesar")
        for linea in purchaseItem.listItemsWithoutProcess:
            print(linea)
    
    def Create(self):
        print("New purchase")
        centroComercial = input("Set a Store: ")
        purchaseDate = input("Set a Purchase date: ")
        imagePath = input("Set the Image path: ")
        newPurchase = Purchase(imagePath,purchaseDate,centroComercial)
        return newPurchase
    
    def Edit(self, purchaseEdit: Purchase):
        print("Update purchase information")
        sys.stdin = StringIO(purchaseEdit._centroComercial)
        centroComercial = input("Set a Store: ")
        sys.stdin = StringIO(purchaseEdit._purchaseDate)
        purchaseDate = input("Set a Purchase date: ")
        sys.stdin = StringIO(purchaseEdit._imagePath)
        imagePath = input("Set the Image path: ")
        purchaseEdit._centroComercial = centroComercial
        purchaseEdit._purchaseDate = purchaseDate
        purchaseEdit._imagePath = imagePath
        return purchaseEdit
    
    def Delete(self,Index):
        print("Desea eliminar la compra ubicada en el indice ", Index,"?")
        respuesta = input("1. SI / 2. No, ingrese el numero de la opcion deseada:")
        return respuesta == "1"