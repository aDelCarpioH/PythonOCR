import cv2 
import pytesseract
import re

def imprimirLinea(productoI, precioI):
    productoL = productoI + (" " * 50)
    productoL = productoL[:50]
    precioL = str(precioI) + (" " * 10)
    precioL = precioL[:10]
    print("Producto: \t",productoL, " Precio: \t",precioL)
    

img = cv2.imread('Boleta2.png')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
lista = re.split('\n',pytesseract.image_to_string(img, config=custom_config))

# print(len(lista))
total = 0.00
cantidad = 0

descartados = []

for linea in lista:
    if "$" in linea and " C" in linea:
        lineaSplit = linea.split("$")
        producto = lineaSplit[0]
        precio = float(lineaSplit[1].split(" ")[0])
        total += precio
        cantidad += 1
        imprimirLinea(producto,precio)
    else:
        descartados.append(linea)
print("\nTotal: ", total)
print("Cantidad:",cantidad)

print("\n")
for linea in descartados:
    print(linea)