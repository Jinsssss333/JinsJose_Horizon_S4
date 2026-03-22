import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        # Create a publisher that sends Int32 messages to the '/distance' topic
        self.publisher_ = self.create_publisher(Int32, 'distance', 10)
        # Set a timer to call the function every 1.0 seconds
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        # Generate a random distance between 10 and 100 cm
        msg.data = random.randint(10, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sensor reading: {msg.data} cm')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
