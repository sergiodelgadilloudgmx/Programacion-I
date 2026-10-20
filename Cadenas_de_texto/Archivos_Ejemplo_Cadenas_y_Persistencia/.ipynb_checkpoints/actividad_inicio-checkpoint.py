"""Completa los TODO conforme a las reglas del documento Word."""
from pathlib import Path
import json
BASE = Path(__file__).resolve().parent
ENTRADA = BASE / "datos" / "solicitudes.txt"
SALIDA = BASE / "salidas"

def normalizar_categoria(texto):
    # TODO: strip, lower, sustituir guiones/guiones bajos y unir palabras.
    raise NotImplementedError("Completa normalizar_categoria")

def validar_campos(campos, ids_vistos):
    # TODO: regresar (registro_limpio, motivo).
    # Un rechazo devuelve (None, motivo); uno válido devuelve (registro, None).
    raise NotImplementedError("Completa validar_campos")

def main():
    # TODO: crear SALIDA; abrir entrada con with y encoding='utf-8'.
    # TODO: verificar encabezado; iterar con número de línea; contar vacías.
    # TODO: validar sin modificar el archivo fuente y escribir rechazos.
    # TODO: producir solicitudes_limpias.txt, resumen.json y ejecuciones.log.
    # TODO: reabrir salidas, verificar conteos y capturar FileNotFoundError.
    raise NotImplementedError("Completa el flujo principal")

if __name__ == "__main__":
    main()
