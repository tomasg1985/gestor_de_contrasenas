# 🔐 Gestor de Contraseñas Corporativo con Persistencia SQL

Un sistema avanzado de administración y auditoría de credenciales desarrollado en **Python** e integrado con **SQLite**. Este proyecto representa una arquitectura híbrida de alto rendimiento, combinando la velocidad de acceso en memoria de los diccionarios con la persistencia estructurada y segura de una base de datos relacional.

---

### 🚀 Innovaciones y Características Técnicas

*   **Persistencia Relacional (SQLite):** Implementación de una base de datos local embebida con esquemas autoincrementales (`INTEGER PRIMARY KEY AUTOINCREMENT`) para asegurar que las credenciales sobrevivan al cierre de la aplicación.
*   **Consultas Seguras y Parametrizadas:** Mitigación de vulnerabilidades críticas de seguridad mediante el uso de tuplas de escape y marcadores de posición (`?`), previniendo ataques de Inyección SQL (SQLi).
*   **Arquitectura de Sincronización Dual:** Motor lógico optimizado que realiza operaciones en caliente sobre la base de datos (Consultas, Inserciones, Actualizaciones y Borrados) y reconstruye en paralelo el estado en un diccionario en memoria para lecturas instantáneas.
*   **Algoritmo de Complejidad Criptográfica:** Generador de claves aleatorias basado en entropía de caracteres que analiza dinámicamente la longitud solicitada por el usuario, clasificando el nivel de seguridad del *string* resultante.
*   **Programación Defensiva Extrema:** Doble confirmación recursiva para operaciones destructivas (`DELETE`) y validaciones nativas estrictas para evitar el almacenamiento de registros huérfanos o campos vacíos.

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.x
*   **Persistencia:** [SQLite3](https://python.org) (Motor relacional nativo)
*   **Librerías de Soporte:** `random` (Entropía y aleatoriedad), `colorama` (Feedback UX visual)

---

### 🗄️ Esquema de la Base de Datos

El sistema inicializa automáticamente una tabla estructurada llamada `gestor` bajo el siguiente modelo relacional:

```sql
CREATE TABLE IF NOT EXISTS gestor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cuenta TEXT NOT NULL,
    usuario TEXT NOT NULL,
    contrasena TEXT NULL
);
```

---

### 📂 Análisis del Núcleo Lógico (`logica_gestor.py`)

Las funciones del componente de negocio han sido diseñadas bajo estándares profesionales de documentación:

| Función | Tipo de Operación | Descripción Técnica |
| :--- | :--- | :--- |
| `cargar_datos()` | **Lectura Inicial / Boot** | Consulta el disco duro al arrancar la app y mapea las filas relacionales en un diccionario indexado por clave única. |
| `nueva_contrasena()` | **Escritura (INSERT)** | Inserta las credenciales en la DB, captura el ID generado en tiempo real (`lastrowid`) y actualiza el estado local. |
| `buscar_contrasena()` | **Filtro Indexado (SELECT)** | Realiza búsquedas directas en el motor de base de datos optimizando el consumo de memoria. |
| `editar_contrasena()` | **Mutación (UPDATE)** | Sanitiza las nuevas entradas del usuario mediante `.strip().title()` y actualiza el registro en ambas capas. |
| `eliminar_contrasena()` | **Destrucción (DELETE)** | Implementa un flujo de confirmación binaria segura antes de ejecutar la remoción física del registro. |
| `generar_sugerencia()`| **Lógica Algorítmica** | Evalúa la robustez de las claves mediante validaciones numéricas (`.isdigit()`) y genera hashes aleatorios seguros. |

---

### ⚙️ Instalación y Pruebas Local

Ejecuta el entorno en tu terminal con los siguientes pasos:

1. **Clonar la versión con soporte SQL:**
   ```bash
   git clone https://github.com
   cd gestor_de_contrasenas
   ```

2. **Instalar el manejador de interfaz visual:**
   ```bash
   pip install colorama
   ```

3. **Iniciar el gestor de credenciales:**
   ```bash
   python app.py
   ```
   *(Nota: Al ejecutarlo por primera vez, el sistema creará automáticamente el archivo de base de datos `gestor.db` en la raíz).*

---

### 📄 Licencia

Este software se distribuye bajo la Licencia MIT. Libre para uso, modificación y distribución académica.

### 📄 Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo de origen para más información.
