# PPSUnidad1 - Actividad Sandboxing

## Índice

- [Descripción de la actividad](#descripción-de-la-actividad)
- [Contenido del repositorio](#contenido-del-repositorio)
- [Cómo ver la reflexión de lenguajes](#cómo-ver-la-reflexión-de-lenguajes)
- [Cómo ver la actividad de sandboxing](#cómo-ver-la-actividad-de-sandboxing)

## Descripción de la actividad

Este repositorio contiene la actividad de la Unidad 1 de **Puesta en Producción Segura**, centrada en:

- Reflexión sobre la seguridad en diferentes lenguajes de programación.
- Creación de un entorno de ejecución aislado (*sandbox*) para probar la aplicación `lavadero` en un entorno controlado.


## Contenido del repositorio

```text
PPSUnidad1-ActividadSandboxingTuNombre/
├─ src/
│ ├─ lavadero.py
│ ├─ main_app.py
├─ reflexion-lenguajes.md
├─ sandbox-lavadero.md
├─ README.md
```
- `src/`: Código fuente de la aplicación `lavadero`.
- `reflexion-lenguajes.md`: Reflexión sobre infraestructuras de seguridad de distintos lenguajes.
- `sandbox-lavadero.md`: Documentación de la actividad de sandboxing y ejecución en Kali.
- `README.md`: Este archivo.


## Cómo ver la reflexión de lenguajes

La reflexión pedida está en:

- [`reflexion-lenguajes.md`](./reflexion-lenguajes.md)

En ese documento se analiza la seguridad de lenguajes como Python, Java, .NET y PHP, relacionándolo con los contenidos teóricos de la unidad.

## Cómo ver la actividad de sandboxing

La documentación completa de la creación del entorno aislado y la ejecución de la aplicación `lavadero` está en:

- [`sandbox-lavadero.md`](./sandbox-lavadero.md)

Ahí se describe:
- Estructura del proyecto.
- Creación del entorno virtual en Kali.
- Ejecución normal de `main_app.py`.
- Ejecución de la aplicación dentro de un sandbox usando Firejail.
- Capturas de pantalla de la ejecución.
