# Desafío 1: Palíndromos

Programa que recibe una frase y dice si es un palíndromo, ignorando espacios, puntuación, mayúsculas y acentos.

**Archivo:** `desafio_1_palindromos.ipynb`

## Solución

La función `limpiar()` quita los acentos (con `unicodedata`), deja solo letras y números y convierte todo a minúsculas. Después `es_palindromo()` compara el texto limpio con su reverso (`limpio[::-1]`).

## Ejemplos

| Entrada | Resultado |
|---|---|
| Anita lava la tina | Sí es palíndromo |
| Dábale arroz a la zorra el abad | Sí es palíndromo |
| Hola mundo | No es palíndromo |

## Robustez

- Si la entrada no tiene letras ni números, el programa lo avisa en lugar de dar un resultado falso.
- El cuaderno incluye casos de prueba con `assert`.

## Eficiencia

Recorre el texto una vez para limpiarlo y otra para compararlo, es decir, O(n).

## Cómo ejecutarlo

1. Abrir el cuaderno en Jupyter o Google Colab.
2. Ejecutar las celdas de arriba hacia abajo.
3. La última celda pide una frase con `input()`.

Requiere Python 3. No usa librerías externas.
