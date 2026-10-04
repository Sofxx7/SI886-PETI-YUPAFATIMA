"""Calcula EFI y EFE con los pesos revisados del caso académico S07.

Adaptación de la herramienta PE02_matrices.py de Oscar Jiménez Flores,
repositorio del curso PETI, HERRAMIENTAS/SEMANA-07. Las ponderaciones,
calificaciones y justificaciones son propuestas académicas para este caso.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
SALIDAS = ROOT / "salidas"
SALIDAS.mkdir(exist_ok=True)

for nombre in ("efi", "efe"):
    ruta = ROOT / f"PE02_matriz_{nombre}.csv"
    matriz = pd.read_csv(ruta)
    assert abs(matriz["peso"].sum() - 1) < 1e-9, (
        f"Los pesos de {nombre.upper()} deben sumar 1; suman {matriz['peso'].sum():.6f}"
    )
    assert matriz["calificacion"].between(1, 4).all()
    assert matriz["justificacion_peso"].fillna("").str.strip().ne("").all()
    matriz["ponderado"] = (matriz["peso"] * matriz["calificacion"]).round(4)
    total = matriz["ponderado"].sum()
    matriz.to_csv(SALIDAS / f"PE02_matriz_{nombre}_calculada.csv", index=False, encoding="utf-8-sig")
    print(f"MATRIZ {nombre.upper()}")
    print(matriz[["id", "peso", "calificacion", "ponderado"]].to_string(index=False))
    print(f"Suma de pesos: {matriz['peso'].sum():.2f}")
    print(f"Total ponderado: {total:.2f} (referencia 2.50)")
    if nombre == "efi":
        print("Lectura: posición interna débil; las debilidades documentadas pesan más.")
    else:
        print("Lectura: respuesta externa no demostrada; ratings miden respuesta evidenciada, no gravedad.")
    print()

