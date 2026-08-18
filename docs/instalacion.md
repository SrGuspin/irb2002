# IRB2002-2026-2

Esta capsula tiene como objetivo **introducirlos** a ROS2, NO ES UN REEMPLAZO DEL CURSO ROBOTICA MOVIL!!

## INSTALAR ROS2  

Esta guia requiere usar Ubuntu 24.04 y vamos a instalar ROS2 Jazzy.
Esto es porque es más facil y rapido :)
Pueden usar dual boot con windows si quieren...

instalar ros2 es tan simple como seguir estos links
<https://docs.ros.org/en/jazzy/Installation.html>

### importante

INSTALAR SOLO ros-jazzy-desktop nO LA VERSIÓN BARE BONES, es la recomendada, no necesitan la otra. Y tampoco pueden estar las 2 a la vez.

### Ambiente

Si se fijan, en los comandos ejemplo les pone ` source /opt/ros/jazzy/setup.bash ` En todas las lineas antes de usar ros2. Esto es para que en la siguiente linea usar `ros2 ...` no les de ningun error.

Por esto mismo, para ahorrarnos tiempo, podemos agregarlo a nuestra raiz.
Por lo que en nuestra ruta raiz hacemos esto

```bash
cd
nano .bashrc
# Ponen: source /opt/ros/jazzy/setup.bash 
# en la ultima fila y guardan.
```

Despues cuando **ABRAN UNA NUEVA TERMINAL** tendran ros2 al tiro :)
pd: verifique el funcionamiento con los ejemplos de la pagina.

## Instalar simulador

El simulador ya viene instalado! Es gazebo, pero nos falta el modelo del robot y el mundo en el que trabajaremos. Por esto usaremos:
<https://docs.robotis.com/docs/systems/turtlebot3/simulation/gazebo_simulation>
Ahí estan las instrucciones de como instalarlo USAR JAZZY!!! RECORDAR!!

Tambien pueden usar el setup_entorno.sh, cortesia de Claude Opus para instalarlo :)
Se ejecuta con `bash -x setup_entorno.sh`
Este define el model y mundo a usar.
