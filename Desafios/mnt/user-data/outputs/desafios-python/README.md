# Desafíos de Python

Soluciones de la tarea de programación, una carpeta por desafío.

**Alumno:** Sergio Delgadillo Domínguez

| Carpeta | Desafío |
|---|---|
| `desafio_1_palindromos/` | Palíndromos |
| `desafio_2_histograma/` | Generador de histograma |

Cada carpeta tiene el cuaderno con la solución y su propio README con la explicación, ejemplos y cómo ejecutarlo.

# Desafío 2: Generador de histograma

Programa que recibe una lista de números y dibuja una barra de asteriscos por cada uno; la barra mide lo que vale el número.

**Archivo:** `desafio_2_histograma.ipynb`

## Solución

`pedir_numeros()` lee los datos (separados por espacios o comas) y los valida. `histograma()` imprime cada número con su barra (`'*' * n`) y alinea las etiquetas usando el ancho del número más grande. Los datos se guardan en una lista.

## Ejemplos

Con `3, 7, 1, 5`:

```
3 | ***
7 | *******
1 | *
5 | *****
```

Con números grandes (`120, 30, 75, 1`) las barras se escalan:

```
120 | **************************************************
 30 | ************
 75 | *******************************
  1 | *

Escala: cada * representa aprox. 2.4
```

## Robustez

- Se rechazan entradas vacías, texto que no sea número y números negativos, y se vuelve a pedir el dato.
- Si hay números muy grandes (más de 50), las barras se escalan para que quepan en pantalla y se imprime la escala usada.
- Un número positivo siempre muestra al menos un asterisco, aunque la escala lo reduzca.
- Una lista vacía no genera error: el programa avisa que la lista está vacía.

## Eficiencia

Recorre la lista una vez para encontrar el mayor y otra para imprimir, es decir, O(n). Cada barra se construye con una sola multiplicación de cadena y mide como máximo 50 caracteres.

## Cómo ejecutarlo

1. Abrir el cuaderno en Jupyter o Google Colab.
2. Ejecutar las celdas de arriba hacia abajo.
3. La última celda pide los números con `input()`.

Requiere Python 3. No usa librerías externas.