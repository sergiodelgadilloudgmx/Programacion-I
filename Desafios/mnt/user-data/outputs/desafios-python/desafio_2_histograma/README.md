# Desafío 2: Generador de histograma

Programa que recibe una lista de números y dibuja una barra de asteriscos por cada uno; la barra mide lo que vale el número.

**Archivo:** `desafio_2_histograma.ipynb`

## Solución

`pedir_numeros()` lee los datos (separados por espacios o comas) y los valida. `histograma()` imprime cada número con su barra (`'*' * n`) y alinea las etiquetas. Los datos se guardan en una lista.

Ejemplo con `3, 7, 1, 5`:

```
3 | ***
7 | *******
1 | *
5 | *****
```

## Robustez

- Se rechazan entradas vacías, texto que no sea número y números negativos, y se vuelve a pedir el dato.
- Si hay números muy grandes (más de 50), las barras se escalan para que quepan en pantalla y se imprime la escala usada.
- Una lista vacía no genera error.

## Eficiencia

Recorre la lista una vez, y cada barra se construye con una sola multiplicación de cadena.

## Cómo ejecutarlo

1. Abrir el cuaderno en Jupyter o Google Colab.
2. Ejecutar las celdas de arriba hacia abajo.
3. La última celda pide los números con `input()`.

Requiere Python 3. No usa librerías externas.
