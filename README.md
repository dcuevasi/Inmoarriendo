# InmoArriendo

InmoArriendo es una aplicación web desarrollada con Django para facilitar el proceso de arriendo de propiedades. Esta aplicación permite a los usuarios arrendar propiedades, listar sus inmuebles y buscar ofertas disponibles en el sitio.

## Funcionalidades

- **Registro y Autenticación de Usuarios**: Los usuarios pueden registrarse y autenticarse para acceder a sus perfiles.
- **Perfil de Usuario**: Los usuarios pueden ver y editar su información de perfil.
- **Gestión de Inmuebles**:
  - **Arrendadores**: Pueden agregar, editar y eliminar sus inmuebles.
  - **Arrendatarios**: Pueden ver la oferta de inmuebles disponibles para arriendo.
- **Páginas Públicas**: La página principal y la página de oferta de inmuebles están disponibles sin necesidad de autenticación.

## Tecnologías Utilizadas

- **Backend**: Django 4.2.11
- **Frontend**: HTML, CSS y Bootstrap 5.3.3
- **Base de Datos**: SQLite (puede cambiarse a PostgreSQL, MySQL, etc.)
- **Despliegue**: A considerar (Heroku, AWS, etc.)

## Instalación y Configuración

### Prerrequisitos

- Python 3.10
- Virtualenv (recomendado)

## Estructura del Proyecto

- **inmoarriendo/**: Contiene la configuración del proyecto Django.
- **proyecto_inmobiliaria/**: Aplicación principal que contiene los modelos, vistas, urls y plantillas.
- **static/**: Archivos estáticos (CSS, JS, imágenes).
- **templates/**: Plantillas HTML.

## Modelos Principales

### Usuario
- `User`: Extiende el modelo de usuario de Django.
- `Usuario`: Información adicional del usuario (nombres, apellidos, RUT, dirección, teléfono, tipo de usuario).

### Inmueble
- `Inmueble`: Información sobre los inmuebles (nombre, descripción, m2 construidos, m2 totales, estacionamientos, habitaciones, baños, dirección, comuna, tipo de inmueble, precio mensual, arrendador).

### Comuna
- `Comuna`: Información sobre las comunas (nombre, región).

### Región
- `Región`: Información sobre las regiones (nombre).

## Vistas Principales

- **home_view**: Vista principal de la página de inicio.
- **profile_view**: Vista del perfil de usuario.
- **edit_profile_view**: Vista para editar el perfil de usuario.
- **agregar_inmueble_view**: Vista para agregar un nuevo inmueble.
- **lista_inmuebles_view**: Vista para listar los inmuebles del arrendador.
- **listar_oferta_view**: Vista para listar la oferta de inmuebles.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. **Haz un Fork del Proyecto**.
2. **Crea una Rama para tu Funcionalidad** (`git checkout -b feature/nueva-funcionalidad`).
3. **Haz Commit de tus Cambios** (`git commit -m 'Agrega nueva funcionalidad'`).
4. **Haz Push a la Rama** (`git push origin feature/nueva-funcionalidad`).
5. **Abre un Pull Request**.

## Contacto

Desarrollado por [David Cuevas]. Puedes contactarme en [dcuevasiturrieta@gmail.com].
