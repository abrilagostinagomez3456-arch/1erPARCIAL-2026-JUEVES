from datetime import date, timedelta
from Ejercicio6 import ProductoKwikE
class KwikEMart:
    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []
        self.pasillos = {
            "Bebidas": self.bebidas,
            "Snacks": self.snacks,
            "conveniencia": self.conveniencia
        }
    
    def agregar_producto(self, pasillo, producto):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = []
        self.pasillos[pasillo].append(producto)

    def buscar_por_id(self, id_producto):
        for nombre_pasillo, lista_productos in self.pasillos.items():
            for prod in lista_productos:
                if prod.id_producto == id_producto:
                    return prod, lista_productos
        return None, None 

    def remover_producto(self, id_producto):
        prod, lista_productos = self.buscar_por_id(id_producto)
        if prod is not None:
            lista_productos.remove(prod)
            return True
        return False

    def actualizar_stock(self, id_producto, nuevo_stock):
        prod, _ = self.buscar_por_id(id_producto)
        if prod is not None:
            prod.actualizar_datos(stock=nuevo_stock)
            return True
        return False

    def desechar_por_expirar_24hs(self):
        hoy = date.today()
        desechados = 0
        for nombre_pasillo, lista_productos in self.pasillos.items():
            a_eliminar = []
            for prod in lista_productos:
                dias = (prod.fecha_vencimiento - hoy).days
                if dias <= 1:
                    a_eliminar.append(prod)
            for prod in a_eliminar:
                lista_productos.remove(prod)
                desechados += 1
        return desechados

mercado = KwikEMart()
p1 = ProductoKwikE("Papas", 101, date.today() + timedelta(days=1), 2.50, 20)
p2 = ProductoKwikE("Coca", 123, date.today() + timedelta(days=10), 1.50, 50)
mercado.agregar_producto("Bebidas", p1)
mercado.agregar_producto("Snacks", p2)
mercado.actualizar_stock(123, 60)
print("Productos desechados en 24hs:", mercado.desechar_por_expirar_24hs())
