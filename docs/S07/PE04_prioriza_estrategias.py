"""Aplica los bonos de priorización especificados en la guía del Taller 07."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
estrategias = pd.read_csv(ROOT / "PE03_foda_cruzado.csv")
pesos = {}
for nombre in ("efi", "efe"):
    matriz = pd.read_csv(ROOT / f"PE02_matriz_{nombre}.csv")
    pesos.update(dict(zip(matriz["id"], matriz["peso"])))
bono = {"DA": 1.35, "FA": 1.20, "DO": 1.10, "FO": 1.00}

def sumar_pesos(cruce):
    codigos = [x.strip() for x in cruce.split("+")]
    faltantes = [x for x in codigos if x not in pesos]
    assert not faltantes, f"Factor sin peso: {faltantes}"
    return sum(pesos[x] for x in codigos)

estrategias["peso_factores"] = estrategias["factores_cruzados"].map(sumar_pesos)
estrategias["bono"] = estrategias["tipo"].map(bono)
estrategias["puntaje"] = (estrategias["peso_factores"] * estrategias["bono"]).round(4)
estrategias = estrategias.sort_values(["puntaje", "id"], ascending=[False, True])
estrategias.to_csv(ROOT / "PE04_estrategias_priorizadas.csv", index=False, encoding="utf-8-sig")
print(estrategias[["id", "tipo", "factores_cruzados", "peso_factores", "bono", "puntaje", "proyecto_candidato"]].to_string(index=False))
print("\nDistribución por tipo:")
print(estrategias["tipo"].value_counts().sort_index().to_string())
print("\nLos puntajes usan pesos académicos provisionales; validarlos con evidencia interna.")

