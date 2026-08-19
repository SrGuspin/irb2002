# Instalación de ROS 2 y el simulador

Esta cápsula tiene como objetivo **introducirlos** a ROS 2. ¡NO ES UN REEMPLAZO DEL CURSO DE ROBÓTICA MÓVIL!

## Instalar ROS 2

Esta guía requiere usar Ubuntu 24.04 y vamos a instalar ROS 2 Jazzy.
Esto es porque es más fácil y rápido :)
Pueden usar dual boot con Windows si quieren...

Instalar ROS 2 es tan simple como seguir este link:
<https://docs.ros.org/en/jazzy/Installation.html>

### Importante

INSTALAR SOLO `ros-jazzy-desktop`, NO LA VERSIÓN BARE BONES: es la recomendada, no necesitan la otra. Y tampoco pueden estar las 2 a la vez.

### Ambiente

Si se fijan, en los comandos de ejemplo les pone `source /opt/ros/jazzy/setup.bash` en todas las líneas antes de usar ros2. Esto es para que en la siguiente línea usar `ros2 ...` no les dé ningún error.

Por esto mismo, para ahorrarnos tiempo, podemos agregarlo a nuestra carpeta personal (*home*).
Por lo que en nuestra carpeta personal hacemos esto:

```bash
cd
nano .bashrc
# Ponen: source /opt/ros/jazzy/setup.bash
# en la última línea y guardan.
```

Después, cuando **ABRAN UNA NUEVA TERMINAL**, tendrán ros2 al tiro :)

PD: verifiquen el funcionamiento con los ejemplos de la página.

## Instalar simulador

¡Tenemos que instalar el simulador! Es Gazebo, pero también nos falta el modelo del robot y el mundo en el que trabajaremos. Por esto usaremos:
<https://docs.robotis.com/docs/systems/turtlebot3/simulation/gazebo_simulation>
Ahí están las instrucciones de cómo instalarlo. ¡USAR JAZZY! ¡RECORDAR!

> **Ojo piojo:**
>
> El script de configuración define automáticamente la variable `TURTLEBOT3_MODEL` en el `.bashrc`.
> De no usar el script, tengan ojo con esto.
> Para ahorrarse problemas, usen el script nomás :)

También pueden usar el [`setup_entorno.sh`](setup_entorno.sh), cortesía de Claude Opus, para instalarlo :)
Se ejecuta con `bash setup_entorno.sh`
Este define el modelo y mundo a usar.
