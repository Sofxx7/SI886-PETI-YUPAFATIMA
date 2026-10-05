from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
df = pd.read_csv(root / "PE03_foda_cruzado.csv")
short = {
    "E-01": "Compromisos de despliegue 5G",
    "E-02": "Demanda y observabilidad de red",
    "E-03": "Atención digital multilingüe",
    "E-04": "Experiencia, calidad y retención",
    "E-05": "Privacidad en servicios 5G",
    "E-06": "Respuesta y solución de reclamos",
    "E-07": "Hoja de ruta 2026-2030",
    "E-08": "Capacidad y disponibilidad digital",
    "E-09": "Accesibilidad por región e idioma",
    "E-10": "Propuesta de valor diferenciada",
    "E-11": "Gobierno de privacidad",
    "E-12": "Trazabilidad de activos y RAEE",
}
styles = {"FO":"#e9f4ea","FA":"#fff4dd","DO":"#e8f2fc","DA":"#fbe9e7"}
positions = {"FO":(0,0),"FA":(0,1),"DO":(1,0),"DA":(1,1)}
titles = {"FO":"FO · Fortalezas + oportunidades","FA":"FA · Fortalezas + amenazas","DO":"DO · Debilidades + oportunidades","DA":"DA · Debilidades + amenazas"}
fig, axes = plt.subplots(2,2,figsize=(14,9))
for tipo,(r,c) in positions.items():
    ax=axes[r,c]
    ax.set_facecolor(styles[tipo])
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color("#394b59"); spine.set_linewidth(1.4)
    ax.set_title(titles[tipo],fontsize=13,fontweight="bold",pad=12)
    subset=df[df.tipo==tipo]
    lines=[f"{row.id} [{row.factores_cruzados}]\n{short[row.id]}\n→ {row.proyecto_candidato}" for row in subset.itertuples()]
    ax.text(0.04,0.92,"\n\n".join(lines),va="top",ha="left",fontsize=9.7,linespacing=1.15,wrap=True,transform=ax.transAxes)
fig.suptitle("Bitel · Matriz FODA cruzada · 12 estrategias propuestas",fontsize=16,fontweight="bold",y=0.98)
fig.text(0.5,0.02,"Basada en evidencia pública; calificaciones EFI/EFE provisionales por falta de insumos internos.",ha="center",fontsize=9)
fig.tight_layout(rect=(0.025,0.05,0.98,0.95),h_pad=2.0,w_pad=1.6)
fig.savefig(root/"anexo_C_foda_cruzado.png",dpi=180,bbox_inches="tight")
fig.savefig(root/"anexo_C_foda_cruzado.svg",bbox_inches="tight")

