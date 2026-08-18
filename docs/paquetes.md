# Paquetes de ros2

Ahora, para crear sus propios codigos, paquetes y algoritmos deben de crear su paquete de ros2.

Primer paso:

Crear carpeta donde vamos a trabajar

```bash
mkdir -p ~/ros2_ws/src
cd cd ~/ros2_ws/src
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

```
mi_paquete/
├── mi_paquete/
│   └── __init__.py        # aquí van los .py de tus nodos
├── resource/
│   └── mi_paquete
├── test/
├── package.xml            # metadatos y dependencias
├── setup.py               # instalación y entry points
└── setup.cfg
```

## setup.py

Este archivo declara dos cosas criticas: registrar ejecutables e instalar la carpeta de launch files.

## Compilar

```bash
cd ~/ros2_ws

rosdep install -i --from-path src --rosdistro jazzy -y   # instala dependencias
colcon build --symlink-install                            # compila todo
colcon build --packages-select mi_paquete                 # solo un paquete
```

Compila **siempre desde la raíz del workspace** (`~/ros2_ws`), nunca desde `src/`.

### Cargar el overlay

```bash
source ~/ros2_ws/install/setup.bash
```

## Ejecutar

```bash
ros2 run mi_paquete mover
```

(deben de correr antes el simulador mossstrado en instalacion.md :p)

Como generalmente uno quiere correr varios nodos o cosas a la vez, tenemos los archivos launch!

```bash

ros2 launch mi_paquete demo.launch.py

```
