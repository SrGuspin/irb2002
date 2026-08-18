# IRB2002 — Cápsula de introducción a ROS 2

Material del curso **IRB2002 (2026-2)**: una introducción práctica a ROS 2 Jazzy usando un
TurtleBot3 simulado en Gazebo.

> Esta cápsula tiene como objetivo **introducirlos** a ROS 2. **No es un reemplazo del curso
> de Robótica Móvil.**

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
| [`src/mi_paquete/`](src/mi_paquete) | Paquete de ejemplo: nodo publisher, nodo subscriber y un launch file |

## Uso rápido

Compilar el paquete desde la raíz del workspace (nunca desde `src/`):

```bash
colcon build --packages-select mi_paquete
source install/setup.bash
```

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
