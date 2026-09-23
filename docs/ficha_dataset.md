# Ficha del dataset

- **Dominio:** Salud — hepatología (enfermedad hepática)
- **Unidad de análisis:** cada fila representa un paciente, caracterizado por
  su edad, género y 8 marcadores bioquímicos de una prueba de sangre.
- **Decisión que apoya:** identificar pacientes con probable enfermedad
  hepática que ameritan estudios adicionales (ecografía, biopsia).
- **Target tentativo:** `Selector` — variable binaria (1 = paciente con
  enfermedad hepática, 2 = paciente sin enfermedad hepática).
- **Tipo de tarea:** clasificación binaria.
- **Error más costoso:** falso negativo — clasificar como "sano" a un
  paciente que en realidad tiene enfermedad hepática, retrasando su
  diagnóstico y tratamiento.
- **Usuario de la solución:** personal clínico o de laboratorio que
  necesita priorizar qué pacientes requieren seguimiento adicional.

## Fuente y procedencia

- **Nombre:** ILPD (Indian Liver Patient Dataset)
- **Repositorio:** UCI Machine Learning Repository (dataset id 225)
- **Página de documentación:** https://archive.ics.uci.edu/dataset/225
- **URL de descarga directa:** https://archive.ics.uci.edu/ml/machine-learning-databases/00225/Indian%20Liver%20Patient%20Dataset%20(ILPD).csv
- **Autor(es):** Bendi Ramana, N. Venkateswarlu (donado 2012)
- **Licencia:** uso académico permitido, citando la política de UCI
- **Tamaño:** 583 filas, 10 columnas (sin encabezado en el archivo crudo)

## Comparación de candidatos

| Criterio | Candidato A — ILPD (elegido) | Candidato B — Pima Diabetes |
|---|---|---|
| Procedencia | UCI ML Repository (id 225) | UCI ML Repository / OpenML (id 37) |
| Licencia | Uso académico con cita | Dominio público / uso académico |
| Filas/columnas | 583 filas, 10 columnas | 768 filas, 9 columnas |
| Target y clases | `Selector`, 2 clases (416 / 167) | `class`, 2 clases (500 / 268) |
| Ausentes | Pocos (A/G Ratio) | Ninguno reportado |
| Riesgo de fuga | Bajo | Bajo |
| Variables categóricas | Sí — Género | Ninguna (100% numérico) |

**Justificación de la elección:** se seleccionó el Candidato A porque, además
de cumplir los criterios de aceptación (>500 filas, target binario, uso
académico permitido), incluye una variable categórica (Género), lo que
permite ejercitar el preprocesamiento completo (imputación + codificación
one-hot) requerido por este laboratorio.