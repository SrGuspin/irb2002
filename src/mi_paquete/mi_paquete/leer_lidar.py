"""
Nodo SUBSCRIBER: lee el LiDAR del TurtleBot3 desde el topico /scan.

Este es el ejemplo minimo de un subscriber en ROS 2:
  1. Creamos un nodo.
  2. Nos suscribimos a un topico indicando el tipo de mensaje y un callback.
  3. El callback se ejecuta automaticamente cada vez que llega un mensaje.

El TurtleBot3 Burger trae un LiDAR 2D de 360 grados. Cada mensaje LaserScan
contiene un arreglo con cientos de distancias, una por cada angulo.
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan

from intro_ros2.utiles import distancia_en_angulo, formatear_distancia


class LeerLidar(Node):

    def __init__(self):
        super().__init__('leer_lidar')

        self.declare_parameter('topico', '/scan')
        self.declare_parameter('periodo_impresion', 1.0)  # segundos

        topico = self.get_parameter('topico').value
        self.periodo = self.get_parameter('periodo_impresion').value

        # --- Subscriber ---------------------------------------------------
        # IMPORTANTE: los sensores publican con un perfil de QoS distinto al
        # de por defecto (usan BEST_EFFORT en vez de RELIABLE). Si usas el
        # QoS por defecto, el callback nunca se ejecuta y no aparece ningun
        # error. Por eso usamos qos_profile_sensor_data.
        self.subscription = self.create_subscription(
            LaserScan,
            topico,
            self.callback_scan,
            qos_profile_sensor_data
        )

        self.ultimo_msg = None

        # Imprimimos con un timer en vez de dentro del callback, porque el
        # LiDAR publica ~5 veces por segundo y saturaria la consola.
        self.timer = self.create_timer(self.periodo, self.imprimir_lectura)

        self.get_logger().info(f'Nodo iniciado. Escuchando {topico}...')

    def callback_scan(self, msg):
        """Se ejecuta cada vez que llega un mensaje del LiDAR."""
        self.ultimo_msg = msg

    def imprimir_lectura(self):
        """Muestra las distancias en cuatro direcciones clave."""
        if self.ultimo_msg is None:
            self.get_logger().warn('Aun no llegan datos del LiDAR...')
            return

        msg = self.ultimo_msg

        frente = distancia_en_angulo(msg, 0)
        izquierda = distancia_en_angulo(msg, 90)
        derecha = distancia_en_angulo(msg, -90)
        atras = distancia_en_angulo(msg, 180)

        self.get_logger().info(
            f'Frente: {formatear_distancia(frente)} | '
            f'Izq: {formatear_distancia(izquierda)} | '
            f'Der: {formatear_distancia(derecha)} | '
            f'Atras: {formatear_distancia(atras)} | '
            f'({len(msg.ranges)} mediciones por barrido)'
        )


def main(args=None):
    rclpy.init(args=args)
    nodo = LeerLidar()
    try:
        rclpy.spin(nodo)
    except KeyboardInterrupt:
        pass
    finally:
        nodo.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
