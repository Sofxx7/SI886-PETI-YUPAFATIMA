"""Controles de cierre solicitados por el Taller 07."""
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
assert len(pestel) >= 6 and pestel["decision_que_obliga"].fillna("").str.strip().ne("").all()
assert abs(efi["peso"].sum() - 1) < 1e-9
assert abs(efe["peso"].sum() - 1) < 1e-9
assert len(foda) >= 12 and foda["id"].nunique() == len(foda)
assert foda["tipo"].value_counts().to_dict() == {"FO": 3, "FA": 3, "DO": 3, "DA": 3}
assert len(trazabilidad) >= 12
assert set(foda["id"]) == set(priorizadas["id"])
assert abs(efi.assign(p=efi.peso * efi.calificacion).p.sum() - 1.50) < 1e-9
assert abs(efe.assign(p=efe.peso * efe.calificacion).p.sum() - 1.14) < 1e-9
assert priorizadas.iloc[0]["id"] == "E-12"

lines = [
    "VALIDACIÓN DEL TALLER 07 · 4 de octubre de 2026",
    f"PESTEL: {len(pestel)} factores; {len(dimensiones)} dimensiones; todas las decisiones están especificadas.",
    f"EFI: suma de pesos {efi.peso.sum():.2f}; total ponderado {((efi.peso * efi.calificacion).sum()):.2f} frente a 2.50.",
    f"EFE: suma de pesos {efe.peso.sum():.2f}; total ponderado {((efe.peso * efe.calificacion).sum()):.2f} frente a 2.50.",
    f"FODA: {len(foda)} estrategias; distribución {', '.join(f'{k}={v}' for k, v in sorted(foda.tipo.value_counts().to_dict().items()))}.",
    f"Priorización: {len(priorizadas)} estrategias; mayor puntaje {priorizadas.iloc[0]['id']} = {priorizadas.iloc[0]['puntaje']:.4f}.",
    f"Trazabilidad: {len(trazabilidad)} filas.",
    "Resultado: controles de la guía satisfechos; ratings EFE A3/A4 son provisionales por falta de evidencia interna.",
]
out = root / "salidas" / "validacion.txt"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))

