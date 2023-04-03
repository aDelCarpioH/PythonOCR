class Item:
    
    def __init__(self,name,precio):
        self.name = name
        self.precio = precio
      
    def __str__(self):
        productoL = self.name + (" " * 50)
        productoL = productoL[:50]
        precioL = str(self.precio) + (" " * 10)
        precioL = precioL[:10]
        return "Producto: \t" + productoL + " Precio: \t" + precioL