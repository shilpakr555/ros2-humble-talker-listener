#!/usr/bin/env python3
"""ROS 2 Humble subscriber: receives String messages from /chatter."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.subscription = self.create_subscription(
            String, "chatter", self.message_callback, 10
        )
        self.get_logger().info("Listener started; listening on /chatter")

    def message_callback(self, message):
        self.get_logger().info(f"Received: {message.data}")


def main(args=None):
    rclpy.init(args=args)
    node = Listener()
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
