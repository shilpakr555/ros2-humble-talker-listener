#!/usr/bin/env python3
"""ROS 2 Humble publisher: publishes String messages on /chatter."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.publisher = self.create_publisher(String, "chatter", 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.publish_message)
        self.get_logger().info("Talker started; publishing on /chatter")

    def publish_message(self):
        message = String()
        message.data = f"Hello from ROS 2 Talker! Message number: {self.count}"
        self.publisher.publish(message)
        self.get_logger().info(f"Published: {message.data}")
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
