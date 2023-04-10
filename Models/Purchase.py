class Purchase:
    listItems = []
    listItemsWithoutProcess = []
    listItemsDescartados = []

    def __init__(self, imagePath, purchaseDate,centroComercial):
        self._imagePath = imagePath
        self._purchaseDate = purchaseDate
        self._centroComercial = centroComercial
    
    def __str__(self):
        centroComercialL = self._centroComercial + (" " * 30)
        centroComercialL = centroComercialL[:30]
        purchaseDateL = str(self._purchaseDate) + (" " * 10)
        purchaseDateL = purchaseDateL[:10]
        imagePathL = self._imagePath + (" "* 100)
        imagePathL = imagePathL[:100]
        
        return centroComercialL + "\t" + purchaseDateL + "\t" + imagePathL