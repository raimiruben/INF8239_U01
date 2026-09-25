# INF8239_U01 — Ciencia de Datos II

Proyecto reproducible para la Unidad 01 (Modelos avanzados, reducción
dimensional y Green AI), asignatura INF-8239 Ciencia de Datos II, UASD.

## Sistema operativo

Windows 11

## Herramientas utilizadas

- Python 3.13.7
- Git 2.55.0.windows.5
- Visual Studio Code (extensiones: Python, Jupyter, Pylance, Ruff)

## Estructura del proyecto

INF8239_U01/
├── data/
├── notebooks/
│ └── 00_verificacion.ipynb
├── reports/
├── src/
│ └── inf8239_u01/
│ ├── init.py
│ └── environment.py
├── tests/
│ └── test_environment.py
├── .gitignore
├── README.md
└── requirements.txt

## Comandos usados (LAB00)

### Verificación de Python y Git

python --version
python -m pip --version
git --version
git config --global user.name "Raimi Dejesus"
git config --global user.email "raymiruben10@gmail.com"
git config --global --list

### Creación del proyecto
mkdir INF8239_U01
cd INF8239_U01
mkdir data,notebooks,reports,src,tests
dir
code .

### Entorno virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

### Instalación de dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

### Pruebas unitarias
$env:PYTHONPATH="src"
python -m pytest -q

### Git — control de versiones
git init
git add .
git commit -m "chore: create INF-8239 reproducible environment"
git status
git log --oneline

## Notas

- Se usó `mkdir data,notebooks,reports,src,tests` (separado por comas) en
  lugar de espacios, por ser la sintaxis correcta del alias `mkdir` en
  PowerShell.
- El kernel de Jupyter seleccionado en los notebooks corresponde al
  entorno virtual `.venv` (Python 3.13.7).
  

  ## LAB02 — Dataset propio: enfermedad hepática (ILPD)

### Instalación y descarga
El dataset se descarga automáticamente ejecutando la celda correspondiente
del notebook `01_svm_guiada.ipynb`, que llama a
`inf8239_u01.data.download_csv()`. No requiere Google Drive ni rutas
personales — el archivo se guarda en `data/raw/dataset.csv`.

### Target
`Selector` — clasificación binaria (1 = enfermedad hepática, 2 = sin
enfermedad).

### Métrica
F1-macro, por el desbalance de clases (71% / 29%).

### Ejecución

.venv\Scripts\Activate.ps1
$env:PYTHONPATH="src"
python -m pytest -q
Luego abrir `notebooks/01_svm_guiada.ipynb` y ejecutar todas las celdas
en orden.

## Conclusión

Este laboratorio permitió adaptar el pipeline de clasificación construido en
LAB01 a un dataset propio y real: el Indian Liver Patient Dataset (ILPD) del
repositorio UCI, con el objetivo de apoyar la identificación de pacientes con
probable enfermedad hepática a partir de marcadores bioquímicos de sangre.

El proceso comenzó por formular el problema antes de buscar datos: se definió
el dominio, la unidad de análisis, la decisión que el modelo apoyaría y el
error más costoso (un falso negativo, es decir, no detectar a un paciente
enfermo). Se compararon dos candidatos —el ILPD y el dataset Pima de
diabetes— y se eligió el ILPD por incluir una variable categórica (Género)
que permitía ejercitar el preprocesamiento completo con `ColumnTransformer`,
algo que un dataset puramente numérico no habría permitido.

La descarga se implementó de forma reproducible mediante la función
`download_csv()`, sin depender de rutas personales ni de Google Drive. Sin
embargo, surgió un problema recurrente ya observado en LAB01: al ejecutar la
descarga desde el notebook, el directorio de trabajo correspondía a
`notebooks/` y no a la raíz del proyecto, por lo que el archivo se guardó
inicialmente en una ubicación incorrecta. Se corrigió usando `Path.cwd()`
para construir una ruta absoluta hacia la raíz, la misma estrategia aplicada
previamente para los resultados de LAB01 — confirmando que este es un patrón
de error a tener en cuenta al trabajar con Jupyter.

La auditoría del dataset reveló hallazgos reales: 4 valores ausentes en la
variable `AG_Ratio` (0.69%) y 13 filas duplicadas. Se decidió conservar los
duplicados, documentando la limitación de no contar con un identificador de
paciente que permitiera confirmar si se trataba de registros repetidos o de
coincidencias plausibles entre pacientes distintos.

El hallazgo más relevante ocurrió al comparar el baseline con la SVM: con
hiperparámetros por defecto, la SVM (F1-macro 0.406) tuvo un desempeño
prácticamente idéntico al `DummyClassifier` (F1-macro 0.415), colapsando a
predecir casi siempre la clase mayoritaria (recall de 0% en la clase
minoritaria). Esto evidenció el efecto del desbalance de clases (71%/29%)
sobre un modelo sin ajustar. Al introducir `class_weight="balanced"`, el
F1-macro subió a 0.619 y el recall de la clase minoritaria pasó de 0% a 88%,
aunque a costa de reducir el recall de la clase mayoritaria (de 96% a 52%) —
una tensión real entre el balance estadístico y el error clínicamente más
costoso definido en la ficha del dataset, que merece seguir explorándose en
laboratorios posteriores.

En conjunto, LAB01 y LAB02 documentan un flujo completo y honesto de trabajo
con datos reales: desde la formulación del problema hasta el hallazgo de
limitaciones del modelo, pasando por errores de reproducibilidad
identificados y corregidos de forma transparente.
