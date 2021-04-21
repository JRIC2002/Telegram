# Telegram
![Telegram v1.0.0](https://img.shields.io/badge/Telegram-v1.0.0-brightgreen)
![Release stable](https://img.shields.io/badge/Release-stable-brightgreen)
![License GNU General Public License v3.0](https://img.shields.io/badge/License-GNU%20General%20Public%20License%20v3.0-blue)

## Información
Con esta sencilla herramienta en python podrás iniciar sesión con tu cuenta de Telegram desde la Terminal y con funciones extra.

## Características
* Iniciar sesión con tu username, api id y api hash.
* Funciones extra.

## Instalación
1. Para el despliegue de la herramienta vamos a necesitar Python, si no lo tienes instalado puedes descargarlo desde el sitio web oficial https://www.python.org/downloads/
2. Ahora nos vamos a https://my.telegram.org/auth para crear una aplicación. Colocamos nuestro número, después nos llegará un código de confirmación a nuestra cuenta de telegram.
![Iniciar sesión](https://github.com/jric2002/Telegram/blob/master/.images/iniciar-sesion-my-telegram.png)
3. Nos aparecerá esta ventana, le damos click en **API development tools**.
![Entramos a API development tools](https://github.com/jric2002/Telegram/blob/master/.images/iniciar-sesion-my-telegram-2.png)
4. Ingresamos un título y nombre para nuestra aplicación.
![Crear aplicación](https://github.com/jric2002/Telegram/blob/master/.images/create-app.png)
5. Si todo sale bien, nos saldrá una ventana como esta. La **api_id** y **api_hash** es lo que usaremos para inciar sesión desde la terminal.
![Datos de la aplicación](https://github.com/jric2002/Telegram/blob/master/.images/app-telegram.png)
**Nota:** No compartas tu **api_id** y **api_hash** con nadie.
6. Bien, ahora clonamos este repositorio.
```bash
   git clone https://github.com/jric2002/Telegram
```
7. Nos vamos a la carpeta.
```bash
   cd Telegram/modules
```
8. Editamos el archivo `config.json`, reemplazamos los números con nuestra **api_id** y hacemos lo mismo con la **api_hash**.
![Editar el archivo config.json](https://github.com/jric2002/Telegram/blob/master/.images/config-json.png)
9. Bueno, ahora solo nos falta instalar algunos módulos. En esta parte instalaremos los módulos que estan dentro del archivo `requirements.txt`. Si eres desarrollador y sabes como crear un entorno virtual en python, entonces puedes usar **pipenv** y luego instalar los módulos.
```bash
   python -m pip install -r requirements.txt
```
10. Ahora vamos a iniciar sesión con nuestro username, de esta manera.
```bash
   python index.py -u <username>
```
**Nota:** Es importante que tengas un username para poder utilizar los comandos.

# Prueba
Bueno, ahora nos vamos a nuestro Telegram, y si mandamos `.help` en cualquier chat, nos aparecerá el menú de ayuda.
![Probando los comandos](https://github.com/jric2002/Telegram/blob/master/.images/prueba-telegram.png)

## Uso
**Comandos generales**  
Los siguientes comandos solo los puede usar el usuario.  
* **Menú de ayuda**  
  `.help`: Muestra el menú de ayuda.  
  * `.help <comando>`: Ver más detalles acerca del comando.  
* **Conseguir información**  
  `.getinfo`: Consigue información de un usuario, grupo o canal.  
  Flags: `-u` o `--user`, `-t`  
  * `-u` o `--user`: Consigue información de un usuario.  
    Ejemplo: `.getinfo -u <username>` o `.getinfo --user <username>`
  * `-c`: Consigue información de un grupo o canal.  
    Ejemplo: `.getinfo -t <group or channel>`
* **Buscar videos en YouTube**  
  `.yt` o `.youtube`: Busca un video en YouTube y lanza el primer resultado.  
  Ejemplo: `.yt the weeknd blinding lights` o `.youtube the weeknd blinding lights`  
* **Configurar el prefijo**  
  `.setprefix`: Configura un nuevo prefijo para los comandos.  
  Ejemplo: `.setprefix <prefijo>`

## Soporte
Si tienes alguna sugerencia o si ocurre algún problema, puedes dejar tu comentario en la sección de [**Issues**](https://github.com/JRIC2002/Telegram/issues).

## Licencia
Telegram está hecho con 💚 por JRIC2002. Vea el archivo de **Licencia** para más detalles.