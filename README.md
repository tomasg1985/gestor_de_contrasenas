# 🔐 Gestor de Contraseñas Híbrido (Python & SQLite3)

<p align="left">
  <img src="https://shields.io" alt="Language">
  <img src="https://shields.io" alt="Repo Size">
  <img src="https://shields.io" alt="License">
</p>

Sistema local de gestión de credenciales que utiliza una arquitectura híbrida: combina la persistencia de **SQLite3** con un manejo eficiente en memoria.

## 🚀 Características
*   **Seguridad:** Uso de consultas parametrizadas contra inyecciones SQL.
*   **Robustez:** Manejo de excepciones y transacciones seguras (rollback).
*   **Funcionalidad:** Gestión CRUD completa, generación de contraseñas y alta eficiencia.

## 📂 API de la Capa de Negocio (`logica_gestor.py`)

| Función | Descripción |
| :--- | :--- |
| `cargar_datos()` | Lectura de datos en memoria (SQLite). |
| `nueva_contrasena()` | Creación de registro con control de errores. |
| `editar_contrasena()` | Actualización segura de credenciales. |
| `eliminar_contrasena()`| Borrado con doble confirmación. |

## ⚙️ Instalación y Uso
1. **Clonar:** `git clone https://github.com`
2. **Entrar:** `cd gestor_de_contrasenas`
3. **Dependencias:** `pip install -r requirements.txt`
4. **Ejecutar:** `python app.py`

## 📄 Licencia
[MIT](LICENSE)
