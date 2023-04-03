from Models.Item import Item
from Models.Purchase import Purchase
import cv2
import pytesseract
import re

class PurchaseService:
    listItemsWithoutProcess = []
    listItemsDescartados = []
    
    def __init__(self, purchaseItem:Purchase):
        self.Purchase = purchaseItem
    
    def processImage(self):
        img = cv2.imread(self.Purchase._imagePath)
        custom_config = r'--oem 3 --psm 6'
        lista = re.split('\n', pytesseract.image_to_string(img, config=custom_config))
        for linea in lista:
            self.listItemsWithoutProcess.append(linea)
            self.processLine(linea)

    def processLine(self, linea):
        if "$" in linea and " C" in linea:
            lineaSplit = linea.split("$")
            producto = lineaSplit[0]
            precio = float(lineaSplit[1].split(" ")[0])
            total += precio
            cantidad += 1
            pI = Item(producto, precio)
            self.Purchase.listItems.append(pI)
        else:
            self.listItemsDescartados.append(linea)

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
            
    def getUnknowItem(self,index):
        return self.listItemsDescartados[index]
    
    def getItemsWithoutProcess(self,index):
        return self.listItemsWithoutProcess[index]
    
    def getItem(self,index):
        return self.Purchase.listItems[index]