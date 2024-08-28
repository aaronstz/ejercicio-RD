# README.md

## Microservicio REST API en Python con FastAPI

Este proyecto es un microservicio REST API desarrollado en Python utilizando FastAPI. La aplicación permite recibir datos a través de un endpoint, modificar ciertos campos y almacenarlos en una base de datos SQLite. También incluye autenticación básica y permite recuperar los datos almacenados.

### Características

- **Autenticación Básica**: Protege los endpoints con un método de autenticación básica.
- **Endpoint POST**: `/input/{my_target_field}` para recibir datos en formato JSON y convertir el campo especificado a mayúsculas.
- **Endpoint GET**: `/data/{id}` para recuperar los datos almacenados en la base de datos usando el ID.
- **Base de Datos**: Utiliza SQLite para almacenar los datos.
- **Documentación Interactiva**: Genera automáticamente una interfaz Swagger para probar los endpoints.

### Estructura del Proyecto

```
/ejercicio_RD
    ├── main.py
    ├── models.py
    ├── database.py
    ├── requirements.txt
    └── README.md
```

### Requisitos

- Python 3.7 o superior
- Dependencias en `requirements.txt`

### Instalación y Configuración

1. **Clonar el Repositorio**:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ejercicio_RD
   ```

2. **Instalar Dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la Aplicación**:

   ```bash
   uvicorn ejercicio_RD.main:app
   ```

   La aplicación estará disponible en `http://127.0.0.1:8000`.

### Uso de la Aplicación

#### Autenticación

Las credenciales para acceder a los endpoints son:

- **Nombre de usuario**: `admin`
- **Contraseña**: `password`

#### Ejemplo de Solicitudes

##### 1. POST `/input/{my_target_field}`

Este endpoint recibe un JSON y convierte el campo especificado a mayúsculas. 

**Ejemplo de solicitud**:

```bash
curl -u admin:password -X POST http://localhost:8000/input/author -H "Content-Type: application/json" -d '{"field_1": "some data ...", "author": "some author data...", "description": "even more data...", "my_numeric_field": 123}'
```

**Respuesta esperada**:

```json
{
    "id": 1
}
```

##### 2. GET `/data/{id}`

Este endpoint recupera los datos almacenados en la base de datos usando el ID.

**Ejemplo de solicitud**:

```bash
curl -u admin:password http://localhost:8000/data/1
```

**Respuesta esperada**:

```json
{
    "ID": 1,
    "field_1": "some data ...",
    "author": "SOME AUTHOR DATA...",
    "description": "even more data...",
    "my_numeric_field": 123
}
```

#### Errores

Si se pasa un valor que no corresponde a uno de los campos válidos, se devolverá un mensaje de error.

**Ejemplo de solicitud con error**:

```bash
curl -u admin:password -X POST http://localhost:8000/input/random_field -H "Content-Type: application/json" -d '{"field_1": "some data ...", "author": "some author data...", "description": "even more data...", "my_numeric_field": 123}'
```

**Respuesta esperada**:

```json
{
    "error": "random_field no es un campo válido para convertir a mayúscula"
}
```

