# Taller 07 · evidencia

Rama de trabajo: `taller-07-caso02` · base `develop`.  
Guía del curso: https://github.com/OscarJimenezFlores/PETI/blob/main/SEMANA-07/3-TALLER.md

## Confidencialidad y alcance

El informe académico completo se clasifica **CONFIDENCIAL**. Este repositorio es público: por ello se omite el nombre de la organización y se exponen solo factores agregados necesarios para comprobar el ejercicio. No se incluyen nombres de pacientes, historias, credenciales, direcciones, configuraciones ni información clínica individual. El conteo de incidentes es el dato agregado que contiene el caso académico. La propuesta no es una auditoría ni confirma el cumplimiento real de la organización.

## Artefactos

- `PE01_pestel.csv`: ocho factores PESTEL con fuente, evidencia, efecto, intensidad, horizonte y decisión.
- `PE02_matriz_efi.csv`, `PE02_matriz_efe.csv`: factores, pesos, rating y justificación.
- `PE02_matrices.py`: cálculo EFI/EFE, validación de pesos y totales.
- `salidas/PE02_matriz_efi_calculada.csv`, `salidas/PE02_matriz_efe_calculada.csv`: cálculos reproducibles.
- `PE03_foda_cruzado.csv`: doce estrategias, tres por cuadrante.
- `PE04_prioriza_estrategias.py`, `PE04_estrategias_priorizadas.csv`: fórmula y salida de priorización de la guía.
- `PE05_trazabilidad.csv`: doce filas de evidencia a proyecto.
- `validar_entrega.py`: comprobaciones de cierre requeridas por la guía.
- `3.3-3.5.md`: redacción de las secciones del PETI y fuentes.
- `anexo_C_foda_cruzado.svg`: matriz FODA para lectura rápida (el informe PDF incorpora la imagen PNG).
- `salidas/validacion.txt`: evidencia de sumas, resultados y conteos comprobados.

## Reproducción

Requiere Python 3.11 o superior y `pandas`. Ejecutar en este directorio:

```text
python PE02_matrices.py
python PE04_prioriza_estrategias.py
python validar_entrega.py
```

Los ratings EFE valoran la respuesta acreditada en el caso, no la severidad del evento. A3 y A4 son provisionales donde no hay evidencia interna. El PESTEL usa estadísticas nacionales como contexto y no las atribuye a los pacientes particulares del caso.

