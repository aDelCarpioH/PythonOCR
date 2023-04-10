class Purchase:
    listItems = []
    listItemsWithoutProcess = []
    listItemsDescartados = []

    def __init__(self, imagePath, purchaseDate,centroComercial):
        self._imagePath = imagePath
        self._purchaseDate = purchaseDate
        self._centroComercial = centroComercial
    
    def __str__(self):
        centroComercialL = self._centroComercial + (" " * 100)
        centroComercialL = centroComercialL[:100]
        purchaseDateL = str(self._purchaseDate) + (" " * 20)
        purchaseDateL = purchaseDateL[:20]
        imagePathL = self._imagePath + (" "* 300)
        imagePathL = imagePathL[:300]
        
        return centroComercialL + "\t" + purchaseDateL + "\t" + imagePathL