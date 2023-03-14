#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import time
import os
import serial


class serial_publisher(Node):

    def __init__(self):
        super().__init__('serial_publisher')
        self.publisher_ = self.create_publisher(String, 'serial_power_msg', 10)
        self.update()


    def update(self):
        if os.path.exists('/dev/ttyACM0') == True:
            ser = serial.Serial('/dev/ttyACM0', baudrate=9600,
                                bytesize=8, timeout=20, stopbits=serial.STOPBITS_ONE)

            time.sleep(1)

        while True:
            if ser.in_waiting > 0:
                # Read data out of the buffer until a carraige return / new line is found
                serialString = ser.readline().strip()
                if serialString != '':
                    msg = String()
                    msg.data = serialString.decode().strip()
                    self.publisher_.publish(msg)
                    # Print the contents of the serial data
                    print(serialString.decode().strip())
       
                
def main(args=None):
    rclpy.init(args=args)

    ser = serial_publisher()

    rclpy.spin(ser)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ser.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()