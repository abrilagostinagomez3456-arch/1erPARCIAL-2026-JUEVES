from datetime import date, timedelta
from Ejercicio6 import ProductoKwikE

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class IteradorListaEnlazada:
    def __init__(self, nodo_inicial):
        self.actual = nodo_inicial

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def __len__(self):
        return self.header._elem

    def is_empty(self):
        return self.header._elem == 0

    def append(self, dato):
        nuevo = Nodo(dato)
        if self.is_empty():
            self.header._nxt = nuevo
        else:
            actual = self.header._nxt
            while actual._nxt is not None:
                actual = actual._nxt
            actual._nxt = nuevo
        self.header._elem += 1

    def remove(self, dato):
        ant = self.header
        act = self.header._nxt
        while act is not None:
            if act._elem == dato:
                ant._nxt = act._nxt
                self.header._elem -= 1
                return True
            ant = act
            act = act._nxt
        raise ValueError("Elemento no encontrado")

    def __iter__(self):
        return IteradorListaEnlazada(self.header._nxt)

    def __str__(self):
        elementos = [str(elem) for elem in self]
        return "[" + ", ".join(elementos) + "]"

class KwikEMart:
    def __init__(self):
        self.bebidas = ListaEnlazada()
        self.snacks = ListaEnlazada()
        self.conveniencia = ListaEnlazada()
        self.pasillos = {
            "Bebidas": self.bebidas,
            "Snacks": self.snacks,
            "Conveniencia": self.conveniencia
        }

    def agregar_producto(self, pasillo, producto):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = ListaEnlazada()
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
            a_eliminar = ListaEnlazada()
            for prod in lista_productos:
                dias = (prod.fecha_vencimiento - hoy).days
                if dias <= 1:
                    a_eliminar.append(prod)
            for prod in a_eliminar:
                lista_productos.remove(prod)
                desechados += 1
        return desechados

mercado = KwikEMart()
p1 = ProductoKwikE("Squishee", 101, date.today() + timedelta(days=1), 2.50, 20)
p2 = ProductoKwikE("Donuts Glaseadas", 123, date.today() + timedelta(days=10), 1.50, 50)
mercado.agregar_producto("Bebidas", p1)
mercado.agregar_producto("Snacks", p2)
mercado.actualizar_stock(123, 60)
print("Productos desechados en 24hs:", mercado.desechar_por_expirar_24hs())