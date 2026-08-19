# Paquetes de ROS 2

Ahora, para crear sus propios códigos, paquetes y algoritmos, deben crear su paquete de ROS 2.

Primer paso:

Crear carpeta donde vamos a trabajar

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

Segundo paso: crear paquete de python

> En Jazzy el argumento `--license` es prácticamente obligatorio: sin él, `colcon build`
> emite un warning en cada compilación.

```bash
ros2 pkg create --build-type ament_python --license Apache-2.0 mi_paquete
```

Con dependencias declaradas desde el inicio:

```bash
ros2 pkg create mi_paquete --build-type ament_python --license Apache-2.0 --dependencies rclpy std_msgs
```

Estructura generada:

```text
mi_paquete/
├── LICENSE                 # lo genera el argumento --license
├── mi_paquete/
│   └── __init__.py         # aquí van los .py de tus nodos
├── package.xml             # metadatos y dependencias
├── resource/
│   └── mi_paquete
├── setup.cfg
├── setup.py                # instalación y entry points
└── test/                   # linters que corre `colcon test`
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

## setup.py

Este archivo declara dos cosas críticas: registrar ejecutables e instalar la carpeta de launch files.

La parte más destacable para esta guía es el `entry_points`:

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
cd ~/ros2_ws

rosdep install -i --from-path src --rosdistro jazzy -y   # instala dependencias
colcon build --symlink-install                            # compila todo
colcon build --packages-select mi_paquete                 # solo un paquete
```

Compilen **siempre desde la raíz del workspace** (`~/ros2_ws`), nunca desde `src/`.

### Cargar el overlay

```bash
source ~/ros2_ws/install/setup.bash
```

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
