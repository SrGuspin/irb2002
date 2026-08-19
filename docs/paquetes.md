# Paquetes de ROS 2

Ahora, para crear sus propios códigos, paquetes y algoritmos, deben crear su paquete de ROS 2.

## Dónde trabajar

Este repo **ya es un workspace de colcon**: la carpeta que clonaron tiene un `src/` adentro, que
es todo lo que colcon necesita. No hay que crear nada.

```bash
cd ~/irb2002
ls src/          # mi_paquete
```

> El nombre de la carpeta es libre. Si prefieren `~/ros2_ws` o `~/lo_que_sea`, funciona igual;
> en esta guía la llamamos `~/irb2002` y ustedes reemplazan por la suya.

El `src/mi_paquete` que viene en el repo es **material de lectura**: está para que lo lean, lo
corran y le copien lo que necesiten. Su propio paquete lo crean **al lado y con otro nombre**,
para que no choquen dos paquetes que se llamen igual.

## Crear su paquete

> En Jazzy el argumento `--license` es prácticamente obligatorio: sin él, `colcon build`
> emite un warning en cada compilación.

```bash
cd ~/irb2002/src
ros2 pkg create --build-type ament_python --license Apache-2.0 mi_primer_paquete
```

Con dependencias declaradas desde el inicio:

```bash
ros2 pkg create mi_primer_paquete --build-type ament_python --license Apache-2.0 --dependencies rclpy std_msgs
```

Estructura generada:

```text
mi_primer_paquete/
├── LICENSE                 # lo genera el argumento --license
├── mi_primer_paquete/
│   └── __init__.py         # aquí van los .py de tus nodos
├── package.xml             # metadatos y dependencias
├── resource/
│   └── mi_primer_paquete
├── setup.cfg
├── setup.py                # instalación y entry points
└── test/                   # linters que corre `colcon test`
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

## setup.py

Este archivo declara dos cosas críticas: registrar ejecutables e instalar la carpeta de launch files.

La parte más destacable para esta guía es el `entry_points`. Así lo declara el paquete de
ejemplo del repo:

```python
    entry_points={
        'console_scripts': [
            'mover = mi_paquete.mover_robot:main',
            'lidar = mi_paquete.leer_lidar:main',
        ],
    },
```

Esta entrada nos da los dos comandos a usar en `ros2 run`; sin ella, `mover` y `lidar` no tienen ningún significado.

## Compilar

```bash
cd ~/irb2002

rosdep install -i --from-path src --rosdistro jazzy -y   # instala dependencias
colcon build --symlink-install                            # compila todo
colcon build --packages-select mi_primer_paquete          # solo un paquete
```

Compilen **siempre desde la raíz del workspace** (`~/irb2002`), nunca desde `src/`.

### Cargar los overlays

Esta es la parte que más problemas causa. Tienen **tres capas**, y cada una se apoya en la
anterior:

| Capa | Qué aporta | Cómo se carga |
|---|---|---|
| ROS 2 Jazzy (*underlay*) | `rclpy`, los comandos `ros2 ...`, los mensajes | `source /opt/ros/jazzy/setup.bash` |
| `~/turtlebot3_ws` | el robot y los mundos de Gazebo | `source ~/turtlebot3_ws/install/setup.bash` |
| `~/irb2002` | `mi_paquete` y el paquete de ustedes | `source ~/irb2002/install/setup.bash` |

**El orden importa**: van siempre de arriba hacia abajo. Si cargan la suya antes que Jazzy, no
encuentra nada.

Si corrieron el [`setup_entorno.sh`](setup_entorno.sh), las dos primeras capas ya quedaron en el
`.bashrc` y sólo les falta la tercera:

```bash
source ~/irb2002/install/setup.bash
```

> Hay que cargar el overlay **en cada terminal nueva**, o lo agregan al final del `.bashrc` como
> las otras dos.

Si el `ros2 launch` les responde `PackageNotFoundError: turtlebot3_gazebo`, es exactamente esto:
les falta la segunda capa.

## Ejecutar

```bash
ros2 run mi_paquete mover
ros2 run mi_paquete lidar
```

> Hay dos códigos de ejemplo, `mover` y `lidar`:
>
> - `mover`: simplemente hace que el robot gire en círculos.
> - `lidar`: lee el LiDAR y entrega algunos datos :D

(deben correr antes el simulador mostrado en [instalacion.md](instalacion.md) :p)

Como generalmente uno quiere correr varios nodos o cosas a la vez, ¡tenemos los archivos launch!

```bash
ros2 launch mi_paquete demo.launch.py
```
