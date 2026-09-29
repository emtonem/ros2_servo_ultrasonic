import rclpy, serial
from rclpy.node import Node
from std_msgs.msg import Float32, UInt16

class Bridge(Node):
    def __init__(self):
        super().__init__('bridge_node')
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.05)
        self.pub = self.create_publisher(Float32, 'distance', 10)
        self.create_subscription(UInt16, 'servo_angle', self.on_angle, 10)
        self.create_timer(0.05, self.read_serial)

    def on_angle(self, msg):
        self.ser.write(f"{msg.data}\n".encode())

    def read_serial(self):
        line = self.ser.readline().decode(errors='ignore').strip()
        try:
            self.pub.publish(Float32(data=float(line)))
        except ValueError:
            pass

def main():
    rclpy.init()
    rclpy.spin(Bridge())

if __name__ == '__main__':
    main()
