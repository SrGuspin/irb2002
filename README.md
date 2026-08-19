# IRB2002 — Cápsula de introducción a ROS 2

Material del curso **IRB2002 (2026-2)**: una introducción práctica a ROS 2 Jazzy usando un
TurtleBot3 simulado en Gazebo.

> Esta cápsula tiene como objetivo **introducirlos** a ROS 2. **No es un reemplazo del curso
> de Robótica Móvil.**

## Cómo usar este repo

Este repo **es un workspace de colcon**, así que se clona y se trabaja adentro:

```bash
git clone https://github.com/SrGuspin/irb2002.git ~/irb2002
cd ~/irb2002
```

El nombre de la carpeta es libre — si prefieren otro, sólo reemplacen `~/irb2002` en el resto
de la documentación.

> [`src/mi_paquete/`](src/mi_paquete) es **material de lectura**. Está para que lo lean, lo
> corran y le copien lo que necesiten. El paquete de ustedes va **al lado, con otro nombre**,
> siguiendo [`docs/paquetes.md`](docs/paquetes.md); si ambos se llaman igual, ROS no sabe cuál
> ejecutar.

El simulador vive en un workspace aparte (`~/turtlebot3_ws`, lo crea
[`docs/setup_entorno.sh`](docs/setup_entorno.sh)). Cómo se encadenan los dos está explicado en
[Cargar los overlays](docs/paquetes.md#cargar-los-overlays).

## Requisitos

- Ubuntu 24.04
- ROS 2 Jazzy — instalar `ros-jazzy-desktop` (no la versión *bare bones*, y nunca las dos a la vez)
- Gazebo + los paquetes de TurtleBot3

Todo el detalle está en [`docs/instalacion.md`](docs/instalacion.md).

## Contenido

| Archivo | De qué trata |
|---|---|
| [`docs/instalacion.md`](docs/instalacion.md) | Instalar ROS 2 Jazzy, configurar el entorno y el simulador |
| [`docs/basics.md`](docs/basics.md) | Conceptos base: nodos, tópicos, servicios, acciones y parámetros |
| [`docs/paquetes.md`](docs/paquetes.md) | Crear tu propio paquete, compilarlo con `colcon` y ejecutarlo |
| [`docs/setup_entorno.sh`](docs/setup_entorno.sh) | Script que instala Gazebo y clona los paquetes de TurtleBot3 |
| [`src/mi_paquete/`](src/mi_paquete) | Paquete de ejemplo (material de lectura): nodo publisher, nodo subscriber y un launch file |

## Uso rápido

Compilar desde la raíz del workspace (nunca desde `src/`) y cargar el overlay:

```bash
cd ~/irb2002
colcon build --packages-select mi_paquete
source install/setup.bash
```

Esto asume que ROS 2 y `~/turtlebot3_ws` ya están cargados; si no, ver
[Cargar los overlays](docs/paquetes.md#cargar-los-overlays).

Ejecutar el nodo que mueve el robot (el simulador debe estar corriendo, ver
[`docs/instalacion.md`](docs/instalacion.md)):

```bash
ros2 run mi_paquete mover
```

O lanzar el simulador y el nodo juntos:

```bash
ros2 launch mi_paquete demo.launch.py
```

## Licencia

- **Código** (`src/`): [Apache-2.0](LICENSE)
- **Documentación** (`docs/`): [CC BY 4.0](docs/LICENSE)
