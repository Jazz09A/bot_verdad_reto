
# Bot de Verdad o Reto para Telegram

Este es un bot de Telegram que permite jugar al clásico juego de "Verdad o Reto" con tus amigos. Los jugadores pueden unirse al juego, elegir entre preguntas de verdad o retos, y disfrutar de una experiencia interactiva a través de botones.

## Características

- Registro de múltiples jugadores por chat
- Selección aleatoria de jugadores
- Preguntas de "Verdad" y retos predefinidos
- Interfaz interactiva con botones (para elegir jugadores y opciones)
- Fácil de usar, solo interactúa con comandos y botones

## Configuración

### 1. Instala las dependencias:
Asegúrate de tener Python 3.8 o superior instalado. Luego, instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

### 2. Configura el token del bot:
   - Obtén un token de bot de Telegram a través de [@BotFather](https://t.me/BotFather).
   - crea el archivo `config.py` y añade el token de tu bot de Telegram en el archivo.

### 3. Ejecuta el bot:
   Inicia el bot ejecutando el siguiente comando en la terminal:

```bash
python bot.py
```

## Cómo jugar

1. **Inicia el bot** con el comando `/start`. El bot te dará la bienvenida y te pedirá que ingreses los nombres de los jugadores.
2. **Cada jugador se une** escribiendo su nombre en el chat.
3. Cuando todos los jugadores estén listos, usa el comando **`/listo`** para comenzar el juego.
4. Durante el juego, el bot **elegirá a un jugador al azar** y le dará la opción de escoger entre una pregunta de **Verdad** o un **Reto**.
5. El bot **muestra las opciones** en botones interactivos, y el jugador elige entre ellas.
6. El juego continúa hasta que se terminen los jugadores o se decida finalizar el juego.

## Comandos disponibles

- `/start` - Inicia el bot y prepara un nuevo juego. Pide los nombres de los jugadores.
- `/listo` - Indica que todos los jugadores están listos para comenzar el juego.


## Estructura del código

- `bot.py`: El archivo principal que ejecuta el bot.
- `verdades_y_retos.json`: Archivo que contiene las preguntas de verdad y los retos.(No subidos a github)
- `config.py`: Archivo donde configuras el token del bot.

## Notas

- El bot permite múltiples jugadores por chat y selecciona aleatoriamente a un jugador en cada turno.
- Puedes personalizar las preguntas de "Verdad" y los "Retos" editando el archivo `verdades_y_retos.json`.(No subidos en el github)
- Asegúrate de tener el archivo `config.py` correctamente configurado con el token de tu bot de Telegram.

## Contribuciones

Si deseas contribuir al proyecto, siéntete libre de abrir un "issue" o enviar un "pull request". Cualquier mejora es bienvenida.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.


### Cambios importantes:
1. **Configuración**: Se añadió información sobre cómo crear el archivo `.env` y configurar el token del bot.
2. **Comandos**: Se agregaron detalles sobre los comandos, como `/start`, `/listo`, y el proceso de juego.
3. **Estructura**: Se explicó la estructura de archivos del proyecto para mayor claridad.

Este README es más detallado, incluye instrucciones claras y facilita la configuración del bot para cualquier usuario que quiera usarlo o contribuir al proyecto.