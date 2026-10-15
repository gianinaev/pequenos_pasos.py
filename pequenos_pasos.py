
from abc import ABC, abstractmethod


# Composición: cada producto tiene un objeto Categoria.
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


# Abstracción: define la estructura común de los productos.
class ProductoBebe(ABC):
    def __init__(self, nombre, precio, stock=0, categoria=None):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo.")

        self.nombre = nombre
        self.__precio = precio  # Encapsulamiento
        self.__stock = stock    # Encapsulamiento
        self.categoria = categoria or Categoria("General")

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @abstractmethod
    def mostrar_detalle(self, formato="completo"):
        """Cada subclase debe mostrar sus propios detalles."""
        pass

    def actualizar_stock(self, cantidad):
        nuevo_stock = self.__stock + cantidad

        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.__stock = nuevo_stock


# Herencia: RopaBebe reutiliza las características del producto base.
class RopaBebe(ProductoBebe):
    def __init__(self, nombre, precio, talla, stock=0):
        super().__init__(
            nombre, precio, stock, Categoria("Ropa")
        )
        self.talla = talla

    # Polimorfismo: sobrescribe el método de la clase abstracta.
    # El argumento formato permite dos presentaciones del mismo método.
    def mostrar_detalle(self, formato="completo"):
        if formato == "corto":
            return f"{self.nombre} - ${self.precio:.2f}"

        return (
            f"ROPA: {self.nombre} | Talla: {self.talla} | "
            f"Categoría: {self.categoria.nombre} | "
            f"Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )


# Herencia y polimorfismo: implementa su propia versión del método.
class AlimentacionBebe(ProductoBebe):
    def __init__(self, nombre, precio, edad_recomendada, stock=0):
        super().__init__(
            nombre, precio, stock, Categoria("Alimentación")
        )
        self.edad_recomendada = edad_recomendada

    def mostrar_detalle(self, formato="completo"):
        if formato == "corto":
            return f"{self.nombre} - ${self.precio:.2f}"

        return (
            f"ALIMENTACIÓN: {self.nombre} | "
            f"Edad recomendada: {self.edad_recomendada} | "
            f"Categoría: {self.categoria.nombre} | "
            f"Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )


# Agrupación: Inventario administra una colección de productos.
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if not isinstance(producto, ProductoBebe):
            raise TypeError("Solo se pueden agregar productos para bebés.")

        self.productos.append(producto)

    # Argumento por defecto: simula sobrecarga de métodos.
    # Se utiliza el mismo método con formato completo o corto.
    def mostrar_catalogo(self, formato="completo"):
        print("\nCATÁLOGO PEQUEÑOS PASOS")
        print("-" * 55)

        for producto in self.productos:
            print(producto.mostrar_detalle(formato))


# Programa principal
if __name__ == "__main__":
    inventario = Inventario()

    ropa = RopaBebe("Pijama de algodón", 18.99, "6-9 meses", 15)
    alimento = AlimentacionBebe(
        "Biberón", 8.75, "0 meses en adelante", 20
    )

    inventario.agregar(ropa)
    inventario.agregar(alimento)

    # Polimorfismo: cada objeto presenta sus propios detalles.
    inventario.mostrar_catalogo()

    # Simulación de sobrecarga mediante un argumento por defecto.
    inventario.mostrar_catalogo("corto")

    # Actualización del stock con validación.
    ropa.actualizar_stock(5)
    print("\nStock actualizado:", ropa.stock)

    # Prueba de la validación de datos.
    try:
        ProductoPrueba = RopaBebe("Pijama", -5, "3-6 meses", 2)
    except ValueError as error:
        print("\nValidación correcta:", error)
