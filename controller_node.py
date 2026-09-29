import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, UInt16

class Controller(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.pub = self.create_publisher(UInt16, 'servo_angle', 10)
        self.create_subscription(Float32, 'distance', self.on_distance, 10)

    def on_distance(self, msg):
        d = max(5.0, min(50.0, msg.data))
        angle = int((d - 5) / 45 * 180)
        self.pub.publish(UInt16(data=angle))
        self.get_logger().info(f'distance={msg.data:.1f} cm -> angle={angle}')

def main():
    rclpy.init()
    rclpy.spin(Controller())

if __name__ == '__main__':
    main()
