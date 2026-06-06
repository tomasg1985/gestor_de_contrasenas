# 🔐 Gestor de Contraseñas - TalentoLab

Este es un sistema de gestión de credenciales desarrollado en **Python** como parte del programa de formación en **Talento Tech**. El proyecto representa una evolución técnica significativa, migrando de una estructura de datos basada en listas hacia una arquitectura profesional optimizada con **diccionarios**, **modularización** y **documentación técnica**.

## 🚀 Características Principales

*   **Arquitectura Modular**: Separación estricta de responsabilidades entre la interfaz de usuario (`app.py`) y la lógica de negocio (`logica_gestor.py`).
*   **Eficiencia O(1)**: Uso de diccionarios para garantizar búsquedas, ediciones y eliminaciones instantáneas mediante el uso de claves únicas (cuentas), optimizando drásticamente el rendimiento.
*   **Validación de Datos**: Implementación de controles de flujo para evitar campos vacíos y asegurar la integridad de la información ingresada.
*   **Experiencia de Usuario (UX)**: Interfaz de consola mejorada con la librería **Colorama**, proporcionando feedback visual intuitivo (éxitos en verde, errores en rojo y advertencias en amarillo).
*   **Documentación Senior**: Todas las funciones core están documentadas mediante **Docstrings** profesionales que detallan propósito, parámetros y tipos de retorno.

## 🛠️ Tecnologías Utilizadas

*   **Python 3.x**
*   **Colorama**: Para el estilizado y manejo de colores en la terminal.

## 📂 Estructura del Proyecto

1.  **`app.py`**: El punto de entrada del programa. Gestiona el menú interactivo mediante la instrucción `match` y coordina la interacción con el usuario.
2.  **`logica_gestor.py`**: El motor lógico. Contiene las funciones core de administración: `nueva_contrasena`, `ver_contrasena`, `eliminar_contrasena` y `editar_contrasena`.

## 🔧 Instalación y Ejecución

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/nombre-del-repo.git
    ```
2.  **Instalar dependencias**:
    ```bash
    pip install colorama
3.  **Ejecutar la aplicación**:
    ```bash
    python app.py
