# Santiaguía
La Santiaguía es una página web escrita con Django.

Es un portal de información que ayuda al estudiante foráneo a vivir y estudiar en Santiago, a través de una wiki, mapa y, además, cuenta con un sistema de colaboración para que alumnos o personas puedan ayudar con nueva información a añadir.

## Setup
Las instrucciones están pensadas en ser ejecutadas a través de una CLI (command line interface).\
*IMPORTANTE*: Es necesario tener `git`, `python` (>= 3.15.2) y `pip`.
1. Clonar el repositorio
> Dentro de una carpeta, ejecuta el comando `git clone https://github.com/ruax2891/santiaguia/main`. Esto clonará el repositorio a la carpeta en la que estás situado en tu CLI.
> Usa `cd santiaguia` para entrar a la carpeta del repositorio

2. Entorno virtual
> Crea el entorno virtual: `python -m venv venv/`.
> Activa el entorno virtual:
> - \*nix: `source venv/bin/activate`.
> - Windows (cmd): `venv\Scripts\activate.bat`.
> - Windows (PowerShell): `venv\Scripts\Activate.ps1`.

3. Instalación de dependencias
> Instala las dependencias del entorno virtual: `pip install -r requirements.txt`.

4. Corre el servidor de testeo de django
> Estando en la carpeta raíz del repositorio, crea un usuario administrador con `python manage.py createsuperuser` y ingresa los datos que desees.
> Estando en la carpeta raiz del repositorio, corre `python manage.py runserver`.
> En un navegador, entra a `http://localhost:8000/` o `http://127.0.0.1:8000/`.

5. Probar funcionalidad corazón
> Mientras la página está andando, entra al apartado de Wiki `http://localhost:8000/wiki/` y entra como usuario administrador.
> Luego, sigue los pasos que indica la página para crear el primer artículo raíz y finalmente puedes crear, modificar y ver el historial de los artículos ocupando los botones integrados en la página de wiki.