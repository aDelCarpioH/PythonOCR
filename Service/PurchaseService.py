from Models.Item import Item
from Models.Purchase import Purchase
from Repository.PurchaseRepository import PurchaseRepository
import cv2
import pytesseract
import re
from typing import List

class PurchaseService:
    
    
    def __init__(self, objRepository: PurchaseRepository):
        self.Repository = objRepository
    
    def Add(self,purchaseItem: Purchase):
        self.processImage(purchaseItem)
        return self.Repository.Add(purchaseItem)
    
    def Update(self,index, purchaseItem: Purchase):
        self.processImage(purchaseItem)
        return self.Repository.Update(index,purchaseItem)
        
    def Delete(self, index):
        return self.Repository.Delete(index)
        
    def processImage(self,purchaseItem: Purchase):
        img = cv2.imread(purchaseItem._imagePath)
        custom_config = r'--oem 3 --psm 6'
        lista = re.split('\n', pytesseract.image_to_string(img, config=custom_config))
        for linea in lista:
            purchaseItem.listItemsWithoutProcess.append(linea)
            if "$" in linea and " C" in linea:
                item = self.processLine(linea)
                purchaseItem.listItems.append(item)
            else:
                purchaseItem.listItemsDescartados.append(linea)

    def processLine(self, linea):
            lineaSplit = linea.split("$")
            producto = lineaSplit[0]
            precio = float(lineaSplit[1].split(" ")[0])
            # total += precio
            # cantidad += 1
            pI = Item(producto, precio)
            return pI
            
    def getPurchases(self):
        return self.Repository.getAllItems()
    
    
    def getPurchaseItem(self,index):
        return self.Repository.getItem(index)
    
    # def showItems(self):
    #     index = 0
    #     for iItem in self.Purchase.listItems:
    #         print(index,". ",iItem)
            
    # def showUnknowItems(self):
    #     index = 0
    #     for iItem in self.listItemsDescartados:
    #         print(index,". ",iItem)
    
    # def showItemsWithoutProcess(self):
    #     index = 0
    #     for iItem in self.listItemsWithoutProcess:
    #         print(index,". ",iItem)
            
    # def getUnknowItem(self,index):
    #     return self.Purchase.listItemsDescartados[index]
    
    # def getItemsWithoutProcess(self,index):
    #     return self.Purchase.listItemsWithoutProcess[index]
    
    # def getItem(self,index):
    #     return self.Purchase.listItems[index]