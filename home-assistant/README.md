# Trydan Home-Assistant:

Esta integración de Home Assistant te permite conectarte a tu e-charger, para poder monitorizar los valores del cargador y también mandar nuevos valores.
Es importante que estéis conectados al mismo internet que el Trydan, funciona mediante Modbus-Tcp.

## Configuration:
Primero descarga estos ficheros, tienen el código de la integración: [Aqui](https://github.com/V2Charge/Trydan_Modbus_TCP/tree/main/home-assistant/custom_components/v2c)
<br>![arch](https://user-images.githubusercontent.com/121380348/231111804-25bfff86-c44a-4e09-8353-d55e7dd7d535.png)</br>

Una vez estes en tu Home Assistant y tengas instalada la extensión de Studio Code Server. 
![visual](https://user-images.githubusercontent.com/121380348/231114227-ee6d0d12-4218-4dd5-a85c-87ccf4917153.png)

Al abrirla pordás ver que hay un conjunto de ficheros por defecto, para instalar la integración del Trydan en vuestro Home Assistant: <br>
- Añadir un fichero 'v2c' dentro de la carpeta 'custom_components' y pega todos los archivos que has descargado antes.

<br>![ficheros](https://user-images.githubusercontent.com/121380348/231093952-1cc5099c-d1a2-4777-877c-3e5b39b30327.png) </br>




Además, hay que configurar el archivo 'configuration.yaml': <br>
- Para configurar este archivo, solo tenéis que copiar el propio archivo configuration.yaml, también lo que podéis hacer es pegar el siguiente contenido:
- Donde pone 'host' hay que poner la ip del Trydan, el trydan tiene que estar conectado al mismo internet que tu ordenador.

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

## Dashboard:

Este sería el resultado del panel para mandar valores, WRITE HOLDING REGISTER :
<br>![panel_control](https://user-images.githubusercontent.com/121380348/231107807-64d40d2e-5906-4a31-bfe3-bbc950b7cb4b.png)</br>

Como quedarían las entidades de lectura, READ HOLDING REGISTER :
<br>![sensor](https://user-images.githubusercontent.com/121380348/231108758-9c03df67-590e-45b2-9a42-8bb06e5f89e4.png) </br>
