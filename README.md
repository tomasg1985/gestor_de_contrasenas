# 🔐 Gestor de Contraseñas - TalentoLab

Este es un sistema de gestión de credenciales desarrollado en **Python** como parte del programa de formación en **Talento Tech**. El proyecto representa una evolución técnica significativa, migrando de una estructura de datos basada en listas hacia una arquitectura profesional optimizada con **diccionarios**, **modularización** y **documentación técnica** [cite: 22, 224].

## 🚀 Características Principales

*   **Arquitectura Modular**: Separación estricta de responsabilidades entre la interfaz de usuario (`app.py`) y la lógica de negocio (`logica_gestor.py`) [cite: 161, 189].
*   **Eficiencia O(1)**: Uso de diccionarios para garantizar búsquedas, ediciones y eliminaciones instantáneas mediante el uso de claves únicas (cuentas), optimizando drásticamente el rendimiento [cite: 104, 110].
*   **Validación de Datos**: Implementación de controles de flujo para evitar campos vacíos y asegurar la integridad de la información ingresada [cite: 36, 112].
*   **Experiencia de Usuario (UX)**: Interfaz de consola mejorada con la librería **Colorama**, proporcionando feedback visual intuitivo (éxitos en verde, errores en rojo y advertencias en amarillo) [cite: 178, 196].
*   **Documentación Senior**: Todas las funciones core están documentadas mediante **Docstrings** profesionales que detallan propósito, parámetros y tipos de retorno [cite: 144, 160].

## 🛠️ Tecnologías Utilizadas

*   **Python 3.x** [cite: 10]
*   **Colorama**: Para el estilizado y manejo de colores en la terminal [cite: 178].

## 📂 Estructura del Proyecto

1.  **`app.py`**: El punto de entrada del programa. Gestiona el menú interactivo mediante la instrucción `match` y coordina la interacción con el usuario [cite: 189].
2.  **`logica_gestor.py`**: El motor lógico. Contiene las funciones core de administración: `nueva_contrasena`, `ver_contrasena`, `eliminar_contrasena` y `editar_contrasena` [cite: 189].

## 🔧 Instalación y Ejecución

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/nombre-del-repo.git
    ```
2.  **Instalar dependencias**:
    ```bash
    pip install colorama
    ``` [cite: 178]
3.  **Ejecutar la aplicación**:
    ```bash
    python app.py
    ``` [cite: 17]

## 📝 Próximos Pasos (Roadmap)

*   [ ] **Persistencia de Datos**: Implementación de guardado permanente en archivos `.txt` o `.json` (Clase 12) [cite: 184, 207].
*   [ ] **Cifrado**: Seguridad avanzada mediante encriptación de contraseñas.
<<<<<<< HEAD
*   [ ] **Base de Datos**: Migración del sistema a SQLite para gestión de volúmenes de datos masivos
=======
*   [ ] **Base de Datos**: Migración del sistema a SQLite para gestión de volúmenes de datos masivos
>>>>>>> 84934 (Se reescribio el readme con las optimizaciones nuevas del sistema de gestion de contraseñas)
