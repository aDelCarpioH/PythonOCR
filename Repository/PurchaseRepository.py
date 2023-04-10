from typing import List
from Models.Purchase import Purchase

class PurchaseRepository:

    

    def __init__(self,purchaseDBInput: List[Purchase]):
        self.PurchaseDB = purchaseDBInput
        print(type(self.PurchaseDB))
        print("repository created")
        
    def getAllItems(self):
        return self.PurchaseDB

    def getItem(self,index):
        return self.PurchaseDB[index]

    def Add(self,purchase: Purchase):
        self.PurchaseDB.append(purchase)
        return True

    def Update(self,index,purchase: Purchase):
        self.PurchaseDB[index]= purchase
        return True
        
    def Delete(self,index):
        del self.PurchaseDB[index]
        return True
        

