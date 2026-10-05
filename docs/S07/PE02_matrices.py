"""Calcula EFI/EFE con ponderaciones académicas provisionales basadas en evidencia pública."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
SALIDAS = ROOT / "salidas"
SALIDAS.mkdir(exist_ok=True)

for nombre in ("efi", "efe"):
    matriz = pd.read_csv(ROOT / f"PE02_matriz_{nombre}.csv")
    assert abs(matriz["peso"].sum() - 1) < 1e-9
    assert matriz["calificacion"].between(1, 4).all()
    assert matriz["justificacion_peso"].fillna("").str.strip().ne("").all()
    matriz["ponderado"] = (matriz["peso"] * matriz["calificacion"]).round(4)
    total = matriz["ponderado"].sum()
    matriz.to_csv(SALIDAS / f"PE02_matriz_{nombre}_calculada.csv", index=False, encoding="utf-8-sig")
    print(f"MATRIZ {nombre.upper()}")
    print(matriz[["id", "peso", "calificacion", "ponderado"]].to_string(index=False))
    print(f"Suma de pesos: {matriz['peso'].sum():.2f}")
    print(f"Total ponderado: {total:.2f} (referencia académica 2.50)")
    print("Lectura provisional: revisar ratings con datos internos antes de concluir sobre Bitel.")
    print()

