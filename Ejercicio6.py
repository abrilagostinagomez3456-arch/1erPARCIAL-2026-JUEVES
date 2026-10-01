from datetime import date
from Ejercicio5 import ProductoKwikE
class ProductoKwikE(ProductoKwikE):
    def __str__(self):
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __eq__(self, otro):
        if isinstance(otro, ProductoKwikE):
            return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion
        return False 

p1 = ProductoKwikE("coca", 123, date(2026, 10, 15), 1.50, 50)
p2 = ProductoKwikE("coca", 123, date(2026, 10, 20), 2.00, 30)
print(p1)
print(p1 == p2)