# Telegram
![Telegram v1.2.0](https://img.shields.io/badge/Telegram-v1.2.0-brightgreen)
![Release stable](https://img.shields.io/badge/Release-stable-brightgreen)
![License GNU General Public License v3.0](https://img.shields.io/badge/License-GNU%20General%20Public%20License%20v3.0-blue)
![Telegram](https://github.com/jric2002/Telegram/blob/master/.images/Telegram.png)

## Información
Con esta sencilla herramienta en python podrás iniciar sesión con tu cuenta de Telegram desde la Terminal y con funciones extra.

## Características
* Iniciar sesión desde terminal
* Funciones extra
* 16 módulos integrados

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

### Prueba
Bueno, ahora nos vamos a nuestro Telegram, y si mandamos `.help` en cualquier chat, nos aparecerá el menú de ayuda.
![Probando los comandos](https://github.com/jric2002/Telegram/blob/master/.images/prueba-telegram.png)

## Uso
**Comandos generales**  
Los siguientes comandos solo los puede usar el usuario.  
* **Menú de ayuda**  
  `.help`: Muestra el menú de ayuda.  
  * `.help <comando>`: Ver más detalles acerca del comando.  
* **Información del servidor**  
  `.serverinfo`: Mostrar información del servidor.
* **Información del usuario**  
  `.getinfo`: Consigue información de un usuario, grupo o canal.  
  Flags: `-u` o `--user`, `-t`  
  * `-u` o `--user`: Consigue información de un usuario.  
    Ejemplo: `.getinfo -u <username>` o `.getinfo --user <username>`
  * `-t`: Consigue información de un grupo o canal.  
    Ejemplo: `.getinfo -t <group or channel>` o `.getinfo -t .`  
    Nota: El `.` indica el actual grupo o canal. 
* **YouTube**  
  `.youtube` o `.yt`: Buscar un video en YouTube y mostrar el primer resultado.  
  Ejemplo: `.youtube the weeknd blinding lights` o `.yt the weeknd blinding lights`  
* **Wikipedia**  
  `.wikipedia` o `.wiki`: Buscar información en Wikipedia.  
  Ejemplo: `.wikipedia gnu linux` o `.wiki gnu linux`  
* **Google**  
  `.google`: Buscar en Google.  
  Ejemplo: `.google windows 10`  
* **Traductor**  
  `.translate`: Traducir texto a otro idioma.  
  Flags : `<lang_code>`  
  * `<lang_code>`: Código del idioma a traducir.  
    Ejemplo: `.translate es Hello world`  
* **Clima**  
  `.weather`: Conseguir datos del clima de una ciudad en http://wttr.in/  
  Ejemplo: `.weather Lima`  
* **Alternativas**  
  `.alternative`: Buscar alternativas a ciertos programas en https://alternativeto.net/  
  Ejemplo: `.alternative google chrome`  
* **Favoritos**  
  `.myfavoriteos` o `mfos`: Ver, agregar y eliminar mis sistemas operativos favoritos.   
  Flags: `-s` o `--show`, `-a` o `--add`, `-d` o `--delete`  
  * `-s` o `--show`: Mostrar mis sistemas operativos favoritos.  
    Ejemplo: `.myfavoriteos -s` o `.myfavoriteos --show`  
  * `-a` o `-add`: Agregar un sistema operativo a Mis Favoritos.  
    Ejemplo: `.myfavoriteos -a <os>` o `.myfavoriteos --add <os>`  
  * `-d` o `--delete`: Eliminar un sistema operativo de Mis Favoritos.  
    Ejemplo: `.myfavoriteos -d <os>` o `.myfavoriteos --delete <os>`  
* **Hacker**  
  `.hackear`: Es una broma, intentalo.  
  Ejemplo: `.hackear`  
* **Bloquear**  
  `.block`: Bloquear a un usuario.  
  Ejemplo: `.block <username>`  
* **Desbloquear**  
  `.unblock`: Desbloquear a un usuario.  
  Ejemplo: `.unblock <username>`  
* **Seguridad**  
  `.security`: Activar o desactivar medidas de seguridad.  
  Flags: `-a` o `--activate`, `-d` o `--desactivate`  
  * `-a` o `--activate`: Activar medidas de seguridad.  
    Ejemplo: `.security -a` o `.security --activate`  
  * `-d` o `--desactivate`: Desactivar medidas de seguridad.  
    Ejemplo: `.security -d` o `.security --desactivate`  
* **Prefijo de los comandos**  
  `.setprefix`: Configura un nuevo prefijo para los comandos.  
  Ejemplo: `.setprefix <prefijo>`  

### Funciones en desarrollo
* **Idioma**  
  `.setlanguage`: Establecer un nuevo idioma.  
  Ejemplo: `.setlanguage <lang_code>`  
**Nota:** Esta función esta en desarrollo; solo afecta a algunas funciones.

## Soporte
Si tienes alguna sugerencia o si ocurre algún problema, puedes dejar tu comentario en la sección de [**Issues**](https://github.com/jric2002/Telegram/issues).

## Licencia
Telegram está hecho con 💚 por **José Rodolfo**. Vea el archivo de **Licencia** para más detalles.