from Models.Purchase import Purchase
from Service.PurchaseService import PurchaseService 
from Views.PurchaseViews import PurchaseViews

class PurchaseController:
    
    def __init__(self,service :PurchaseService):
        self.pService = service
        self.pView = PurchaseViews()
        
    def Index(self):
        self.pView.index(self.pService.getPurchases())
        
    def Details(self, index):
        self.pView.details(self.pService.getPurchaseItem(index))
        
    def Create(self):
        pObject = self.pView.Create()
        self.pService.Add(pObject)
        print("Purchase Created")
        
    def Edit(self, index):
        pObject = self.pService.getPurchaseItem(index)
        pObject = self.pView.Edit(pObject)
        self.pService.Update(index,pObject)
        print("Purchase Updated")
    
    def Delete(self,index):
        self.pService.Delete(index)
        print("Purchase Deleted")