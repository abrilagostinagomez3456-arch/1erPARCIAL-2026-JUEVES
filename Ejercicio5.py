from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria="general"):
        self.descripcion = str(descripcion)
        self.id_producto = int(id_producto)
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = float(precio)
        self.stock = int(stock)
        self.categoria = categoria 
    
    def actualizar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = str(descripcion)
        if precio is not None:
            self.precio = float(precio)
        if stock is not None:
            self.stock = int(stock)

    def dias_para_expirar(self):
        hoy = date.today()
        dias = (self.fecha_vencimiento - hoy).days
        if dias <0:
            self.stock = 0 
            print(f"el producto '{self.descripcion}' ha expirado. el stock se marco como 0.")
            return 0 
        return dias

producto1 = productoKwikE("coca", 123, date(2026, 10, 15),1.50, 50)
print("dias para expirar:", producto1.dias_para_expirar())
producto1.actualizar_datos(precio=2.00, stock=45)