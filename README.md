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
