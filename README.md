# 🔐 Gestor de Contraseñas Local

Un sistema de gestión de credenciales estructurado desarrollado en **Python** como parte del programa de formación en **Talento Tech**. Este proyecto representa una evolución técnica significativa, migrando de estructuras de datos lineales hacia una arquitectura optimizada con diccionarios y una separación estricta de responsabilidades.

---

### 🚀 Características Principales

*   **Arquitectura Modular:** Separación estricta de responsabilidades (SoC) entre la interfaz de usuario (`app.py`) y la lógica de negocio (`logica_gestor.py`).
*   **Eficiencia $O(1)$:** Uso estratégico de diccionarios para garantizar búsquedas, ediciones y eliminaciones instantáneas mediante claves únicas (cuentas), optimizando drásticamente el rendimiento frente a estructuras basadas en listas.
*   **Validación de Datos:** Implementación de controles de flujo defensivos para mitigar campos vacíos y asegurar la integridad de la información ingresada.
*   **Experiencia de Usuario (UX):** Interfaz interactiva por línea de comandos potenciada con la librería **Colorama**, proporcionando un sistema de alertas visuales intuitivo (Éxitos en verde, Errores en rojo y Advertencias en amarillo).
*   **Documentación Senior:** Funciones *core* completamente documentadas mediante **Docstrings** profesionales que detallan de forma explícita el propósito, tipos de parámetros y esquemas de retorno.

---

### 🛠️ Tecnologías Utilizadas

*   **Python 3.x**
*   **Colorama:** Para el estilizado y manejo de colores en la terminal de comandos.

---

### 📂 Estructura del Proyecto

1.  **`app.py`**: El punto de entrada del programa. Gestiona el menú interactivo mediante la instrucción nativa `match` y coordina la interacción directa con el usuario.
2.  **`logica_gestor.py`**: El motor lógico de la aplicación. Encapsula las funciones *core* de administración: `nueva_contrasena`, `ver_contrasena`, `eliminar_contrasena` y `editar_contrasena`.

---

### 🔧 Instalación y Ejecución

Sigue estos pasos para clonar, configurar y ejecutar la aplicación de forma local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd gestor_de_contrasenas
   ```

2. **Instalar las dependencias necesarias:**
   ```bash
   pip install colorama
   ```

3. **Iniciar la aplicación:**
   ```bash
   python app.py
   ```

---

### 📄 Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo de origen para más información.
