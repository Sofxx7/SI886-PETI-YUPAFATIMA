from pathlib import Path
import re

import matplotlib.pyplot as plt


EMPRESA = "Bitel Peru"
COMPETIDORES = ["Claro Peru", "Entel Peru", "Integratel Peru"]

MISION = (
    "Desarrollo para los peruanos y la sociedad: Bitel siempre trata de ser creativo "
    "y cambiarnos a nosotros mismos para contribuir a mejorar la calidad de vida de "
    "los peruanos y la sociedad. Asimismo, Bitel continua innovando, en conjunto con "
    "los clientes para crear productos y servicios que hacen la vida y trabajo facil."
)

VISION = (
    "Lider en telecomunicaciones y tecnologia de la informacion (TIC), fuerza principal "
    "para crear la sociedad digital. Bitel es pionero en desplegar tecnologia 4.0 y crear "
    "plataformas digitales para cada persona, la organizacion en conjunto contribuye y "
    "crea nuevos valores para el desarrollo del pais y los peruanos."
)

FUENTE = {
    "Direccion de la pagina": "https://bitel.com.pe/nosotros/history-of-bitel",
    "Fecha de consulta": "10 de septiembre de 2026",
    "Publica vision": "Si, en la misma pagina institucional",
    "Prueba de la decision": "No comprobable desde informacion publica",
}

COMPONENTES = {
    "Que hacemos": "crear productos y servicios",
    "Para quien": "los peruanos y la sociedad; los clientes",
    "Como nos distingue": "continua innovando, en conjunto con los clientes",
    "Para que": "contribuir a mejorar la calidad de vida; hacen la vida y trabajo facil",
    "Con que compromiso": "siempre trata de ser creativo y cambiarnos a nosotros mismos",
}

JUICIO_MISION = {
    "Intercambiable": (
        True,
        "Conserva sentido al atribuirla a Claro, Entel o Integratel; no contiene una capacidad exclusiva",
    ),
    "Contradice la practica": (
        False,
        "No existe evidencia publica suficiente para sostener una contradiccion general",
    ),
    "Escrita por una sola persona": (
        False,
        "El proceso de formulacion no es verificable desde la pagina publica",
    ),
}

JUICIO_VISION = {
    "Ambiciosa pero alcanzable": (
        False,
        "Bitel ocupa el segundo lugar por lineas activas, pero la declaracion no fija plazo ni meta",
    ),
    "Especifica del negocio": (
        True,
        "Menciona telecomunicaciones, TIC, tecnologia 4.0 y plataformas digitales",
    ),
    "Movilizadora": (
        False,
        "No permite determinar cuanto invertir ni que resultado cuantitativo priorizar",
    ),
}

ASPIRACIONAL = re.compile(
    r"\b(ser|seremos|convertirnos|liderar|lider\w*|numero uno|primera opcion|la mejor)\b",
    re.I,
)
VALORES = re.compile(
    r"\b(honestidad|respeto|integridad|excelencia|compromis\w+|innovacion|calidad total|trabajo en equipo|mejora continua|transparencia|responsabilidad)\b",
    re.I,
)
HORIZONTE = re.compile(r"(al\s+(ano\s+)?20\d{2}|en\s+20\d{2}|al cierre del horizonte|a\s+\w+\s+anos)", re.I)
METRICA = re.compile(r"\d+([.,]\d+)?\s*(%|por ciento|puntos|horas|dias|millones|mil)", re.I)


def diagnosticar():
    palabras_mision = len(MISION.split())
    palabras_vision = len(VISION.split())
    presentes = {k: v for k, v in COMPONENTES.items() if v}

    detectados = {
        "Intercambiable": JUICIO_MISION["Intercambiable"],
        "Confunde mision con vision": (
            False,
            "La expresion 'ser creativo' describe un compromiso presente, no una posicion futura",
        ),
        "Enumera valores": (
            len({m.group(0).lower() for m in VALORES.finditer(MISION)}) >= 3,
            "Tres o mas valores reemplazan la razon de ser",
        ),
        "Omite al destinatario": (
            COMPONENTES["Para quien"] is None,
            "No identifica a quien sirve",
        ),
        "Extension desmedida": (
            palabras_mision > 50,
            f"{palabras_mision} palabras; limite practico usado por el instrumento: 50",
        ),
        "Contradice la practica": JUICIO_MISION["Contradice la practica"],
        "Escrita por una sola persona": JUICIO_MISION["Escrita por una sola persona"],
    }

    hay_horizonte = bool(HORIZONTE.search(VISION))
    hay_metrica = bool(METRICA.search(VISION))
    atributos = {
        "Temporalmente acotada": (
            hay_horizonte,
            "Declara horizonte" if hay_horizonte else "No declara fecha ni horizonte",
        ),
        "Verificable": (
            hay_metrica,
            "Incluye cifra meta" if hay_metrica else "No incluye una cifra meta verificable",
        ),
        "Ambiciosa pero alcanzable": JUICIO_VISION["Ambiciosa pero alcanzable"],
        "Especifica del negocio": JUICIO_VISION["Especifica del negocio"],
        "Movilizadora": JUICIO_VISION["Movilizadora"],
    }

    print("=" * 78)
    print(f"DIAGNOSTICO DE LAS DECLARACIONES PUBLICADAS - {EMPRESA}")
    print("=" * 78)
    for clave, valor in FUENTE.items():
        print(f"{clave:30s}: {valor}")

    print(f"\nMISION - {palabras_mision} palabras")
    print(MISION)
    print("\nCinco componentes")
    for componente, cita in COMPONENTES.items():
        print(f"[{'SI' if cita else 'NO'}] {componente:22s} {cita or 'ausente'}")
    print(f"Resultado: {len(presentes)} de 5 componentes")

    print("\nSiete defectos")
    for defecto, (existe, prueba) in detectados.items():
        estado = "X" if existe else " "
        detalle = prueba if existe or defecto in {"Contradice la practica", "Escrita por una sola persona"} else ""
        print(f"[{estado}] {defecto:30s} {detalle}")

    print("\nPrueba de sustitucion")
    for competidor in COMPETIDORES:
        print(f"- {competidor}: la declaracion conserva sentido general")
    print("Resultado: FALLA la prueba de sustitucion")
    print("Prueba de la decision: NO COMPROBABLE desde informacion publica")
    print("Prueba del reconocimiento: NO COMPROBABLE sin consulta a trabajadores")
    print("VEREDICTO DE LA MISION: SE REFORMULA - falla la prueba de sustitucion")

    print(f"\nVISION - {palabras_vision} palabras")
    print(VISION)
    print("\nCinco atributos")
    for atributo, (cumple, prueba) in atributos.items():
        print(f"[{'SI' if cumple else 'NO'}] {atributo:28s} {prueba}")
    total_atributos = sum(1 for cumple, _ in atributos.values() if cumple)
    print(f"Resultado automatico conservador: {total_atributos} de 5 atributos")
    print("Revision cualitativa: verificable y alcanzable son PARCIALES, no logros completos")
    print("VEREDICTO DE LA VISION: SE REFORMULA - solo 1 de 5 atributos esta completo")

    return presentes, atributos


def graficar(presentes, atributos):
    destino = Path(__file__).resolve().parents[1] / "evidencias" / "S04" / "MV_diagnostico_declaraciones.png"
    destino.parent.mkdir(parents=True, exist_ok=True)

    componentes = list(COMPONENTES.keys())
    valores_mision = [1 if COMPONENTES[c] else 0 for c in componentes]
    nombres_atributos = list(atributos.keys())
    valores_vision = [1 if atributos[a][0] else 0 for a in nombres_atributos]

    fig, ejes = plt.subplots(1, 2, figsize=(12, 5.2))
    for eje, etiquetas, valores, titulo in [
        (ejes[0], componentes, valores_mision, "Mision: cinco componentes"),
        (ejes[1], nombres_atributos, valores_vision, "Vision: cinco atributos"),
    ]:
        etiquetas = etiquetas[::-1]
        valores = valores[::-1]
        eje.barh(etiquetas, valores, color=["#0F766E" if valor else "#B45309" for valor in valores])
        eje.set_xlim(0, 1)
        eje.set_xticks([0, 1], ["Ausente", "Presente"])
        eje.set_title(titulo, fontsize=11, fontweight="bold", color="#16285C")
        eje.grid(axis="x", alpha=0.2)
        eje.tick_params(labelsize=9)

    fig.suptitle(f"Diagnostico de las declaraciones vigentes - {EMPRESA}", fontsize=13, fontweight="bold")
    fig.text(0.5, 0.01, "Fuente: Bitel Peru. Evaluacion conforme a la teoria del Taller 04 de SI-886.", ha="center", fontsize=8)
    plt.tight_layout(rect=(0, 0.04, 1, 0.94))
    plt.savefig(destino, dpi=180, bbox_inches="tight")
    print(f"\nGrafico generado: {destino.as_posix()}")


if __name__ == "__main__":
    componentes_presentes, atributos_evaluados = diagnosticar()
    graficar(componentes_presentes, atributos_evaluados)
