import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class RoverBrain(Node):
    def __init__(self):
        super().__init__('rover_brain')
        
        self.distance_sub = self.create_subscription(Int32, 'distance', self.process_sensor_data, 10)
        self.command_pub = self.create_publisher(String, 'rover_command', 10)

    def process_sensor_data(self, msg):
        current_distance = msg.data
        
        if current_distance < 30:
            status = "STOP"
        else:
            status = "MOVE_FORWARD"

        decision = String()
        decision.data = status
        
        self.command_pub.publish(decision)
        self.get_logger().info(f'Distance: {current_distance}cm | Decision: {status}')

def main(args=None):
    rclpy.init(args=args)
    brain_node = RoverBrain()
    try:
        rclpy.spin(brain_node)
    except KeyboardInterrupt:
        pass
    finally:
        brain_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
