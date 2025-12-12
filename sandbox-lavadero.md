
# Sandboxing y pruebas de la aplicación `lavadero`

## Índice


- [Sandboxing y pruebas de la aplicación `lavadero`](#sandboxing-y-pruebas-de-la-aplicación-lavadero)
  - [Índice](#índice)
  - [Introducción](#introducción)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Creación del entorno virtual](#creación-del-entorno-virtual)
  - [Ejecución normal de la aplicación](#ejecución-normal-de-la-aplicación)
  - [Ejecución en sandbox con Firejail](#ejecución-en-sandbox-con-firejail)
    - [Instalación y comprobación de Firejail](#instalación-y-comprobación-de-firejail)
    - [Ejecución de `lavadero` dentro del sandbox](#ejecución-de-lavadero-dentro-del-sandbox)


## Introducción
En esta parte de la actividad he probado la aplicación `lavadero` en un entorno controlado tipo *sandbox* usando herramientas del sistema en mi máquina Kali. La idea es poder ejecutar un programa (o incluso malware) aislado del sistema principal, reduciendo el impacto si se comporta de forma maliciosa o tiene vulnerabilidades.

## Estructura del proyecto

Mi repositorio de la actividad tiene la siguiente estructura:
```text
PPSUnidad1-ActividadSandboxingTuNombre/  
├─ src/  
│ ├─ lavadero.py  
│ ├─ main_app.py  
├─ sandbox-lavadero.md  
├─ reflexion-lenguajes.md
```
El archivo que se ejecuta como entrada principal es `src/main_app.py`, que a su vez utiliza la lógica definida en `lavadero.py`.

## Creación del entorno virtual

Siguiendo la misma idea que en la actividad de pruebas en Python, primero he creado un entorno virtual para aislar las dependencias.

1. Desde la carpeta del proyecto:
```bash
cd PPSUnidad1-ActividadSandboxingTuNombre
python3 -m venv .venv
```
2. Activar el entorno virtual:
```bash
source .venv/bin/activate
```
En el prompt aparece ahora `(.venv)` delante, lo que indica que estoy usando el Python del entorno virtual.

3. Verificación rápida de que se usa el Python del entorno:
```bash
which python
python --version
```
Esto me asegura que cualquier paquete que instale o ejecute queda dentro de este entorno y no afecta al Python global del sistema.

## Ejecución normal de la aplicación

Antes de meter nada en sandbox, comprobé que la aplicación funciona de forma normal dentro del entorno virtual.
1. Desde la raíz del proyecto, con el entorno virtual activado:
```bash
python3 src/main_app.py
```
2. Probé varios casos de uso, introduciendo datos por teclado y verificando que la lógica de `lavadero` se ejecutaba correctamente (mensajes esperados, cálculos, etc.).
![Captura prueba ejecución]()


## Ejecución en sandbox con Firejail

Para hacer el sandboxing en Kali he utilizado **Firejail**, que es una herramienta ligera para aislar procesos mediante espacios de nombres y perfiles de seguridad. En las transparencias de la unidad se mencionan herramientas de este tipo como ejemplo de sandbox basado en software.

### Instalación y comprobación de Firejail

1. Instalé Firejail (si no estaba ya en el sistema):
```bash
sudo apt update
sudo apt install firejail
```
2. Verifiqué que Firejail está disponible:
```bash
firejail --version
```
### Ejecución de `lavadero` dentro del sandbox

La idea es ejecutar el mismo comando de antes, pero precedido por `firejail`, para que el proceso de Python se ejecute en un entorno aislado con restricciones sobre el sistema de archivos, red, etc.
1. Desde la raíz del proyecto, con el entorno virtual activado:
```bash
cd PPSUnidad1-ActividadSandboxingTuNombre
source .venv/bin/activate
```
2. Ejecuté la aplicación `main_app.py` dentro de Firejail, indicando el `PYTHONPATH` para que encuentre el paquete `src`:
```bash
firejail --private=./ --whitelist=./src python3 src/main_app.py
```
- `--private=./` hace que Firejail cree un *home* privado basado en la carpeta actual, aislando el resto del sistema de archivos.  
- `--whitelist=./src` garantiza que la carpeta `src` está accesible dentro del sandbox, de forma que el programa puede leer sus archivos.  
- `python3 src/main_app.py` es el mismo comando que usaba fuera del sandbox, pero ahora se ejecuta con las restricciones de Firejail.
3. Dentro de este entorno, volví a probar la aplicación introduciendo varios datos, igual que en la ejecución normal, y comprobé que el comportamiento era el mismo (mismas entradas, mismas salidas), pero ahora el proceso estaba aislado del resto de mi sistema Kali.
![Captura Firejail]()
![Captura ejecucion en Firejail]()


