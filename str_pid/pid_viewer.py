#!/usr/bin/env python

import rclpy
import time
from rclpy.node import Node
from ichthus_can_msgs.msg import Pid
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
import matplotlib.pyplot as plt


class Steer_pid_graph(Node):

  def __init__(self):
    super().__init__("steer_pid_graph")
    self.ref_subs = self.create_subscription(
      Pid, "pid_ang", self.pid_callback, 10)
    self.start_time = time.time()
    self.pid_ang_axis = []
    self.str_time_axis = []
    self.ref_subs
    self.fig = plt.figure()

  def pid_callback(self, data):
    arrive_time = time.time()
    time_index = arrive_time - self.start_time
    print(time_index)
    pid = data.data
    self.pid_ang_axis.append(pid)
    self.str_time_axis.append(time_index)

    plt.xlabel("Time (Seconds)", fontsize=14)
    plt.ylabel("Angle PID Output", fontsize=14)
    plt.plot(self.str_time_axis, self.pid_ang_axis, color="black", label="PID")
    plt.draw()
    plt.pause(0.2)
    self.fig.clear()



def main(args=None):
  rclpy.init(args=args)
  steer_pid_graph = Steer_pid_graph()

  rclpy.spin(steer_pid_graph)

  steer_graph.destroy_node()
  rclpy.shutdown()


if __name__ == "__main__":
  main()
