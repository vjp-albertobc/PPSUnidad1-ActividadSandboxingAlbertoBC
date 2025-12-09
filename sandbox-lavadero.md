
# Sandboxing y pruebas de la aplicación `lavadero`

## Índice

- [Sandboxing y pruebas de la aplicación `lavadero`](#sandboxing-y-pruebas-de-la-aplicación-lavadero)
  - [Índice](#índice)
  - [Introducción](#introducción)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Creación del entorno virtual](#creación-del-entorno-virtual)
  - [Pruebas unitarias de `lavadero`](#pruebas-unitarias-de-lavadero)


## Introducción

En esta parte de la actividad he puesto en práctica la idea de ejecutar una aplicación Python en un entorno controlado (*sandbox*), similar a lo que se comenta en la unidad sobre entornos de ejecución aislados y herramientas de sandboxing. He combinado tres elementos: entorno virtual de Python, pruebas unitarias y Firejail en Kali, para comprobar que la aplicación `lavadero` funciona correctamente incluso cuando está aislada del sistema.

## Estructura del proyecto

Mi repositorio de la actividad tiene la siguiente estructura:
```
PPSUnidad1-ActividadSandboxingTuNombre/  
├─ src/  
│ ├─ lavadero.py  
│ ├─ main_app.py  
├─ tests/  
│ ├─ test_lavadero_unittest.py  
├─ sandbox-lavadero.md  
├─ reflexion-lenguajes.md
```
- `lavadero.py`: contiene la lógica principal de la aplicación (funciones o clases).  
- `main_app.py`: punto de entrada que usa `lavadero`.  
- `tests/test_lavadero_unittest.py`: pruebas unitarias de la lógica de `lavadero`.

## Creación del entorno virtual

Siguiendo la misma idea que en la actividad de pruebas en Python, primero he creado un entorno virtual para aislar las dependencias.

1. Desde la raíz del proyecto:
```bash
cd PPSUnidad1-ActividadSandboxingTuNombre
python3 -m venv .venv
```
2. Activar el entorno virtual:
```bash
source .venv/bin/activate
```
3. Verificación rápida de que se usa el Python del entorno:
```bash
which python
python --version
```
Esto asegura que cualquier librería que instale o use queda dentro del proyecto y no afecta al Python del sistema.

## Pruebas unitarias de `lavadero`

Para tener una forma automática de comprobar el comportamiento de la aplicación, he creado un archivo de pruebas con `unittest` para la lógica de `lavadero`.
1. He creado la carpeta `tests` y dentro el archivo `tests/test_lavadero_unittest.py`.  
2. El contenido es similar a esto (adaptado a las funciones/clases reales de `lavadero.py`).
3. Ejecución de las pruebas sin sandbox, para asegurar que todo está correcto:
```bash
#Desde la raíz del proyecto, con .venv activado
PYTHONPATH=src python3 -m unittest tests/test_lavadero_unittest.py -v
```

