
# Pequeños Pasos

## 1. Descripción del proyecto

Pequeños Pasos es una aplicación desarrollada en Python para
gestionar productos de una tienda de artículos para bebés.
Permite organizar productos de ropa y alimentación, mostrar
su información y actualizar las cantidades disponibles.

## 2. Objetivos

- Aplicar los cuatro pilares de la Programación Orientada a Objetos.
- Organizar el código mediante clases y métodos.
- Validar los datos para evitar información incorrecta.
- Practicar el uso de Git y GitHub para controlar las versiones.

## 3. Funcionalidades

- Crear productos de ropa para bebés.
- Crear productos de alimentación para bebés.
- Mostrar un catálogo completo o resumido.
- Consultar el precio y el stock de los productos.
- Actualizar el stock con validaciones.
- Rechazar precios, cantidades y datos inválidos.

## 4. Conceptos de Programación Orientada a Objetos

### Abstracción
La clase abstracta `ProductoBebe` define una estructura común
para los productos de la tienda.

### Encapsulamiento
Los atributos `__precio` y `__stock` protegen la información
interna de los productos.

### Herencia
Las clases `RopaBebe` y `AlimentacionBebe` heredan de
`ProductoBebe`.

### Polimorfismo
Las subclases implementan su propia versión del método
`mostrar_detalle()` para presentar información específica.

## 5. Relaciones entre clases

- **Composición:** cada producto contiene un objeto `Categoria`.
- **Agrupación:** la clase `Inventario` mantiene una lista de productos.
- **Clases abstractas:** `ProductoBebe` utiliza el módulo `abc`.
- **Variables primitivas y objetos:** los productos combinan datos
  como nombre, precio y stock con objetos de la clase `Categoria`.

## 6. Tecnologías utilizadas

- Python 3.11
- Visual Studio Code
- Git
- GitHub

## 7. Archivo principal

`pequenos_pasos.py`

Este archivo contiene las clases, las validaciones y el programa
principal para demostrar el funcionamiento de la aplicación.
