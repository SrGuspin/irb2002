"""
Nodo PUBLISHER: mueve el TurtleBot3 publicando en el topico /cmd_vel.

Este es el ejemplo minimo de un publisher en ROS 2:
  1. Creamos un nodo.
  2. Creamos un publisher hacia un topico, con un tipo de mensaje.
  3. Un timer llama periodicamente a una funcion que publica.

Nota sobre Jazzy: algunos paquetes migraron /cmd_vel del tipo Twist al tipo
TwistStamped (que es lo mismo, pero con un encabezado de tiempo). Por eso el
nodo tiene un parametro 'usar_stamped'. Antes de correrlo, verifica el tipo
real con:  ros2 topic info /cmd_vel -v
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped


class MoverRobot(Node):

    def __init__(self):
        # El nombre que pasamos aqui es el que veras en 'ros2 node list'
        super().__init__('mover_robot')

        # --- Parametros ---------------------------------------------------
        # Los parametros permiten cambiar el comportamiento del nodo sin
        # tocar el codigo. Se pueden modificar al lanzarlo con --ros-args.
        self.declare_parameter('velocidad_lineal', 0.15)   # metros/segundo
        self.declare_parameter('velocidad_angular', 0.30)  # radianes/segundo
        self.declare_parameter('usar_stamped', True)
        self.declare_parameter('topico', '/cmd_vel')

        self.vel_lineal = self.get_parameter('velocidad_lineal').value
        self.vel_angular = self.get_parameter('velocidad_angular').value
        self.usar_stamped = self.get_parameter('usar_stamped').value
        topico = self.get_parameter('topico').value

        # --- Publisher ----------------------------------------------------
        # El "10" es el tamano de la cola de mensajes (QoS depth).
        tipo_msg = TwistStamped if self.usar_stamped else Twist
        self.publisher = self.create_publisher(tipo_msg, topico, 10)

        # --- Timer --------------------------------------------------------
        # Publicamos 10 veces por segundo. Si dejamos de publicar, el robot
        # eventualmente se detiene por seguridad.
        self.timer = self.create_timer(0.1, self.publicar_velocidad)

        self.get_logger().info(
            f'Nodo iniciado. Publicando {tipo_msg.__name__} en {topico} | '
            f'lineal={self.vel_lineal} m/s, angular={self.vel_angular} rad/s'
        )

    def publicar_velocidad(self):
        """Construye y publica un mensaje de velocidad."""
        if self.usar_stamped:
            msg = TwistStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'base_link'
            msg.twist.linear.x = self.vel_lineal
            msg.twist.angular.z = self.vel_angular
        else:
            msg = Twist()
            # linear.x  = avanzar / retroceder
            # angular.z = girar sobre su propio eje
            # El TurtleBot3 es diferencial: solo usa estos dos campos.
            msg.linear.x = self.vel_lineal
            msg.angular.z = self.vel_angular

        self.publisher.publish(msg)

    def detener(self):
        """Publica velocidad cero para que el robot no siga moviendose."""
        if self.usar_stamped:
            msg = TwistStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
        else:
            msg = Twist()
        self.publisher.publish(msg)
        self.get_logger().info('Robot detenido.')


def main(args=None):
    rclpy.init(args=args)
    nodo = MoverRobot()
    try:
        # spin() bloquea y procesa callbacks (timers, subscripciones)
        # hasta que se interrumpa con Ctrl+C.
        rclpy.spin(nodo)
    except KeyboardInterrupt:
        pass
    finally:
        nodo.detener()
        nodo.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
