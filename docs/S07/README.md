# Taller 07 · análisis público de Bitel

Guía: https://github.com/OscarJimenezFlores/PETI/blob/main/SEMANA-07/3-TALLER.md

## Alcance y limitaciones

Se desarrolla el Taller 07 como continuación del PETI de Bitel. No se encontraron las secciones previas 1.1, 3.1 y 3.2 requeridas por la guía. La evidencia de entorno procede de fuentes públicas. Los puntajes EFI/EFE y las brechas internas son hipótesis académicas provisionales: no constituyen auditoría ni prueban fallas o incumplimiento. Las cifras agregadas del MTC para contratos 5G no se atribuyen íntegramente a Bitel; falta revisar su contrato específico.

## Artefactos

- PE01_pestel.csv: ocho factores en seis dimensiones, con evidencia, fuente, efecto, intensidad, horizonte y decisión.
- PE02_matriz_efi.csv y PE02_matriz_efe.csv: pesos justificados y ratings provisionales.
- PE02_matrices.py: cálculos reproducibles EFI/EFE.
- PE03_foda_cruzado.csv: doce estrategias, tres por cuadrante, con códigos, objetivos y proyectos.
- PE04_prioriza_estrategias.py y PE04_estrategias_priorizadas.csv: fórmula de la guía y salida.
- PE05_trazabilidad.csv: 24 filas, con ambos factores de cada estrategia vinculados a evidencia.
- docs/S07/3.3-3.5.md: redacción PETI y referencias.
- anexo_C_foda_cruzado.png y .svg: figura FODA.
- validar_entrega.py: controles mecánicos de aritmética y estructura. No valida el sentido de los supuestos.

Con Python y pandas, ejecutar PE02_matrices.py y PE04_prioriza_estrategias.py en este directorio. La validación semántica de ratings y debilidades requiere los insumos internos que faltan.

