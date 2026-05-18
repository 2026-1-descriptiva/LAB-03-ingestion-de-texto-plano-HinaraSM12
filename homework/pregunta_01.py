"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    rows = []
    current_row = None

    for line in lines:
        line = line.rstrip()

        if not line.strip():
            continue

        parts = line.split()

        if parts[0].isdigit():
            if current_row is not None:
                rows.append(current_row)

            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje = float(parts[2].replace(",", "."))

            # Se usa parts[4:] para saltar el símbolo %
            palabras = " ".join(parts[4:]).strip()

            current_row = [
                cluster,
                cantidad,
                porcentaje,
                palabras,
            ]

        elif current_row is not None:
            texto = line.strip()
            if texto:
                current_row[3] += " " + texto

    if current_row is not None:
        rows.append(current_row)

    df = pd.DataFrame(
        rows,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )

    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)
        .str.replace(r"\s*,\s*", ", ", regex=True)
        .str.strip()
        .str.rstrip(".")
    )

    return df