# 🔐 Gestor de Contraseñas Híbrido con Tolerancia a Fallos (SQL & Memoria)

Un sistema de misión crítica para la administración local de credenciales desarrollado en **Python** e integrado con **SQLite**. El proyecto destaca por su arquitectura híbrida de alto rendimiento y su robusta capa de persistencia defensiva, la cual implementa control de excepciones avanzado y reversión de transacciones para garantizar la integridad absoluta de los datos.

---

### 🚀 Innovaciones y Características Técnicas

*   **Arquitectura de Persistencia Robusta (SQLite):** Inicialización automatizada de esquemas relacionales relocalizables. Centraliza el almacenamiento físico en disco asegurando la persistencia a largo plazo.
*   **Manejo de Excepciones y Transacciones Seguras:** Integración de bloques de control de fallos (`try/except sqlite3.Error`) en todas las operaciones de escritura. Implementa mecanismos de reversión automática (`conexion.rollback()`) ante errores del motor, evitando la corrupción de las tablas.
*   **Sincronización Eficiente de Estado Dinámico:** Reconstrucción óptima del estado de la aplicación al arranque mediante la conversión de tuplas relacionales a diccionarios en memoria. Permite lecturas y validaciones de alta velocidad sin sobrecargar el disco duro.
*   **Seguridad contra Inyecciones SQL (SQLi):** Uso estricto de consultas parametrizadas basadas en marcadores de posición (`?`), aislando por completo las entradas del usuario de las sentencias del motor de la base de datos.
*   **Auditoría y Métrica de Entropía:** Generador criptográfico con evaluación en tiempo real de la longitud de clave solicitada, categorizando el nivel de seguridad del string generado.

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.x
*   **Motor Relacional:** [SQLite3](https://python.org) (Mapeo relacional local)
*   **Librerías Core:** `random` (Entropía algorítmica), `colorama` (Consola interactiva UX)

---

### 🗄️ Modelo Físico de Datos

El sistema asegura y estructura la persistencia mediante la creación automática de la siguiente entidad relacional indexada:

```sql
CREATE TABLE IF NOT EXISTS gestor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cuenta TEXT NOT NULL,
    usuario TEXT NOT NULL,
    contrasena TEXT NULL
);
```

---

### 📂 API de la Capa de Negocio (`logica_gestor.py`)

Las funciones del motor lógico implementan estándares avanzados de documentación y aislamiento de código:

| Función | Operación CRUD | Mecanismo de Estabilidad y Control |
| :--- | :--- | :--- |
| `cargar_datos()` | **Read (SELECT ALL)** | Escanea el disco al inicio de la app, procesa el set de registros completo mediante bucles limpios y levanta el diccionario en memoria. |
| `nueva_contrasena()` | **Create (INSERT)** | Captura metadatos en caliente (`lastrowid`), actualiza la memoria y confirma cambios (`commit`). Ejecuta rollback automático en caso de fallo. |
| `buscar_contrasena()` | **Read (SELECT WHERE)** | Ejecuta consultas filtradas por cuenta y desestructura el registro de forma directa desde la base de datos. |
| `editar_contrasena()` | **Update (UPDATE)** | Sanitiza entradas (`.strip().title()`), actualiza los punteros en memoria y muta el registro físico en la base de datos de manera segura. |
| `eliminar_contrasena()` | **Delete (DELETE)** | Implementa un flujo defensivo de doble confirmación interactiva (`Si/No`) antes de remover de manera física y lógica el registro. |
| `generar_sugerencia()`| **Algorítmica** | Valida tipos de datos nativos (`.isdigit()`) para asegurar el flujo del programa y mitigar excepciones de casteo de tipos. |

---

### ⚙️ Despliegue y Ejecución Local

Clona y ejecuta el entorno seguro siguiendo estos pasos en tu terminal:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd gestor_de_contrasenas
   ```

2. **Instalar dependencias de interfaz:**
   ```bash
   pip install colorama
   ```

3. **Iniciar el sistema:**
   ```bash
   python app.py
   ```
   *(Nota: El archivo relacional `gestor.db` se generará automáticamente en el directorio raíz durante la primera inicialización).*

---

### 📄 Licencia

Este proyecto está bajo la Licencia MIT. Libre para su modificación, distribución y uso profesional continuo.
