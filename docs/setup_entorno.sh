#!/usr/bin/env bash
#
# Instala todo lo necesario para correr la capsula en Ubuntu 24.04 + ROS 2 Jazzy.
# Uso:  ./setup_entorno.sh
#
# Este script asume que ROS 2 Jazzy YA esta instalado. Si no lo tienes:
#   https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

set -e  # abortar si cualquier comando falla

WS=~/turtlebot3_ws

echo "=== 1/5  Verificando ROS 2 Jazzy ==="
if [ ! -f /opt/ros/jazzy/setup.bash ]; then
    echo "ERROR: no encuentro ROS 2 Jazzy en /opt/ros/jazzy"
    echo "Instalalo primero siguiendo la documentacion oficial."
    exit 1
fi
source /opt/ros/jazzy/setup.bash
echo "OK - ROS 2 Jazzy encontrado"

echo "=== 2/5  Instalando Gazebo Harmonic y dependencias ==="
sudo apt update
sudo apt install -y \
    ros-jazzy-ros-gz \
    ros-jazzy-teleop-twist-keyboard \
    ros-jazzy-rqt-common-plugins \
    ros-jazzy-rviz2 \
    python3-colcon-common-extensions \
    git

echo "=== 3/5  Clonando paquetes de TurtleBot3 (rama jazzy) ==="
mkdir -p $WS/src
cd $WS/src

# NOTA: para que la grabacion siga funcionando a futuro, conviene
# fijar el commit exacto. Despues de verificar que todo corre, ejecuta
# 'git rev-parse HEAD' en cada repo y reemplaza la rama por ese commit.
[ -d turtlebot3 ]             || git clone -b jazzy https://github.com/ROBOTIS-GIT/turtlebot3.git
[ -d turtlebot3_msgs ]        || git clone -b jazzy https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
[ -d turtlebot3_simulations ] || git clone -b jazzy https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git

echo "=== 4/5  Compilando el workspace ==="
cd $WS
rosdep install --from-paths src --ignore-src -r -y || true
colcon build --symlink-install

echo "=== 5/5  Configurando el .bashrc ==="
# TURTLEBOT3_MODEL es obligatorio: sin el, los launch no saben que robot cargar
grep -q "TURTLEBOT3_MODEL" ~/.bashrc || echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
grep -q "source /opt/ros/jazzy" ~/.bashrc || echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
grep -q "turtlebot3_ws/install" ~/.bashrc || echo "source $WS/install/setup.bash" >> ~/.bashrc

echo ""
echo "======================================================"
echo " LISTO. Abre una terminal NUEVA y prueba con:"
echo "   ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py"
echo "======================================================"
