from Item import Item
import cv2 
import pytesseract
import re

class Purchase:
    listItems = []
    listItemsDescartados = []

    def __init__(self,imagePath,purchaseDate):
        self._imagePath = imagePath
        self._purchaseDate = purchaseDate
        
    def processImage(self):
        img = cv2.imread(self._imagePath)
        custom_config = r'--oem 3 --psm 6'
        lista = re.split('\n',pytesseract.image_to_string(img, config=custom_config))
        for linea in lista:
            if "$" in linea and " C" in linea:
                lineaSplit = linea.split("$")
                producto = lineaSplit[0]
                precio = float(lineaSplit[1].split(" ")[0])
                total += precio
                cantidad += 1
                pI = Item(producto,precio)
                self.listItems.append(pI)
            else:
                self.listItemsDescartados.append(linea)


