# ROS 2

ROS 2 significa Robot Operating System 2. Su aporte principal es dejar que escribas programas pequeños e independientes (nodos) que se comunican entre sí por la red sin que tengas que programar sockets, serialización ni descubrimiento.

Es importante cambiar el `ROS_DOMAIN_ID` si saben que están en una red con varios equipos corriendo ROS 2: todos deben tener el mismo ID para que puedan descubrirse entre sí. Ejemplo en `.bashrc`:

```bash
export ROS_DOMAIN_ID=42
```

## Nodos

Los nodos consisten en procesos que hacen **una** tarea específica. La gracia de ROS es tener muchos nodos pequeños en vez de un código ilegible de 50000 líneas.

### Los cuatro mecanismos de comunicación

| Mecanismo | Patrón | Cuándo usarlo |
|---|---|---|
| **Tópico** | Publish/Subscribe, muchos-a-muchos, asíncrono | Flujos continuos: sensores, odometría, comandos de velocidad |
| **Servicio** | Request/Response, uno-a-uno, bloqueante | Consultas puntuales y rápidas: "¿cuál es tu estado?", "reinicia el contador" |
| **Acción** | Goal/Feedback/Result, cancelable | Tareas largas con progreso: "navega a este punto", "mueve el brazo" |
| **Parámetro** | Configuración clave-valor por nodo | Ajustes: velocidad máxima, ruta de un archivo, modo de operación |

**Cómo decidir:**

- ¿Es un flujo continuo de datos sin respuesta? → **Tópico**
- ¿Necesitas una respuesta y tarda milisegundos? → **Servicio**
- ¿Necesitas una respuesta, tarda segundos/minutos y quieres poder cancelar? → **Acción**
- ¿Es un valor de configuración que cambia poco? → **Parámetro**

### Inspeccionar los tópicos

Hay varias formas de visualizar nuestro sistema: CLI o GUI. Por CLI tenemos que hacer lo siguiente (esta es la visualización de nuestro simulador):

```bash
ros2 topic list
```

```text
/clock
/cmd_vel
/imu
/joint_states
/odom
/parameter_events
/robot_description
/rosout
/scan
/tf
/tf_static
```

Ahora podemos obtener la info de los tópicos. Por ejemplo, la info de `/cmd_vel`:

```bash
ros2 topic info /cmd_vel
```

```text
Type: geometry_msgs/msg/TwistStamped
Publisher count: 0
Subscription count: 1
```

¡Esto nos da información muy útil!

1. Tipo de mensaje, importante cuando queramos enviar mensajes en el tópico
2. Cuántos nodos están publicando en este tópico
3. Cuántos nodos están suscritos al tópico (leyendo)

También podemos escuchar el tópico con:

```bash
ros2 topic echo /topico
```

También podemos ver lo mismo para los nodos con:

```bash
ros2 node list
ros2 node info [cualquier nodo que les salga :p]
```

Para ver los tópicos/nodos/grafos/mensajes, etc., pueden usar `rqt`, una herramienta visual que dispone de muchas opciones para sus gustos.
