## Configuration:

Una vez estes en tu Home Assistant y tengas instalada la extensión de Studio Code Server. 
<br>![studio](https://user-images.githubusercontent.com/121380348/231089281-02486875-5531-42dd-b493-b18654ff2093.png) </br>

Al abrirla pordás ver que hay un conjunto de ficheros por defecto:<br>
Para instalar la integración del Trydan en vuestro Home Assistant, tendréis que descargar el código:
Añadir el fichero 'v2c' dentro de la carpeta 'custom_components'.
<br>![ficheros](https://user-images.githubusercontent.com/121380348/231093952-1cc5099c-d1a2-4777-877c-3e5b39b30327.png) </br>


Además, hay que configurar el archivo 'configuration.yaml':
Para configurar este archivo, solo tenéis que copiar el propio archivo configuration.yaml, también lo que podéis hacer es pegar el siguiente contenido:
Donde pone 'host' hay que poner la ip del Trydan, el trydan tiene que estar conectado al mismo internet que tu ordenador.

```yaml
v2c:
  host: "XXXXXXXX"

input_text:
  my_input_text:
    name: "Escribe el número:"
    initial: ""
    max: 20

input_number:
  my_input_number:
    max: 32
    min: 6
    name: "Intensity"
    mode: slider
    unit_of_measurement: A

input_boolean:
  lock_switch:
    name: "Lock state:"
  pause_switch:
    name: "Pause state:"

input_select:
  my_list:
    name: My List
    options:
      - "Program:"
      - "Dynamic:"
      - "Payment:"
      - "OCPP:"
      - "Min Intensity:"
      - "Max Intensity:"
      - "Pause Dynamic:"
      - "Dynamic Power Mode:"
      - "Contracted Power:"
```
Lo que hacemos es pasarle al código el parametro de la ip para que pueda conectarse y configurar el panel de control para cambiar valores del trydan desde el dashboard.
Este sería el resultado del panel de control:
<br>![panel_control](https://user-images.githubusercontent.com/121380348/231107807-64d40d2e-5906-4a31-bfe3-bbc950b7cb4b.png)</br>

Como quedarían los valores es:
<br>![sensor](https://user-images.githubusercontent.com/121380348/231108758-9c03df67-590e-45b2-9a42-8bb06e5f89e4.png) </br>
