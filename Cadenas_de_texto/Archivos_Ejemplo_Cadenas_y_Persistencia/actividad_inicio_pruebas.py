"""Completa los TODO conforme a las reglas del documento Word."""
from pathlib import Path
import json
from datetime import datetime

BASE = Path(__file__).resolve().parent
#ENTRADA = BASE / "datos" / "solicitudes_copia_prueba.txt"
ENTRADA = BASE / "datos" / "solicitudes.txt"
SALIDA = BASE / "salidas"

def normalizar_categoria(texto):
    # TODO: strip, lower, sustituir guiones/guiones bajos y unir palabras.
    #raise NotImplementedError("Completa normalizar_categoria")
    """
    Normaliza la categoría:
    - strip()
    - lower()
    - reemplaza '-' y '_' por espacios
    - une con guion bajo
    """
    limpio = texto.strip().lower().replace("-", " ").replace("_", " ")
    return "_".join(limpio.split())

def normalizar_descripcion(texto):
    """
    Quita espacios extremos y reduce los espacios internos a uno solo.
    """
    return " ".join(texto.strip().split())


def validar_campos(campos, ids_vistos):
    # TODO: regresar (registro_limpio, motivo).
    # Un rechazo devuelve (None, motivo); uno válido devuelve (registro, None).
    #raise NotImplementedError("Completa validar_campos")
    """
    Recibe [id, correo, categoria, descripcion]
    Regresa (registro_limpio, None) o (None, motivo)
    """
    if len(campos) != 4:
        return None, "Número incorrecto de campos"

    id_raw, correo_raw, cat_raw, desc_raw = campos

    id_norm = id_raw.strip()
    correo_norm = correo_raw.strip()
    cat_norm = normalizar_categoria(cat_raw)
    desc_norm = normalizar_descripcion(desc_raw)

    if not id_norm:
        return None, "ID vacío"
    if id_norm in ids_vistos:
        return None, "ID duplicado"
    if "@" not in correo_norm or correo_norm.count("@") != 1:
        return None, "Correo inválido"
    if not cat_norm:
        return None, "Categoría vacía"
    if not desc_norm:
        return None, "Descripción vacía"

    ids_vistos.add(id_norm)
    registro = f"{id_norm}|{correo_norm}|{cat_norm}|{desc_norm}"
    return registro, None


def main():
    # TODO: crear SALIDA; abrir entrada con with y encoding='utf-8'.
    # TODO: verificar encabezado; iterar con número de línea; contar vacías.
    # TODO: validar sin modificar el archivo fuente y escribir rechazos.
    # TODO: producir solicitudes_limpias.txt, resumen.json y ejecuciones.log.
    # TODO: reabrir salidas, verificar conteos y capturar FileNotFoundError.
    #raise NotImplementedError("Completa el flujo principal")
    try:
        SALIDA.mkdir(exist_ok=True)

        # Apertura de entrada con with y encoding
        with ENTRADA.open(encoding="utf-8") as entrada:
            # 1. Verificar encabezado exacto
            encabezado = entrada.readline().rstrip("\n")
            esperado = "id|correo|categoria|descripcion"
            if encabezado != esperado:
                print("Encabezado incorrecto.")
                print("Encontrado:", encabezado)
                print("Esperado :", esperado)
                return

            # Preparar salidas (Etapa 4)
            limpias_path = SALIDA / "solicitudes_limpias.txt"
            rechazos_path = SALIDA / "rechazos.jsonl"

            with limpias_path.open("w", encoding="utf-8") as limpias, \
                 rechazos_path.open("w", encoding="utf-8") as rechazos:

                limpias.write(encabezado + "\n")

                total = 0
                validos = 0
                rechazados = 0
                categorias = {}
                ids_vistos = set()

                # 2. Iteración línea por línea (sin read/readlines)
                for num, linea in enumerate(entrada, start=2):
                    texto_original = linea.rstrip("\n")
                    total += 1

                    if not texto_original.strip():
                        rechazados += 1
                        rej = {
                            "linea": num,
                            "motivo": "Línea vacía",
                            "texto_original": texto_original
                        }
                        rechazos.write(json.dumps(rej, ensure_ascii=False) + "\n")
                        continue

                    campos = texto_original.split("|")
                    registro, motivo = validar_campos(campos, ids_vistos)

                    if registro:
                        limpias.write(registro + "\n")
                        validos += 1
                        cat = registro.split("|")[2]
                        categorias[cat] = categorias.get(cat, 0) + 1
                    else:
                        rechazados += 1
                        rej = {
                            "linea": num,
                            "motivo": motivo,
                            "texto_original": texto_original
                        }
                        rechazos.write(json.dumps(rej, ensure_ascii=False) + "\n")

        # resumen.json
        resumen = {
            "total": total,
            "validos": validos,
            "rechazados": rechazados,
            "por_categoria": categorias
        }

        resumen_path = SALIDA / "resumen.json"
        with resumen_path.open("w", encoding="utf-8") as f:
            json.dump(resumen, f, ensure_ascii=False, indent=2)

        # ejecuciones.log (fecha, hora, nombre de entrada, conteos)
        log_path = SALIDA / "ejecuciones.log"
        ahora = datetime.now().isoformat(timespec="seconds")
        with log_path.open("a", encoding="utf-8") as log:
            log.write(
                f"{ahora} | entrada={ENTRADA.name} | "
                f"total={total} | validos={validos} | rechazados={rechazados}\n"
            )

        # Reabrir y verificar persistencia
        with limpias_path.open(encoding="utf-8") as f:
            registros_limpios = len(f.readlines()) - 1  # sin cabecera

        with resumen_path.open(encoding="utf-8") as f:
            resumen_cargado = json.load(f)

        with rechazos_path.open(encoding="utf-8") as f:
            for linea in f:
                json.loads(linea)  # valida que cada línea sea JSON

        assert resumen_cargado["total"] == resumen_cargado["validos"] + resumen_cargado["rechazados"]
        assert sum(resumen_cargado["por_categoria"].values()) == resumen_cargado["validos"]
        assert registros_limpios == resumen_cargado["validos"]

        print("Depuración completada.")
        print("Resumen:", resumen)

    except FileNotFoundError as e:
        print("Archivo no encontrado:", e.filename)

if __name__ == "__main__":
    main()
