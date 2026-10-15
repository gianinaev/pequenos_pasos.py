
from abc import ABC, abstractmethod


# COMPOSICIÓN:
# Cada producto contiene un objeto de la clase Categoria.
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


# ABSTRACCIÓN:
# Esta clase abstracta define la estructura común de los productos.
class ProductoBebe(ABC):
    def __init__(self, nombre, precio, stock=0, categoria=None):
        # Validación de datos para mejorar la calidad del software.
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo.")

        self.nombre = nombre
        self.__precio = precio  # ENCAPSULAMIENTO
        self.__stock = stock    # ENCAPSULAMIENTO

        self.categoria = categoria or Categoria("General")

    # Propiedad para consultar el precio de forma controlada.
    @property
    def precio(self):
        return self.__precio

    # Propiedad para consultar el stock.
    @property
    def stock(self):
        return self.__stock

    @abstractmethod
    def mostrar_detalle(self, formato="completo"):
        # Cada subclase debe implementar este método.
        pass

    def actualizar_stock(self, cantidad):
        nuevo_stock = self.__stock + cantidad

        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.__stock = nuevo_stock


# HERENCIA:
# RopaBebe hereda atributos y métodos de ProductoBebe.
class RopaBebe(ProductoBebe):
    def __init__(self, nombre, precio, talla, stock=0):
        super().__init__(
            nombre,
            precio,
            stock,
            Categoria("Ropa")
        )

        if not talla.strip():
            raise ValueError("La talla no puede estar vacía.")

        self.talla = talla

    # POLIMORFISMO:
    # Sobrescribe mostrar_detalle() con información de ropa.
    # El argumento formato permite dos presentaciones del método.
    def mostrar_detalle(self, formato="completo"):
        if formato == "corto":
            return f"{self.nombre} - ${self.precio:.2f}"

        return (
            f"ROPA: {self.nombre} | "
            f"Talla: {self.talla} | "
            f"Categoría: {self.categoria.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )


# HERENCIA Y POLIMORFISMO:
# AlimentacionBebe implementa su propia versión del método.
class AlimentacionBebe(ProductoBebe):
    def __init__(self, nombre, precio, edad_recomendada, stock=0):
        super().__init__(
            nombre,
            precio,
            stock,
            Categoria("Alimentación")
        )

        if not edad_recomendada.strip():
            raise ValueError(
                "La edad recomendada no puede estar vacía."
            )

        self.edad_recomendada = edad_recomendada

    def mostrar_detalle(self, formato="completo"):
        if formato == "corto":
            return f"{self.nombre} - ${self.precio:.2f}"

        return (
            f"ALIMENTACIÓN: {self.nombre} | "
            f"Edad recomendada: {self.edad_recomendada} | "
            f"Categoría: {self.categoria.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )


# AGRUPACIÓN:
# Inventario mantiene una lista de diferentes productos.
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if not isinstance(producto, ProductoBebe):
            raise TypeError(
                "Solo se pueden agregar productos para bebés."
            )

        self.productos.append(producto)

    # SIMULACIÓN DE SOBRECARGA:
    # Python permite cambiar el comportamiento mediante argumentos
    # por defecto, en lugar de definir varias versiones del método.
    def mostrar_catalogo(self, formato="completo"):
        print("\nCATÁLOGO PEQUEÑOS PASOS")
        print("-" * 55)

        for producto in self.productos:
            print(producto.mostrar_detalle(formato))


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    inventario = Inventario()

    # Variables primitivas y objetos de clases.
    nombre_ropa = "Pijama de algodón"
    precio_ropa = 18.99
    talla_ropa = "6-9 meses"
    stock_ropa = 15

    ropa = RopaBebe(
        nombre_ropa,
        precio_ropa,
        talla_ropa,
        stock_ropa
    )

    alimento = AlimentacionBebe(
        "Biberón",
        8.75,
        "0 meses en adelante",
        20
    )

    # Agrupación: se agregan objetos al inventario.
    inventario.agregar(ropa)
    inventario.agregar(alimento)

    # Polimorfismo: cada producto muestra sus propios detalles.
    inventario.mostrar_catalogo()

    # Argumento diferente: muestra el catálogo resumido.
    inventario.mostrar_catalogo("corto")

    # Actualización controlada del stock.
    ropa.actualizar_stock(5)
    print("\nStock actualizado:", ropa.stock)

    # Prueba de validación: el precio negativo debe rechazarse.
    try:
        RopaBebe("Pijama de prueba", -5, "3-6 meses", 2)
    except ValueError as error:
        print("\nValidación correcta:", error)

    # Prueba de validación: la talla vacía debe rechazarse.
    try:
        RopaBebe("Pijama de prueba", 10, "   ", 2)
    except ValueError as error:
        print("Validación correcta:", error)
