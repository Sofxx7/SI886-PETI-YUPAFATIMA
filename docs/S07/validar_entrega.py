"""Comprueba aritmética y estructura; no valida la interpretación semántica de las fuentes."""
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent
pestel = pd.read_csv(root / "PE01_pestel.csv")
efi = pd.read_csv(root / "PE02_matriz_efi.csv")
efe = pd.read_csv(root / "PE02_matriz_efe.csv")
foda = pd.read_csv(root / "PE03_foda_cruzado.csv")
priorizadas = pd.read_csv(root / "PE04_estrategias_priorizadas.csv")
trazabilidad = pd.read_csv(root / "PE05_trazabilidad.csv")
dimensiones = {"Político", "Económico", "Social", "Tecnológico", "Ecológico/Ético", "Legal"}

assert set(pestel["dimension"]) == dimensiones
assert len(pestel) == 8
assert pestel["decision_que_obliga"].fillna("").str.strip().ne("").all()
assert pestel["fuente_url"].fillna("").str.startswith("http").all()
assert abs(efi["peso"].sum() - 1) < 1e-9
assert abs(efe["peso"].sum() - 1) < 1e-9
assert efi["calificacion"].between(1, 4).all() and efe["calificacion"].between(1, 4).all()
assert len(foda) == 12 and foda["id"].nunique() == 12
assert foda["tipo"].value_counts().to_dict() == {"FO": 3, "FA": 3, "DO": 3, "DA": 3}
assert len(trazabilidad) == 24
assert trazabilidad.groupby("estrategia")["factor"].nunique().eq(2).all()
assert set(foda["id"]) == set(priorizadas["id"])
assert abs((efi.peso * efi.calificacion).sum() - 2.46) < 1e-9
assert abs((efe.peso * efe.calificacion).sum() - 2.49) < 1e-9
assert priorizadas.iloc[0]["id"] == "E-10"
assert abs(priorizadas.iloc[0]["puntaje"] - 0.378) < 1e-9

lines = [
    "TALLER 07 · comprobación aritmética y estructural",
    f"PESTEL: {len(pestel)} factores; {len(dimensiones)} dimensiones; fuentes y decisiones registradas.",
    f"EFI: pesos {efi.peso.sum():.2f}; total {((efi.peso * efi.calificacion).sum()):.2f} frente a 2.50.",
    f"EFE: pesos {efe.peso.sum():.2f}; total {((efe.peso * efe.calificacion).sum()):.2f} frente a 2.50.",
    f"FODA: {len(foda)} estrategias; " + ", ".join(f"{k}={v}" for k,v in sorted(foda.tipo.value_counts().to_dict().items())),
    f"Prioridad mayor: {priorizadas.iloc[0]['id']} = {priorizadas.iloc[0]['puntaje']:.4f}.",
    f"Trazabilidad: {len(trazabilidad)} filas; dos factores por estrategia.",
    "Nota: estas comprobaciones no validan supuestos internos; ratings y brechas son provisionales por falta de PETI 3.1/3.2.",
]
out = root / "salidas" / "validacion.txt"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))

